# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# ⦁	One with all the positives (including 0) numbers
# ⦁	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"


num_lines = int(input())
positive = []
negative = []
count_positive = 0
sum_negative = 0

for i in range(1, num_lines + 1):
    current_num = int(input())
    if current_num > 0:
        count_positive += 1
        positive.append(current_num)

    else:
        sum_negative += current_num
        negative.append(current_num)

print(positive)
print(negative)

print(f"Count of positives: {len(positive)}")
# print(f"Count of positives: {count_positive}")
print(f" Sum of negatives: {sum(negative)}")
# print(f" Sum of negatives: {sum_negative}")

