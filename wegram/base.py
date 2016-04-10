# coding: utf-8
from __future__ import unicode_literals, print_function
from datetime import datetime

from requests import post

class TelegramAdapter(object):
    def send(self, msg):
        raise RuntimeError('Should be implemented in subclass')


class TelegramBotAdapter(TelegramAdapter):
    def __init__(self, token):
        super(TelegramBotAdapter, self).__init__()
        self.__token = token
        self.__bot = None  # FIXME

    def send(self, msg):
        # Allowed data types: text, image
        # Raise error for other types
        # Wrap text in markdown
        # Send text
        # Send images
        pass


class Eth0Adapter(TelegramAdapter):
    API_URL = 'https://eth-nookcloud.rhcloud.com/bot/push'

    def __init__(self, push_code):
        super(Eth0Adapter, self).__init__()
        self.__token = push_code

    def send(self, msg):
        msg['body'] = msg['body']#.replace()
        msg['time'] = datetime.fromtimestamp(msg['time']).strftime('%H:%M:%S')
        group = msg.get('group', None)
        content = '*WeChatForwardBot*'
        if group:
            content += ' [群:{group}]'.format(**msg)
        content += '\n*{from}*: {body}\n{time}'.format(**msg)
        print(content)
        try:
            post(
                self.API_URL,
                data={
                    'code': self.__token,
                    'text': content,
                }
            )
        except Exception as e:
            print(e)
        # TODO more types
        # Allowed data types: text
        # Raise error for other types
        # Wrap text in markdown
        # Send text
        pass

