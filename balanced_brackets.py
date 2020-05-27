def check_balance(brackets):  # The argument is a string
    left = 0
    right = 0
    for bracket in brackets:
        if bracket == '[':
            left += 1
        elif bracket == ']':
            right += 1
    if left == right:
        return True
    else:
        return False


print(check_balance('[]'))
