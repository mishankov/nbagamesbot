from message import Message


class Update:
    def __init__(self, update_id, message=None, edited_message=None, channel_post=None, edited_channel_post=None):
        self.update_id = update_id

        if message is None:
            self.message = ''
        else:
            self.message = message

        if edited_message is None:
            self.edited_message = ''
        else:
            self.edited_message = edited_message

        if channel_post is None:
            self.channel_post = ''
        else:
            self.channel_post = channel_post

        if edited_channel_post is None:
            self.edited_channel_post = ''
        else:
            self.edited_channel_post = edited_channel_post

    @classmethod
    def from_json(cls, json):
        update_id = json['update_id']

        if 'message' in json.keys():
            message = Message.from_json(json['message'])
        else:
            message = None

        if 'edited_message' in json.keys():
            edited_message = Message.from_json(json['edited_message'])
        else:
            edited_message = None

        if 'channel_post' in json.keys():
            channel_post = Message.from_json(json['channel_post'])
        else:
            channel_post = None

        if 'edited_channel_post' in json.keys():
            edited_channel_post = Message.from_json(json['edited_channel_post'])
        else:
            edited_channel_post = None

        return cls(update_id, message, edited_message, channel_post, edited_channel_post)
