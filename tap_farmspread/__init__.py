#!/usr/bin/env python3

import singer

import tap_framework

from tap_farmspread.client import FarmspreadClient
from tap_farmspread.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class FarmspreadRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=[
        'api_token'])
    client = FarmspreadClient(args.config)
    runner = FarmspreadRunner(args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
