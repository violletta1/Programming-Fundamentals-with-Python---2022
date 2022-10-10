# gifts = input().split(' ')
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money#
#
#
# list of items
#list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
# Will print the index of 'bat' in list2
#print(list2.index('bat'))#
#
# command = input().split(' ')
# while command[0] != 'No' and command[1] != 'Money':
#     index = 0
#     if command[0] == 'OutOfStock':
#         gift = command[1]
#
#         while gift in gifts:
#             index = gifts.index(gift)
#             gifts[index] = 'None'
#
#     elif command[0] == 'Required':
#          index = int(command[2])
#
#             if len(gifts) > index >= 0:
#                 gifts[index] = command[1]
#
#
#
#     elif command[0] == 'JustInCase':
#         gifts[-1] = command[1]
#
#     command = input().split(' ')
#
# while 'None' in gifts:
#     gifts.remove('None')
#
# for element in gifts:
#     print(element, end=' ')
#
#     gifts = input().split()
#     command = input()
#
#     while not command == "No Money":
#         command = command.split()
#         if "OutOfStock" in command:
#             for i in range(len(gifts)):
#                 if command[1] in gifts[i]:
#                     gifts[i] = "None"
#         elif "Required" in command:
#             for i in range(len(gifts)):
#                 if i == int(command[2]):
#                     gifts[i] = command[1]
#         elif "JustInCase" in command:
#             gifts[-1] = command[1]
#         command = input()
#     while "None" in gifts:
#         gifts.remove("None")
#     for i in gifts:
#         print(i, end=" ")
#
# gifts = input().split()
# command = input()
#
# while not command == "No Money":
#     command = command.split()
#     if "OutOfStock" in command:
#         for i in range(len(gifts)):
#             if command[1] in gifts[i]:
#                 gifts[i] = "None"
#     elif "Required" in command:
#         for i in range(len(gifts)):
#             if i == int(command[2]):
#                 gifts[i] = command[1]
#     elif "JustInCase" in command:
#         gifts[-1] = command[1]
#     command = input()
# while "None" in gifts:
#     gifts.remove("None")
# for i in gifts:
#     print(i, end=" ")
        ###
        #
        #

        #
        #     elif "Required" in command:
        #         for gift_per_person in range(len(gifts_for_family)):
        #             if gift_per_person == int(command[2]):
        #                 gifts_for_family[gift_per_person] = command[1]
        #     elif "JustInCase" in command:
        #         gifts_for_family[-1] = command[1]
        #     command = input()
        # while "None" in gifts_for_family:
        #     gifts_for_family.remove("None")
        # for gift_per_person in gifts_for_family:
        #     print(gift_per_person, end=" ")

gift_names = input()
gift_names_list = gift_names.split()
is_no_money = False
command = input()
command_list = command.split()

while not is_no_money:
    if command_list[0] == 'OutOfStock':
        gift = command_list[1]
        for index, current_gift in enumerate(gift_names_list):
            if current_gift == gift:
                gift_names_list[index] = 'None'
#
# while not command == "NO MONEY":
#     command.split()
#     if command[0] == "out":
#         gift = command[1]
#         for index, element in enumerate(gift_names_list):
#             if element == gift:
#                 gift_names_list[index] = "Non"




    if command_list[0] == 'Required' and 0 <= int(command_list[2]) < len(gift_names_list):
        gift = command_list[1]
        gift_names_list[int(command_list[2])] = gift

    if command_list[0] == 'JustInCase':
        gift = command_list[1]
        gift_names_list[-1] = gift

    command = input()
    command_list = command.split()

    if command == 'No Money':
        is_no_money = True
        while 'None' in gift_names_list:
            gift_names_list.remove('None')
        break

print(' '.join(gift_names_list))