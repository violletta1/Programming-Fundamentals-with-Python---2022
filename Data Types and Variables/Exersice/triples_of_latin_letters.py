number_of_char = int(input())

for first_char in range(number_of_char):
    for second_char in range(number_of_char):
        for third_char in range(number_of_char):
            print(f"{chr(97 + first_char)}{chr(97 + second_char)}{chr(97 + third_char)}")