from __future__ import absolute_import, unicode_literals

import importlib
import logging


from payment import default_settings as settings
from payment.bank.mellat import Mellat
from payment.exceptions.exceptions import BankGatewayAutoConnectionFailed
from payment.models.banks import BankType

class BankFactory:
    def __init__(self):
        logging.debug("Create bank factory")
        self._secret_value_reader = self._import(settings.SETTING_VALUE_READER_CLASS)()

    @staticmethod
    def _import(path):
        package, attr = path.rsplit(".", 1)
        klass = getattr(importlib.import_module(package), attr)
        return klass

    def _import_bank(self, bank_type: BankType, identifier: str):
        """
        helper to import bank aliases from string paths.

        raises an AttributeError if a bank can't be found by it's alias
        """
        bank_class = self._import(self._secret_value_reader.klass(bank_type=bank_type, identifier=identifier))
        logging.debug("Import bank class")

        return bank_class, self._secret_value_reader.read(bank_type=bank_type, identifier=identifier)

    def create(self, bank_type: BankType = None, identifier: str = "1") ->Mellat:
        """Build bank class"""
        # if not bank_type:
        #     bank_type = self._secret_value_reader.default(identifier)
        # logging.debug("Request create bank", extra={"bank_type": bank_type})

        # bank_klass, bank_settings = self._import_bank(bank_type, identifier)
        # bank = bank_klass(**bank_settings, identifier=identifier)
        bank= Mellat()
        bank.set_currency(self._secret_value_reader.currency(identifier))

        logging.debug("Create bank")
        return bank