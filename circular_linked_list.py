#  https://www.hackerearth.com/challenge/hiring/vocera-hiring-challenge-2018
#  Infinite Circular Doubly Linked List
#
# You are given a circular doubly linked list that contains integers as the data in each node. These data on each node is distinct. You have developed a special algorithm that prints the three continuous elements of the list, starting from the first element or head of the list and runs for infinite time. For example, if the list is
# , then the output of the algorithm will be
#
# . The output contains the infinite number of elements because it is a circular list.
#
# You are given only a part of the output that has been returned by the algorithm. Your task is to determine the number of elements available in the original list and print the respective elements.
#
# Note
#
#     It is guaranteed that the provided part of the output of the algorithm is sufficient enough to calculate the size of the original list.
#     Please read the sample explanation carefully and use the following definition of the doubly linked list:
#
# class Node {
#     Object data;
#     Node next;
#     Node prev;
# }
#
# Input format
#
#     First line: Integer
#
#  that denotes the length of the list which is returned as the output of the algorithm
# Next line:
#
#     space-separated integers that denote the elements of the list which is returned as the output of the algorithm
#
# Output format
#
# Your task is to print the output in the following format:
#
#     First line: Length of the original list
#     Second line: Space-separated integers that denote the elements of the original list
# Sample Input
#
# 10
# 7 12 8 12 8 13 8 13 7 13
#
# Sample Output
#
# 4
# 7 12 8 13
#
# Explanation
#
# The hidden list is actually
# with elements hence the output is
#
# .
#
# Note: You can see that the above list actually matches the output of the program of Alice
#
# Note: Your code should be able to convert the sample input into the sample output. However,
# this is not enough to pass the challenge, because the code will be run on multiple test cases.
# Therefore, your code must solve this problem statement.

N = input()
circular_list = input().split()
res = []

for i, elem in enumerate(circular_list):
    if elem not in res:
        res.append(elem)
    if elem == circular_list[0] and i > 0:
        break
print(len(res))
print(' '.join(res))
