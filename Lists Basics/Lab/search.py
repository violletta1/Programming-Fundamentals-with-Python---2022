num_of_searches = int(input())
searched_word = input()

list_of_all_strings = []
strings_included_searched_word = []

for i in range(num_of_searches):
    current_string = input()
    list_of_all_strings.append(current_string)
    if searched_word in current_string:
        strings_included_searched_word.append(current_string)


print(list_of_all_strings)
print(strings_included_searched_word)
