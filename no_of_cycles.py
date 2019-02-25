def number_of_cycles(arr):
    count = 0
    exclude_index = []
    temp = []
    for i in range(len(arr)):
        if i in exclude_index:
            continue
        new_index = arr[i]
        for j in range(len(arr)):
            temp.append(new_index)
            # print('arr['+str(new_index)+']')
            if arr[new_index] == arr[i] and j == i:
                count += 1
                break
            new_index = arr[new_index]
        else:
            temp = []
        exclude_index.extend(temp)
    return count


print(number_of_cycles([1,0,2]))