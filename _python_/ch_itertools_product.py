from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))





print list(product([1,2,3],repeat = 1))
#repeat n => n integer in tuples


print list(product([1,2,3],repeat = 2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print list(product([1,2,3],repeat = 3))

# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3),
# (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3),
# (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1), (3, 3, 2), (3, 3, 3)]

print('-----------------------------------')
print list(product([1,2,3],[3,4]))
# première liste : détermine le premier int du tube
# deuxième liste : détermine la suite
