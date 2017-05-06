# _*_ coding: utf-8 _*_
import requests
from constants import *
import telegramdatamodel as dm


class Bot:
    def __init__(self, token, default_parse_mode=''):
        self.token = token

        self.default_parse_mode = default_parse_mode

    def set_default_parse_mode(self, name):
        """
        Set default value for parse_mode param in send_message() method

        :param str name: should be 'HTML', 'Markdown' or ''
        :return: nothing
        """
        self.default_parse_mode = name

    def get_me(self):
        return requests.post(URL + self.token + '/getMe').json()

    def get_updates(self, offset='', limit=100, timeout=0, allowed_updates=''):
        """
        Use this method to receive incoming updates
        :param offset: 
        :param limit: 
        :param timeout: 
        :param allowed_updates: 
        :return: list of Update objects or False, if no updates
        """
        if allowed_updates == '':
            allowed_updates_str = '[]'
        else:
            allowed_updates_str = '["' + '", "'.join(allowed_updates) + '"]'

        json = requests.post(URL + self.token + '/getUpdates?offset=' + str(offset) +
                             '&limit=' + str(limit) +
                             '&timeout=' + str(timeout) +
                             '&allowed_updates=' + allowed_updates_str).json()

        if json['ok'] is True:
            json_list = json['result']
        else:
            return False

        update_list = []
        for update in json_list:
            update_list.append(dm.Update.from_json(update))

        return update_list

    def send_message(self, chat_id, text, parse_mode=None, disable_web_page_preview=False, disable_notification=False,
                     reply_to_message_id='', reply_markup=''):
        if parse_mode is None:
            parse_mode = self.default_parse_mode

        return requests.post(URL + self.token +
                             '/sendMessage?chat_id=' + str(chat_id) +
                             '&text=' + str(text) +
                             '&parse_mode=' + str(parse_mode) +
                             '&disable_web_page_preview=' + str(disable_web_page_preview) +
                             '&disable_notification=' + str(disable_notification) +
                             '&reply_to_message_id=' + str(reply_to_message_id) +
                             '&reply_markup=' + str(reply_markup)).json()
