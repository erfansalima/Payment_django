# Generated by Django 5.0.7 on 2024-08-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WAITING', 'Waiting'), ('REDIRECT_TO_BANK', 'Redirect to bank'), ('RETURN_FROM_BANK', 'Return from bank'), ('CANCEL_BY_USER', 'Cancel by user'), ('EXPIRE_GATEWAY_TOKEN', 'Expire gateway token'), ('EXPIRE_VERIFY_PAYMENT', 'Expire verify payment'), ('COMPLETE', 'Complete'), ('ERROR', 'Unknown error acquired')], max_length=50, verbose_name='Status')),
                ('bank_type', models.CharField(choices=[('BMI', 'BMI'), ('SEP', 'SEP'), ('ZARINPAL', 'Zarinpal'), ('IDPAY', 'IDPay'), ('ZIBAL', 'Zibal'), ('BAHAMTA', 'Bahamta'), ('MELLAT', 'Mellat'), ('PAYV1', 'PayV1')], max_length=50, verbose_name='Bank')),
                ('tracking_code', models.CharField(max_length=255, verbose_name='Tracking code')),
                ('amount', models.CharField(max_length=10, verbose_name='Amount')),
                ('reference_number', models.CharField(max_length=255, unique=True, verbose_name='Reference number')),
                ('response_result', models.TextField(blank=True, null=True, verbose_name='Bank result')),
                ('callback_url', models.TextField(verbose_name='Callback url')),
                ('extra_information', models.TextField(blank=True, null=True, verbose_name='Extra information')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Bank gateway',
                'verbose_name_plural': 'Bank gateways',
            },
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='game',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]