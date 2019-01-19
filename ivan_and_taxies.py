# Andrew prefers taxi to other means of transport, but recently most taxi drivers have been acting inappropriately. In order to earn more money, taxi drivers started to drive in circles. Roads in Andrew's city are one-way, and people are not necessary able to travel from one part to another, but it pales in comparison to insidious taxi drivers.
#
# The mayor of the city decided to change the direction of certain roads so that the taxi drivers wouldn't be able to increase the cost of the trip endlessly. More formally, if the taxi driver is on a certain crossroads, they wouldn't be able to reach it again if he performs a nonzero trip.
#
# Traffic controllers are needed in order to change the direction the road goes. For every road it is known how many traffic controllers are needed to change the direction of the road to the opposite one. It is allowed to change the directions of roads one by one, meaning that each traffic controller can participate in reversing two or more roads.
#
# You need to calculate the minimum number of traffic controllers that you need to hire to perform the task and the list of the roads that need to be reversed.
#
# Input
# The first line contains two integers n and m (2≤n≤100000, 1≤m≤100000) — the number of crossroads and the number of roads in the city, respectively.
#
# Each of the following m lines contain three integers ui, vi and ci (1≤ui,vi≤n, 1≤ci≤109, ui≠vi) — the crossroads the road starts at, the crossroads the road ends at and the number of traffic controllers required to reverse this road.
#
# Output
# In the first line output two integers the minimal amount of traffic controllers required to complete the task and amount of roads k which should be reversed. k should not be minimized.
#
# In the next line output k integers separated by spaces — numbers of roads, the directions of which should be reversed. The roads are numerated from 1 in the order they are written in the input. If there are many solutions, print any of them.


from collections import deque
N,M=map(int,input().split())
table=[]
#ma=-1
for i in range(M):
    s,t,c=map(int,input().split())
    s,t=s-1,t-1
    table.append((s,t,c))
    #ma=max(c,ma)

def check(k):
    Lin=[0]*N
    edge=[[] for i in range(N)]
    for s,t,c in table:
        if c>k:
            Lin[t]+=1
            edge[s].append(t)
    Haco=deque()
    ans=[]
    for i in range(N):
        if Lin[i]==0:
            ans.append(i)
            Haco.append(i)
    while Haco:
        x = Haco.pop()
        for y in edge[x]:
            Lin[y]-=1
            if Lin[y]==0:
                ans.append(y)
                Haco.append(y)
    return ans
ma=10**9+7
mi=-1
while ma-mi>1:
    mid=(ma+mi)//2
    if len(check(mid))==N:
        ma=mid
    else:
        mi=mid
ans=check(ma)
#print(ma)
#print(ans)
#print(table)
dd={}
for i in ans:
    dd[ans[i]]=i
num=0
answer=[]
#print(dd)
for i in range(M):
    s, t, c=table[i]
    if dd[s]>dd[t] and c<=ma:
        answer.append(i+1)
        num+=1
print(ma,num)
print(' '.join(map(str,answer)))