def check_sum(num_list):
    for num1 in num_list:
        for num2 in num_list:
            if num1 + num2 == 0:
                return True
    
    return False

print(check_sum([5, 2, 3, 4, -2, 0]))

