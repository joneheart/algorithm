def is_correct_parenthesis(string):
    cot_right = 0
    cot_left = 0
    for i in string:
        if i == '(':
            cot_right += 1
        if i == ')':
            cot_left += 1
    if cot_left == cot_right:
        return True
    else:
        return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))