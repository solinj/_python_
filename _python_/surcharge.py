#!/usr/bin/env python3
# coding: utf-8
class Duree(object):

    def __init__(self, min = 0, sec = 0):
        self.min = min
        self.sec = sec

    def __str__(self):
        #EST UN FORMATAGE
        return "{0:02}:{1:02}".format(self.min, self.sec)

dur = Duree()
print(dur.min)

dur1 = Duree(1, 3)
print(dur1.min)

print(dur1.min.__add__(4))
