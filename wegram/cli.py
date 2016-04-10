# coding: utf-8
from __future__ import unicode_literals, print_function
import os
import logging
import json

os.environ['WEGRAM_FORWARD_TYPES'] = json.dumps([
    1, 3, 34, 42, 47, 49, 62,
])

if os.environ.get('ETH0_PUSH_CODE', None):
    from .base import Eth0Adapter
    TELEGRAM_ADAPTER = Eth0Adapter(os.environ['ETH0_PUSH_CODE'])
elif os.environ.get('TELEGRAM_BOT_TOKEN', None):
    from .base import TelegramBotAdapter
    TELEGRAM_ADAPTER = TelegramBotAdapter(os.environ['TELEGRAM_BOT_TOKEN'])
else:
    raise RuntimeError('No Telegram adapter could be inited')

from weixinbot import weixin

def start():
    # Logging to console
    logger = logging.getLogger(__name__)
    import coloredlogs
    coloredlogs.install(level='DEBUG')

    # Weixin bot init
    wxbot = weixin.WebWeixin()
    wxbot.telegram_adapter = TELEGRAM_ADAPTER
    wxbot.start()


if __name__ == '__main__':
    start()

