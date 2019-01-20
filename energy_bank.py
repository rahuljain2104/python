# https://www.hackerearth.com/challenge/hiring/utopus-back-end-hiring-2018
N = input()
maximum = 0
summation = 0
for energy in input().split():
    energy = int(energy)
    if  energy > maximum :
        maximum = energy
    summation += energy
print(summation-maximum)