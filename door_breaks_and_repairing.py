# You are policeman and you are playing a game with Slavik. The game is turn-based and each turn consists of two phases. During the first phase you make your move and during the second phase Slavik makes his move.
#
# There are n doors, the i-th door initially has durability equal to ai.
#
# During your move you can try to break one of the doors. If you choose door i and its current durability is bi then you reduce its durability to max(0,bi−x) (the value x is given).
#
# During Slavik's move he tries to repair one of the doors. If he chooses door i and its current durability is bi then he increases its durability to bi+y (the value y is given). Slavik cannot repair doors with current durability equal to 0.
#
# The game lasts 10100 turns. If some player cannot make his move then he has to skip it.
#
# Your goal is to maximize the number of doors with durability equal to 0 at the end of the game. You can assume that Slavik wants to minimize the number of such doors. What is the number of such doors in the end if you both play optimally?
#
# Input
# The first line of the input contains three integers n, x and y (1≤n≤100, 1≤x,y≤105) — the number of doors, value x and value y, respectively.
#
# The second line of the input contains n integers a1,a2,…,an (1≤ai≤105), where ai is the initial durability of the i-th door.
#
# Output
# Print one integer — the number of doors with durability equal to 0 at the end of the game, if you and Slavik both play optimally.

meta = [int(item) for item in input().split()]  # n, x, y
doors = [int(item) for item in input().split()]

if meta[1] > meta[2]:
    print(meta[0])

if meta[1] <= meta[2]:
    count = 0
    for door in doors:
        if door <= meta[1] :
            count += 1
    print(int(count/2) + 1)
