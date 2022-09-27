
number = int(input())

for i in range(1, number + 1):
    first_digit = 0
    last_digit = 0
    sum_of_digits = 0
    if i < 10:
        first_digit += i
        sum_of_digits += i
        if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
            print(f'{sum_of_digits} -> True')
        else:
            print(f'{sum_of_digits} -> False')
    else:
        first_digit += i // 10
        last_digit += i % 10
        sum_of_digits = first_digit + last_digit
        if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')