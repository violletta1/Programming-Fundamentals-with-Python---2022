# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers,
# which are multiples of the given factor. The numbers should be only positive,
# and they should be arranged in ascending order, starting from the value of the factor.

# factor = int(input())
# count = int(input())
# list_of_numbers = []
# for multiplier in range(1, count + 1):
#     list_of_numbers.append(factor * multiplier)
# print(list_of_numbers)

factor = int(input())
count = int(input())
my_list = []
for num in range(1, count + 1):
    calculation = num * factor
    my_list.append(calculation)
print(my_list)
#
# n = int(input())
# word = input()
# my_list = []
# for _ in range(n):
#     current_word = input()
#     my_list.append(current_word)
# print(my_list)
#
# for i in range(len(my_list) - 1, -1, -1):
#     element = my_list[i]
#     if word not in element:
#         my_list.remove(element)
# print(my_list)