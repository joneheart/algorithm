input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    a = 0
    for i in array:
        if i > a:
            a = i

    return a


result = find_max_num(input)
print(result)
