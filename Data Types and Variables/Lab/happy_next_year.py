# year = int(input())
# happy_year = False
#
# while not happy_year:
#     year += 1
#     set_year = set()
#     for i in range(len(str(year))):
#         set_year.add(str(year)[i])
#
#     happy_year = len(set_year) == len(str(year))
# print(year)

#
# from itertools import permutations
#
# number = tuple(map(int, input()))
# myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
#
# for digits in list(myperm):
#     if digits > number:
#         result = ''.join(str(x) for x in digits)
#         print(result)
#         break

year = int(input())
year_is_happy = False
# Counter of the indexes in year_as_string(year is made as string below)
counter = 0
# Counter: Now many times the digit is NOT included in the year's digits
counter_digits = 0
while not year_is_happy:
    # Go to nex year
    year += 1
    # Make the input year as string
    year_as_string = str(year)
    # Check for equal digits in the year's digits by checking the indexes in the year_as_string
    for digit in year_as_string:
        new_year = (year_as_string[(counter + 1):])
        # If equals digits => brake loop
        if digit in new_year:
            counter = 0
            break
        else:
            # If the digit is not in the year's digits, counter_digits += 1
            counter_digits += 1
        counter += 1
    # If the number of NOT equals digits is as the length of the string year_as_string => The year is HAPPY!
    if counter_digits == len(year_as_string):
        year_is_happy = True
        break
    else:
        # If the yars is NOT happy. Every counter is = 0
        counter_digits = 0

# Finally we have a HAPPY year. Let's print it!
print(year)