def sum(arr, accu):
    print(arr, accu)
    if len(arr) == 0 : return accu
    return sum(arr, accu + arr.pop())


new_array = [2, 9, 4, 6]
result = sum(new_array, 0)
print('result=>', result)