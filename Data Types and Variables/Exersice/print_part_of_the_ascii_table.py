first_ord_ascii = int(input())
last_ord_ascii = int(input())

for i in range(first_ord_ascii, last_ord_ascii + 1):
    char = chr(i)
    print(char, end=" ")


