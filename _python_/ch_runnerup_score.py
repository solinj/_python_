# You are given n scores. Store them in a list and find the score of the runner-up.
# The first line contains n.
# The second line contains an array a[i]  of  integers each separated by a space.

# li = [2, 3, 6, 6, 5]
# x_max = max(li)
# # print(x_max)
# print(li)
# for i in range(len(li) + 1):
#     # x_max = max(li)
#     if li[i] == max(li):
#         li.remove(max(li))
#     print(li)



# arr = list(map(int, x.split()))
# x_max = max(arr)
# arr.remove(arr[len(arr) - 1])
# print(arr)










def runner(arrbo):
    x_max = max(arrbo)
    arrb = []
    for i in range(len(arrbo)):
        if arrbo[i] < (max(arrbo)):
            arrb.append(arrbo[i])
    return max(arrb)




# arr = "2 3 5 6"

arrbo = [2, 3, 6, 5, 6]
print(runner(arrbo))

















#     print(arr[i])

        # print arr
    # print(max(arr))
    # # print(arr[i])
    # print(type(i))
# runner(x)
# n = nbre de scores
# A[i]
