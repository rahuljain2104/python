# Question
# 22
# Max.Marks
# 100.00
# Reversed
# Linked
# List
#
# You
# are
# given
# a
# linked
# list
# that
# contains
#
# integers.You
# have
# performed
# the
# following
# reverse
# operation
# on
# the
# list:
#
# Select
# all
# the
# subparts
# of
# the
# list
# that
# contain
# only
# even
# integers.For
# example,
# if the list is
#
# , then
# the
# selected
# subparts
# will
# be,
# .
# Reverse
# the
# selected
# subpart
# such as
# and
#
# .
#
# Now, you
# are
# required
# to
# retrieve
# the
# original
# list.
#
# Note: You
# should
# use
# the
# following
# definition
# of
# the
# linked
# list
# for this problem:
#
#
# class Node {
# Object data;
# Node next;
# }
#
#
# Input
# format
#
# First
# line:
#
# Next
# line:
#
# space - separated
# integers
# that
# denote
# elements
# of
# the
# reverse
# list
#
# Output
# format
#
# Print
# the
#
# elements
# of
# the
# original
# list.
#
# Constraints
#
# Sample
# Input
#
# 9
# 2
# 18
# 24
# 3
# 5
# 7
# 9
# 6
# 12
#
# Sample
# Output
#
# 24
# 18
# 2
# 3
# 5
# 7
# 9
# 12
# 6


N = int(input())
linked_list = [int(item) for item in input().split()]
# N = 9
# linked_list = [2, 18, 24, 3, 5, 7, 9, 6, 12]
res = []
i = 0
sublist = []
while N > i:
    for elem in sublist[::-1]:
        res.append(elem)
    if linked_list[i] % 2 != 0:
        res.append(str(linked_list[i]))
        i += 1
        sublist = []
        continue
    sublist = []
    while  N > i and linked_list[i] % 2 == 0:
        sublist.append(str(linked_list[i]))
        i += 1
for elem in sublist[::-1]:
    res.append(elem)

print(' '.join(res))

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i-1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end=" ")