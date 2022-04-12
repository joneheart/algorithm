input = 20


def find_prime_list_under_number(number):
    prise_num = []
    for i in range(2, number+1):
        for j in prise_num:
            if i % j == 0 and j * j <=i:
                break
        else:
            prise_num.append(i)
            # print(prise_num)

    return prise_num


result = find_prime_list_under_number(input)
print(result)


