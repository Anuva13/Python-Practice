my_list = [1, 2, 3]

try:
    print(my_list[5])  # Out of range
except Exception as e: # Generic exception
    print(f" Something went wrong. Here is the detail: {e}")
