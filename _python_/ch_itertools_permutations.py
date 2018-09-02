from itertools import permutations
print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]




inp = input().split()
strg = inp[0]
k = int(inp[1])
final_strg = ""

#inter_strg = list(permutations(strg, k))
#print(inter_strg)
inter_strg = sorted(list(map("".join, permutations(strg, k))))


for i in range(len(inter_strg)):
    final_strg += inter_strg[i] + '\n'
print(final_strg.upper())
