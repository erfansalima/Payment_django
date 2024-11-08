import logging

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from payment import bankfactories
from payment import default_settings as settings
from payment.models import banks as bank_models
from payment.apps import AZIranianBankGatewaysConfig
from payment.exceptions.exceptions import AZBankGatewaysException
from payment.forms import PaymentSampleForm
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def sample_payment_view(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PaymentSampleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            mobile_number = form.cleaned_data["mobile_number"]
            game_id= form.cleaned_data["game_id"]
            factory = bankfactories.BankFactory()
            try:
                bank = factory.create()
                bank.set_request(request)
                bank.set_amount(amount)
                bank.set_game_id(game_id)
                # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
                bank.set_client_callback_url(reverse(settings.SAMPLE_RESULT_NAMESPACE))
                # print(reverse(settings.SAMPLE_RESULT_NAMESPACE))
                bank.set_mobile_number(mobile_number)  # اختیاری

                # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که
                # بعدا بتوانید ارتباط بین محصول یا خدمات را با این
                # پرداخت برقرار کنید.

                bank_record = bank.ready()  # noqa

                # هدایت کاربر به درگاه بانک
                if settings.IS_SAMPLE_FORM_ENABLE:
                    return render(request, 'azbankgateways/redirect_to_bank.html', context=bank.get_gateway())
                return bank.redirect_gateway()
            except AZBankGatewaysException as e:
                logging.critical(e)
                # TODO: redirect to failed result.
                raise e

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentSampleForm()

    return render(request, "azbankgateways/samples/gateway.html", {"form": form})


@api_view(['GET'])
def sample_result_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    return render(request, "azbankgateways/samples/result.html", {"bank_record": bank_record})
