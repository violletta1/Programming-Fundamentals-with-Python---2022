all_gifts = input().split(" ")
command = input()

while command != "No Money":
    command = command.split(" ")
    if command[0] == "OutOfStock":
        gift = command[1]
        for element_index in range(len(all_gifts)):
            if gift == all_gifts[element_index]:
                all_gifts[element_index] = "None"
    elif command[0] == 'Required':
        index = int(command[2])

        if len(all_gifts) > index >= 0:
            all_gifts[index] = command[1]

    elif command[0] == "JustInCase":
        all_gifts[-1] = command[1]

    command = input()
while 'None' in all_gifts:
    all_gifts.remove('None')

for element in all_gifts:
    print(element, end=' ')
