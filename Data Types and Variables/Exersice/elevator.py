# import math
#
# num_people = int(input())
# capacity = int(input())
#
#
# course = math.ceil(num_people / capacity)
# print(course)

num_people = int(input())
capacity = int(input())

course2 = num_people // capacity

course = num_people % capacity

if course > 0:
    course2 += 1

print(course2)