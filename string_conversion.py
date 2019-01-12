# "Alfred" Rebel's cute but innovative personal butler bot, decides to play a game to give us some relief from being too awesome in our day to day operations. He would be giving us two strings and would ask us to make them identical, using the minimum actions possible of the following types:
#
# Select any character in any of the strings and repeat it (add another instance of this character exactly after it). For example, in a single move "abc" could be changed to "abbc" (by repeating the character 'b').
# Select any two adjacent and identical characters in any of the strings, and delete one of them.
# For example, in a single move, "abbc" could be changed to "abc" (delete one of the 'b' characters), but can't convert it to "bbc".
# The  actions are independent i.e. it's not necessary that an act of the first type should be followed by an action of the second type (or vice versa).
# We decided to beat Alfred by writing a program to find if it is possible to make the given strings identical and to find the minimum number of moves if it is possible or print "Not possible" if the solution is not possible to derive.
#
# Write a function:
#
# function solution (string A, string B) {} that given 2 strings A and B, returns the minimum no. of tasks required to do so and "Not possible" if the solution is not possible to derive.
#
# Input Format
# Input would be the 2 strings in consideration one in each line. Each string is non-empty and will consist of lower case English characters only, from 'a' to 'z'.
#
# Output Format
# If the two strings could be made identical print the minimum no. of tasks required to do so and "Not possible" if the solution is not possible to derive.
#
# Constraints
#
# Sample Input
# rebel
# reebel

str1 = input()
str2 = input()

def compare_str(str1, str2):
    i = j = 1
    count = 0
    if str1[0] != str2[0] and str1[-1] != str2[-1]:
        return 'Not Possible'

    while len(str1) > i or len(str2) > j :
        try:
            if str1[i] == str2[j]:
                i += 1
                j += 1
                continue
        except:
            if j > len(str2)-1:
                count += len(str1)-i+1
            if i > len(str1)-1:
                count += len(str2) - j+1
            return count

        if str1[i] != str1[i-1] and str2[j] != str2[j-1]:
            return 'Not Possible'

        while str1[i] == str1[i-1]:
            i += 1
            count += 1
            continue

        while str2[j] == str2[j-1]:
            j += 1
            count += 1
            continue
    return count

if not set(str1) == set(str2):
    print("Not possible")
else:
    print(compare_str(str1, str2))

# def compare_str(str1, str2):
#     count = 0
#     j = 0
#     for i, ch in enumerate(str1):
#         flag = False
#         if str2[j] == ch:
#             j += 1
#             continue
#         if str2[j] == str2[j-1]:
#             while str2[j] != ch:
#                 j += 1
#                 count += 1
#                 flag = True
#         if flag:
#             j += 1
#             continue
#         if ch == str1[i - 1]:
#             count += 1
#             continue
#         else:
#             return 'Not possible'
#     return count









        # else:
        #     print('Not possible')
        #     break



