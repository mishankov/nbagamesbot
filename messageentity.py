from user import User


class MessageEntity:
    def __init__(self, type, offset, length, url=None, user=None):
        self.type = type
        self.offset = offset
        self.length = length

        if url is None:
            self.url = ''
        else:
            self.url = url

        if user is None:
            self.user = ''
        else:
            self.user = user

    @classmethod
    def from_json(cls, json):
        type = json['type']
        offset = json['offset']
        length = json['length']

        if 'url' in json.keys():
            url = json['url']
        else:
            url = None

        if 'user' in json.keys():
            user = User.from_json(json['user'])
        else:
            user = None

        return cls(type, offset, length, url, user)
