budged = int(input())
command = input()

while command != "End":
    expenses = int(command)
    budged = budged - expenses
    if budged < 0:
        break

    command = input()


if budged < 0:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
