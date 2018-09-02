#!/usr/bin/env python3
# coding: utf-8

class ZDict(object):
    def __init__(self):
        self._dict = {}

our_dict = ZDict()
print(our_dict._dict)
our_dict._dict["key"] = "value"
print(our_dict._dict["key"])
print(our_dict._dict.__len__())


"""ma_liste = [1, 2, 3, 4, 5]
8 in ma_liste # Revient au même que ...
ma_liste.__contains__(8)


def __getitem__(self, index):
        """"""Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]""""""

        return self._dictionnaire[index]
def __setitem__(self, index, valeur):
        """"""Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur""""""

        self._dictionnaire[index] = valeur

objet.__len__()"""
