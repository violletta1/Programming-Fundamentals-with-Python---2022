string_of_beaches = input().lower()

beaches = ["Sand", "Water", "Fish", "Sun"]
beaches_lower = [beach.lower() for beach in beaches]
number_of_beaches = 0


for item in beaches_lower:
    if item in string_of_beaches:
        number_of_beaches += 1

print(number_of_beaches)