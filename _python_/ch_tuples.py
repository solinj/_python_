# given integer representing n integers
# given n n integers separated by blanks
# => put them in tuple and hash them

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))
