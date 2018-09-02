# 7 - 21 // N x M
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
nb_tirets = 11
motif = ".|."
# print('WELCOM'.rjust((nb_tirets * 2) - 1,'-') + 'E'.ljust(nb_tirets + 1, '-'))
var = 'WELCOME'.center(nb_tirets + 18, '-')
print('WELCOME'.center((nb_tirets * 2 + 7), '-'))
print(len("-----------"))
