# You are given an integer sequence 1,2,…,n. You have to divide it into two sets A and B in such a way that each element belongs to exactly one set and |sum(A)−sum(B)| is minimum possible.
#
# The value |x| is the absolute value of x and sum(S) is the sum of elements of the set S.
#
# Input
# The first line of the input contains one integer n (1≤n≤2⋅109).
#
# Output
# Print one integer — the minimum possible value of |sum(A)−sum(B)| if you divide the initial sequence 1,2,…,n into two sets A and B.


n = int(input()) % 4
if n == 3 or n == 0:
    print(0)

if n == 2 or n == 1:
    print(1)

