
#
# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# ⦁	even
# ⦁	odd
# ⦁	negative
# ⦁	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.


num_checks = int(input())
even = []
odd = []
negative = []
positive = []


for i in range(num_checks):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
        if current_num % 2 == 0:
            even.append(current_num)
        else:
            odd.append(current_num)
    elif current_num < 0:
        negative.append(current_num)
        if current_num % 2 == 0:
            even.append(current_num)
        else:
            odd.append(current_num)


category = input()
if category == "even":
    print(even)
elif category == "odd":
    print(odd)
elif category == "negative":
    print(negative)
elif category == "positive":
    print(positive)