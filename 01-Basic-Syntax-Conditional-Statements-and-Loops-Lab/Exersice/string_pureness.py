num_strings = int(input())

for i in range(1, num_strings + 1):
    string = input()

    if string.__contains__('.') or string.__contains__("_") or string.__contains__(","):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
