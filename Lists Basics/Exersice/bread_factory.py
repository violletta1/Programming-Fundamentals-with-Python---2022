events = input().split("|")
# rest-2|order-10|eggs-100|rest-10
# rest-2 order-10 eggs-100 rest-10
total_coins = 100
total_energy = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    # rest 2  order 10  eggs  100 rest  10
    # rest 2
    type_of_event = event_items[0]
    # rest   order   eggs   rest
    # rest
    event_value = int(event_items[1])
    #  2   10   100  10
    #  int ot str "2"
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_open = False
            break
if factory_is_open:  # if factory_is_open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")