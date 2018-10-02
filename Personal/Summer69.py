def summer_69(arr):
    result = 0
    for i in range(0, len(arr)):
        if arr[i] == 6 or arr[i] == 7 or arr[i] == 8 or arr[i] == 9:
            continue
        result += arr[i]
    return result


print(summer_69([2, 1, 6, 9, 11]))
