my_list = [1, 2, 3]

try:
    print(my_list[5])  # Out of range
except IndexError:
    print("Sorry the element your trying to find doesn't exists!")
