input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    num_sum = 0
    for i in array:
        if i <= 1 or num_sum <= 1:
            num_sum += i
        else:
            num_sum *= i
    return num_sum

result = find_max_plus_or_multiply(input)
print(result)