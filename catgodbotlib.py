# _*_ coding: utf-8 _*_
import requests
from constants import *


class Bot:
    def __init__(self, token):
        self.token = token

    def get_me(self):
        return requests.post(URL + self.token + '/getMe')

    def get_updates(self, **kwargs):
        offset = kwargs.get('offset', '')
        limit = kwargs.get('limit', 100)
        timeout = kwargs.get('timeout', 0)
        allowed_updates = kwargs.get('allowed_updates', [])

        if len(allowed_updates) > 0:
            allowed_updates_str = '["' + '", "'.join(allowed_updates) + '"]'
        else:
            allowed_updates_str = '[]'

        return requests.post(URL + self.token + '/getUpdates?offset=' + str(offset) +
                             '&limit=' + str(limit) +
                             '&timeout=' + str(timeout) +
                             '&allowed_updates=' + allowed_updates_str)

    def send_message(self, chat_id, text, **kwargs):
        parse_mode = kwargs.get('parse_mode', '')
        disable_web_page_preview = kwargs.get('disable_web_page_preview', 'False')
        disable_notification = kwargs.get('disable_notification', 'False')
        reply_to_message_id = kwargs.get('reply_to_message_id', '')
        reply_markup = kwargs.get('reply_markup', '')

        return requests.post(URL + self.token +
                             '/sendMessage?chat_id=' + str(chat_id) +
                             '&text=' + str(text) +
                             '&parse_mode=' + str(parse_mode) +
                             '&disable_web_page_preview=' + str(disable_web_page_preview) +
                             '&disable_notification=' + str(disable_notification) +
                             '&reply_to_message_id=' + str(reply_to_message_id) +
                             '&reply_markup=' + str(reply_markup))
