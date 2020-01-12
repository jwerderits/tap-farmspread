import requests
import singer
import singer.metrics
import json

LOGGER = singer.get_logger()


class FarmspreadClient:

    MAX_TRIES = 5

    def __init__(self, config):
        self.config = config


    def make_request(self, url, method, params=None, body=None):

        headers = {
            "X-API-KEY": "{}".format(self.config['api_token'])
        }
        response = requests.request(
            method,
            url,
            params=params,
            headers=headers)

        if response.status_code != 200:
            LOGGER.info('status={}'.format(response.status_code))
            raise RuntimeError(response.text)

        return response.text
