# problem statement
# There are n students in a university. The number of students is even. The i-th student has programming skill equal to ai.
#
# The coach wants to form n2 teams. Each team should consist of exactly two students, and each student should belong to exactly one team. Two students can form a team only if their skills are equal (otherwise they cannot understand each other and cannot form a team).
#
# Students can solve problems to increase their skill. One solved problem increases the skill by one.
#
# The coach wants to know the minimum total number of problems students should solve to form exactly n2 teams (i.e. each pair of students should form a team). Your task is to find this number.
#
# Input
# The first line of the input contains one integer n (2≤n≤100) — the number of students. It is guaranteed that n is even.
#
# The second line of the input contains n integers a1,a2,…,an (1≤ai≤100), where ai is the skill of the i-th student.
#
# Output
# Print one number — the minimum total number of problems students should solve to form exactly n2 teams.
# code below

N=int(input())
strength = [int(i) for i in input().split()]
strength = sorted(strength)
sum = 0
for i in range(0,N,2):
    sum += abs(strength[i]-strength[i+1])
print(sum)
m,n = [int(i) for i in input().split()]
for i in range(n):
    tmp = input()
if m < 8 or n < 8:
    print(0)
print((m-7)*(n-7))