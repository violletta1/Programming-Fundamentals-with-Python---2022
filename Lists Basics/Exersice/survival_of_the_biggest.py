#
numbers = input().split(" ")
count_remove_num = int(input())
# print([int(x) for x in numbers])

dig_num = [int(x) for x in numbers]
# print(dig_num)

# del dig_num[0: count_remove_num]
#
# print(dig_num)

for current_remove in range(count_remove_num):
    smallest_num = min(dig_num)
    dig_num.remove(smallest_num)
#     # print(dig_num)
# print(dig_num)


string_ints = [str(num) for num in dig_num]
# Convert each integer to a string


str_of_ints = ", ".join(string_ints)
# Combine each string with a comma


print(str_of_ints)