

# min_arr = [int(num[0]), int(num[1])]
#         for n in num:
#             n = int(n)
#             if n < min_arr[0]:
#                 min_arr[0] = n
#             elif n < min_arr[1]:
#                 min_arr[1] = n

# def can_give_change(arr):
#     reserve = 0
#     for i, note in enumerate(arr):
#         if note == 5:
#             reserve += 5
#             continue
#         else:
#             reserve -= (note-5)
#         if reserve < 0:
#             return i+1
#     return 0
#
# print(can_give_change([5,20]))
#



# def find_path(matrix, target_string):
#     i = 0
#     j = 0
#     res = ''
#     for k in range(len(target_string)-1):
#         if matrix[i][j] != target_string[k]:
#             return 'NO PATH'
#         if target_string[k+1] == matrix[i][j+1]:
#             j += 1
#             res += 'R'
#             continue
#         if target_string[k + 1] == matrix[i+1][j]:
#             i += 1
#             res += 'D'
#             continue
#
#     return res

def find_path(matrix, target_string, res = '', i = 0, j = 0, k = 0):

    if matrix[i][j] != target_string[k]:
        return 'NO PATH'
    k +=1
    if target_string[k] == matrix[i][j+1]:
        j += 1
        res += 'R'
        find_path(matrix, target_string, res, i, j, k)
    if target_string[k] == matrix[i+1][j]:
        i += 1
        res += 'D'
        find_path(matrix, target_string, res, i, j, k)
    return res


print(find_path([['a','b','a','d',],['n','j','k','m',],['e','f','q','z',]], 'abjfqz'))