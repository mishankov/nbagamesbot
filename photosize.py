class PhotoSize:
    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height

        if file_size is None:
            self.file_size = ''
        else:
            self.file_size = file_size

    @classmethod
    def from_json(cls, json):
        file_id = json['file_id']
        width = json['width']
        height = json['height']

        if 'file_size' in json.keys():
            file_size = json['file_size']
        else:
            file_size = None

        return cls(file_id, width, height, file_size)