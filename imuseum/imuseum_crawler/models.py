class Model(dict):
    pass


class City(Model):
    pass


class Museum(Model):
    fields = [
        {
            "key": "id",
            "type": "string"
        }
    ]


class Event(Model):
    fields = [
        {
            "key": "id",
            "type": "string"
        },
        {
            "key": "title",
            "type": "string"
        },
        {
            "key": "subtitle",
            "type": "int"
        },
        {
            "key": "address",
            "type": "string"
        },
        {
            "key": "summary",
            "type": "string"
        },
        {
            "key": "description",
            "type": "html"
        },
        {
            "key": "when",
            "type": "tuple"
        },
        {
            "key": "museum",
            "type": "string"
        },
        {
            "key": "price",
            "type": "tuple"
        }

    ]


class User(Model):
    fields = [
        {
            "key": "name",
            "type": "string"
        },
        {
            "key": "avatar",
            "type": "url"
        },
        {
            "key": "id",
            "type": "string"
        }

    ]


class Activity(Model):
    pass


class Following(Model):
    pass


class Mark(Model):
    pass


class Like(Model):
    pass
