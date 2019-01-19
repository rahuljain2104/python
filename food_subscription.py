# Food Subscription
# You want to buy a food subscription package for the upcoming month. You know exactly the days on which you will eat.
# This month has 30 days and there are 3 types of packages that available :
#
# 1-Day Package - 199 valid for one day.
# 7-Day Package - 699 valid for 7 consecutive days.
# 30-Day Package - 2499 valid for all 30 days of the month.
# You want to pay as little as possible. You will be given a sorted (in increasing order) array A of dates when you will be eating. For example, given:
#
# You can buy 7-Day and 1-day subscription. The two 1-day subscriptions should be used on days 29 and 30.
# The 7-day subscription should be used on the first seven days of the month. The total cost is 1097 and there is no other possible way of paying less.
#
# Write a function:
#
# function solution (A) { } that, given an array  consisting of  integers that specifies days on which you will eat,
# returns the minimum amount of money that you have to spend on food subscription for the month.
#
# Input Format
# An array  of  days where you would be eating.
#
# Output Format
# The minimum amount of money that you have to spend.
#
# Constraints
#
#  is an integer within the range ;
# Each element of array is an integer within the range
# Array  is sorted in increasing order
# The element of  is all distinct.


# one_day = 199
# seven_days = 699
# thirty_days = 2499
#
# N = 13
# days = [1, 4 , 5, 6, 7, 10, 11, 12, 15, 17, 18, 19, 20]
# # N = input()
# # days = [int(item) for item in input().split()]
#
# def find_min_sum(lst, ):
#
# def min_amount(N, days):
#     if N >= 25:
#         return thirty_days
#     if N <= 3:
#         return one_day*N
#     relative_dist = [days[i+1]-days[i] for i in range(N-1)]
#
#     print(relative_dist)
#
# print(min_amount(N, days=days))
