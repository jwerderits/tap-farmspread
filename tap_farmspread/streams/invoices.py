from tap_farmspread.streams.base import BaseStream
import singer
import json

LOGGER = singer.get_logger()


class InvoicesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'invoices'
    KEY_PROPERTIES = ['sid']

    @property
    def path(self):
        return '{}/invoices'.format(self.BASE_URL)
