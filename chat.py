class Chat:
    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None,
                 all_members_are_administrators=None):
        self.id = id
        self.type = type

        if 'title' is None:
            self.title = ''
        else:
            self.title = title

        if 'username' is None:
            self.username = ''
        else:
            self.username = username

        if 'first_name' is None:
            self.first_name = ''
        else:
            self.first_name = first_name

        if 'last_name' is None:
            self.last_name = ''
        else:
            self.last_name = last_name

        if 'all_members_are_administrators' is None:
            self.all_members_are_administrators = ''
        else:
            self.all_members_are_administrators = all_members_are_administrators

    @classmethod
    def from_json(cls, json):
        id = json['id']
        type = json['type']

        if 'title' in json.keys():
            title = json['title']
        else:
            title = ''

        if 'username' in json.keys():
            username = json['username']
        else:
            username = ''

        if 'first_name' in json.keys():
            first_name = json['first_name']
        else:
            first_name = ''

        if 'last_name' in json.keys():
            last_name = json['last_name']
        else:
            last_name = ''

        if 'all_members_are_administrators' in json.keys():
            all_members_are_administrators = json['all_members_are_administrators']
        else:
            all_members_are_administrators = ''

        return cls(id, type, title, username, first_name, last_name, all_members_are_administrators)
