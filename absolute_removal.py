# T = int(input())
# def find_index(arr):
#     max_val = 0
#     index = 0
#     for i in range(1, len(arr)-1):
#         if abs(arr[i] - arr[i - 1]) + abs(-arr[i] + arr[i + 1]) > max_val:
#             max_val = abs(arr[i] - arr[i - 1]) + abs(arr[i+1] - arr[i])
#             index = i
#     if index  == 1:
#         if (arr[1]-arr[0]) > arr[2]-arr[1] and arr[0] > arr[1]:
#             index = 0
#     if index == len(arr)-2:
#         if (arr[-1] - arr[-2]) > arr[-2] - arr[-3] and arr[-1] > arr[-2]:
#             index = len(arr)-1
#     return index
#
# def find_sum(arr):
#     summation = 0
#     for i in range(len(arr)-1):
#         summation += abs(arr[i+1]-arr[i])
#     return summation
#
#
# for t in range(T):
#     N = input()
#     arr = [int(item) for item in input().split()]
#     index = find_index(arr)
#     del arr[index]
#     print(find_sum(arr))

T = int(input())
def find_index(arr):
    max_val = 0
    index = 0
    for i in range(1, len(arr)-1):
        if abs(arr[i] - arr[i - 1]) + abs(-arr[i] + arr[i + 1]) > max_val:
            max_val = abs(arr[i] - arr[i - 1]) + abs(arr[i+1] - arr[i])
            index = i
    if index == 1:
        if (arr[1]-arr[0]) > arr[2]-arr[1] and arr[0] > arr[1]:
            index = 0
    if index == len(arr)-2:
        if (arr[-1] - arr[-2]) > arr[-2] - arr[-3] and arr[-1] > arr[-2]:
            index = len(arr)-1
    return index

def find_sum(arr):
    summation = 0
    for i in range(len(arr)-1):
        summation += abs(arr[i+1]-arr[i])
    return summation


for t in range(T):
    N = input()
    arr = [int(item) for item in input().split()]
    index = find_index(arr)
    del arr[index]
    print(find_sum(arr))



