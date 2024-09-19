# This file is placed in the Public Domain.


"broker"


from .object import Object, matchkey, values


class Broker:

    "Broker"

    objs = Object()

    @staticmethod
    def add(obj, key):
        "add object."
        setattr(Broker.objs, key, obj)

    @staticmethod
    def all(type=None):
        "return all objects."
        if type:
            for key in matchkey(Broker.objs, type):
                yield Broker.get(key)
        return values(Broker.objs)

    @staticmethod
    def get(orig):
        "return object by matching repr."
        return getattr(Broker.objs, orig, None)


def __dir__():
    return (
        'Broker',
    )
