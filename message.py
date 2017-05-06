from chat import Chat
from user import User


class Message:
    """
    'from' in API is 'sender' here
    """

    def __init__(self, message_id, date, chat, sender=None, text=None):
        self.message_id = message_id
        self.date = date
        self.chat = chat

        if sender is None:
            self.sender = ''
        else:
            self.sender = sender

        if text is None:
            self.text = ''
        else:
            self.text = text

    @classmethod
    def from_json(cls, json):
        message_id = json['message_id']
        date = json['date']
        chat = Chat.from_json(json['chat'])

        if 'from' in json.keys():
            sender = User.from_json(json['from'])
        else:
            sender = None

        if 'text' in json.keys():
            text = json['text']
        else:
            text = None

        return cls(message_id, date, chat, sender, text)
