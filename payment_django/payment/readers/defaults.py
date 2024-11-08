from payment import default_settings as settings

from payment.readers.bases import Reader


class DefaultReader(Reader):
    def read(self, bank_type, identifier: str) -> dict:
        """

        :param bank_type:
        :param identifier:
        :return:
        base on bank type for example for BMI:
        {
            'MERCHANT_CODE': '<YOUR INFO>',
            'TERMINAL_CODE': '<YOUR INFO>',
            'SECRET_KEY': '<YOUR INFO>',
        }
        """
        return settings.BANK_GATEWAYS[bank_type]

    def default(self, identifier: str):
        return settings.BANK_DEFAULT

    def currency(self, identifier: str):
        return settings.CURRENCY

    def get_bank_priorities(self, identifier: str) -> list:
        priorities = [self.default(identifier)]
        priorities = list(dict.fromkeys(priorities + settings.BANK_PRIORITIES))
        return priorities
