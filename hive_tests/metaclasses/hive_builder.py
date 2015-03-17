from .hive_type import HiveType
from ..bees import Bee


class RegisterDict(dict):

    def __init__(self, condition, callback):
        super().__init__()

        self._condition = condition
        self._callback = callback

    def __setitem__(self, name, value):
        if self._condition(value):
            self._callback(name, value)

        else:
            super().__setitem__(name, value)


class HiveBuilder(HiveType):

    @classmethod
    def __prepare__(metacls, name, bases):
        bee_dict = {}

        is_bee = lambda v: isinstance(v, Bee)
        store_bee = lambda k, v: bee_dict.__setitem__(k, v)

        cls_dict = RegisterDict(is_bee, store_bee)
        cls_dict['_bees'] = bee_dict
        return cls_dict
#