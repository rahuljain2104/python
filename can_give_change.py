def can_give_change(arr):
    reserve = 0
    for i, note in enumerate(arr):
        if note == 5:
            reserve += 5
            continue
        else:
            reserve -= (note-5)
        if reserve < 0:
            return i+1
    return 0

print(can_give_change([5,20]))