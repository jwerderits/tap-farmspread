import math
import pytz
import singer
import singer.utils
import singer.metrics
import time

from datetime import timedelta, datetime
from tap_framework.streams import BaseStream as base


LOGGER = singer.get_logger()

class BaseStream(base):
    KEY_PROPERTIES = ['id']
    BASE_URL = 'https://farmspread.com/api/1.0'


    def sync_data(self):
        table = self.TABLE
        # LOGGER.info('the apit method is {} and the url is {}'.format(self.API_METHOD, self.path))
        result = self.client.make_request(self.path, self.API_METHOD)
