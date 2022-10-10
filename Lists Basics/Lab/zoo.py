# tail = input()
# body = input()
# head = input()
# list_person = [head, body, tail]
# print(list_person)


list_person = [input(), input(), input()]
list_person[0], list_person[2] =  list_person[2], list_person[0]
print(list_person)