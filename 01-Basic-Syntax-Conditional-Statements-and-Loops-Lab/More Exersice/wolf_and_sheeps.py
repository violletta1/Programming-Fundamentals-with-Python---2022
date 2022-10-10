animals = input().split(", ")
animals.reverse()
for index, animal in enumerate(animals):
    if animal == 'wolf' and index == 0:
        print('Please go away and stop eating my sheep')
        break
    elif animal == 'wolf':
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')