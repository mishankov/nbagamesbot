class User:
    def __init__(self, id, first_name, last_name=None, username=None):
        self.id = id
        self.first_name = first_name

        if 'last_name' is None:
            self.last_name = ''
        else:
            self.last_name = last_name

        if 'username' is None:
            self.username = ''
        else:
            self.username = username

    @classmethod
    def from_json(cls, json):
        id = json['id']
        first_name = json['first_name']

        if 'last_name' in json.keys():
            last_name = json['last_name']
        else:
            last_name = None

        if 'username' in json.keys():
            username = json['username']
        else:
            username = None

        return cls(id, first_name, last_name, username)
