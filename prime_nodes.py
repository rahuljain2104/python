# https://www.hackerearth.com/challenge/hiring/utopus-back-end-hiring-2018
from math import sqrt
N = int(input())
count = 0
last_parent = 1
sum = 0

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

for i in range(N-1):
    p, c = map(int, input().split())
    if p == last_parent:
        sum += c
    else:
        if is_prime(sum):
            count += 1
        last_parent = p
        sum = c
if is_prime(sum):
    count += 1
print(count)