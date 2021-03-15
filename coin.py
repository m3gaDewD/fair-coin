import random

class Coin:
    m = 2**32
    a = 1664525
    c = 1013904223

    def __init__(self):
        self.x = random.randint(0, 10000)

    def next(self):
        self.x = (self.a * self.x + self.c) % self.m
        return ['H', 'T'][self.x % 1000 < 500]
