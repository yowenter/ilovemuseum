class Model(dict):
    pass


class City(Model):
    pass


class Museum(Model):
    pass


class Event(Model):
    fields = [
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
        
    ]


class Activity(Model):
    pass
