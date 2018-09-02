#!/usr/bin/env python3
# coding: utf-8

nom_func = lambda x:x * 2
print(nom_func(3))


etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

print(sorted(etudiants, key=lambda c: c[2]))

# >>> sorted(etudiants, key=lambda colonnes: colonnes[2])
# [
#     ('Thomas', 11, 12),
#     ('Charles', 12, 15),
#     ('Damien', 12, 15),
#     ('Clément', 14, 16),
#     ('Oriane', 14, 18)
# ]
# >>>


class Etudiants(object):

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne
    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)

marie = Etudiants("marie", 10, 20)
edouard = Etudiants("edouard", 10, 15)

#print(marie.__repr__())
li = []
li.append(Etudiants("marie", 10, 20))
li.append(Etudiants("edouard", 10, 15))
print(sorted(li, key = lambda c:c.moyenne, reverse = True))
