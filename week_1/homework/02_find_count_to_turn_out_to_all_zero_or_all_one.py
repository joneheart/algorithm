input = "11001110001011"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cot_zero = 0
    cot_one = 0
    if string[0] == '0':
        cot_one +=1
    if string[0] == '1':
        cot_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                cot_one +=1
            if string[i+1] == "1":
                cot_zero +=1


    return min(cot_one, cot_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)