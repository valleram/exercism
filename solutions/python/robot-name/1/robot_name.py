#!/usr/bin/env python3

from random import sample, seed
from string import ascii_uppercase


class Robot:

    used_names = set()

    def __init__(self):
        self.name = self.name_generator()

    def name_generator(self):
        alpha_num = [i for i in map(str, (sample(ascii_uppercase, 2) + \
                                          sample(range(10), 3)))]
        name = ''.join(alpha_num)
        if name not in Robot.used_names:
            Robot.used_names.add(name)
            return name
        else:
            self.name_generator()

    def reset(self):
            seed(42)
            self.name =  self.name_generator()
