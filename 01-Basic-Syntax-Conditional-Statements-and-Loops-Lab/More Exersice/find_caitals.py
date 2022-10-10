
# https://www.geeksforgeeks.org/python-get-the-indices-of-uppercase-characters-in-given-string/
#
word = input()
capitals_index = [index for index in range(len(word)) if word[index].isupper()]


print(str(capitals_index))