input = "abacabade"


def find_not_repeating_character(string):
    alphabet_array = [0] * 26
    for i in string:
        if not i.encode().isalpha():
            continue
        arr_index = ord(i) - ord("a")
        alphabet_array[arr_index] += 1

    not_repeating_array = []
    for index in range(len(alphabet_array)):
        alphabet_occurrence = alphabet_array[index]

        if alphabet_occurrence == 1:
            not_repeating_array.append(chr(index + ord("a")))

    for i in string:
        if i in not_repeating_array:
            return i

    return "_"


result = find_not_repeating_character(input)
print(result)