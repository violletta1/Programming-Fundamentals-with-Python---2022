name = input()


valdemort_found = False
while name != "Welcome!":
    if name != "Voldemort":
        num_char = len(name)
        if num_char < 5:
            print(f"{name} goes to Gryffindor.")
        elif num_char == 5:
            print(f"{name} goes to Slytherin.")
        elif num_char == 6:
            print(f"{name} goes to Ravenclaw.")
        elif num_char > 6:
            print(f"{name} goes to Hufflepuff.")

    else:
        valdemort_found = True
        print("You must not speak of that name!")
        break

    name = input()

if not valdemort_found:
    print("Welcome to Hogwarts.")