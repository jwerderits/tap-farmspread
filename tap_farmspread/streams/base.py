import math
import pytz
import singer
import singer.utils
import singer.metrics
import time

from datetime import timedelta, datetime
from tap_framework.streams import BaseStream as base
import json

LOGGER = singer.get_logger()

class BaseStream(base):
    KEY_PROPERTIES = ['id']
    BASE_URL = 'https://farmspread.com/api/1.0'


    def sync_data(self):
        table = self.TABLE
        # LOGGER.info('the apit method is {} and the url is {}'.format(self.API_METHOD, self.path))

        raw_result = self.client.make_request(self.path, self.API_METHOD)
        result = json.loads(raw_result)

        with singer.metrics.record_counter(endpoint=table) as counter:
            singer.write_records(table, result)
            counter.increment(len(result))
