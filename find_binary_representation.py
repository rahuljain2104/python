A = [1,0,0,1,1,1]
import math
def formula(arr):
    summation = 0
    for index, value in enumerate(arr):
        summation += value*(-2)**index
    return summation

def max_bit(val):
    signbit = 1 if val > 0 else 0
    if signbit:
        count = 0
        summation = 0
        while val > summation:
            summation += 2**count
            count += 2
    else:
        count = 1
        summation = 0
        while val < summation:
            summation += (-2)**count
            count += 2
    return count


def printbinary(lst, val):
    for item in lst:
        t = [int(i) for i in item.split()]
        if formula(t) == val:
            print(t)
            return

def perms(n):
    if not n:
        return
    for i in range(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s



def solution(A):
    val = formula(A)
    val = math.ceil(val/2)
    num_bits = max_bit(val)
    lists = list(perms(5))

