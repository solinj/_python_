# x, y, z
# i, j, k
# x = 2
# y = 2
# z = 2
# n = 2
# cpt = 0
# li = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if(i + j + k) != n:
#                 li.append([])
#                 li[cpt] = [ i , j, k ]
#             # li = li + [[i] + [j]]
#                 cpt = cpt + 1
#
# print(li)
x = 2
y = 2
z = 2
n = 2
print[[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if((i + j + k) != n)]
