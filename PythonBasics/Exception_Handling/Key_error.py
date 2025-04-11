# KeyError
my_dict = {"a": 1}
try:
    print(my_dict["b"])  # ❌ KeyError
except KeyError:
    print("Something went wrong!")