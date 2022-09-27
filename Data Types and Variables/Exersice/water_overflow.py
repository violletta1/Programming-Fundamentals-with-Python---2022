#
# You have a water tank with a capacity of 255 liters. On the first line,
# you will receive n – the number of lines, which will follow.
# On the following n lines,you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.

# number_of_lines = int(input())
# tank_capacity = 255
# water_counter = 0
# for current_line in range(number_of_lines):
#     liters_of_water = int(input())
#     if tank_capacity - liters_of_water < 0:
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= liters_of_water
#     water_counter += liters_of_water
# print(water_counter)


times_added_water = int(input())
water_tank_capacity = 255
added = 0

for line in range(1, times_added_water + 1):
    litter_water = int(input())
    if water_tank_capacity - litter_water < 0:
        print("Insufficient capacity!")
        continue
    water_tank_capacity -= litter_water
    added += litter_water
print(added)
