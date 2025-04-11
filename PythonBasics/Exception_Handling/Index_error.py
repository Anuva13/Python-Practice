# IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])  # ❌ IndexError
except IndexError:
    print(f"Sorry the element your trying to find doesn't exists!")