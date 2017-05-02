# encoding: utf-8
from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, height, weight, age, cloth):
        self.height = height
        self.weight = weight
        self.age = age
        self.cloth = cloth

    @abstractmethod
    def set_cloth(self, cloth):
        pass
