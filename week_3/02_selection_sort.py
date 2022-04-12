input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min = i
        for j in range(n-i):
            if array[i+j]<array[min]:
                min = i+j
        array[i] , array[min] = array[min], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


