from .hives import Hive
from .bees import Bee


class MyBee(Bee):
    pass


class MyHive(Hive):
    bee = MyBee()


print(MyHive._bees)