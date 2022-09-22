command = input()

while command != "End":
    if command != "SoftUni":
        word = ""
        for letter in command:
            word = word + (letter * 2)

        print(f"{word}")
    command = input()
