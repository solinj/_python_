# 1
# 1
# 1
# 2
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#
# x, y, z :  representing the dimensions of a cuboid
# n
# print a list of all possible coordinates given by i, j, k
# on a 3D grid where the sum of i + j + k != n
#
# 0 i x
# 0 j Y
# 0 k z
# Print the list in lexicographic increasing order.

 #

# ar = []
# p = 0
# for i in range ( x + 1 ):
#     for j in range( y + 1):
#         if i+j != n:
#             ar.append([])
#             ar[p] = [ i , j ]
#             p+=1
# print ar
x = 2
y = 2
z = 2
n = 2

print[[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if((i + j + k) != n)]
print [[ i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
