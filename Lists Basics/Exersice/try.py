gifts = input().split(" ")
command = input().split()

if command[0] == 'Required':
    index = int(command[2])
    if len(gifts) > index >= 0:
        gifts[index] = command[1]
    print(gifts)

    elif command[0] == 'Required':
             index = int(command[2])

                if len(gifts) > index >= 0:
                    gifts[index] = command[1]