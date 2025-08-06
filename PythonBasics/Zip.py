# WAP using zip() to combine a list of names and ages into a list of tuples, and print all the tuples at once.
# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip to combine the lists
combined = zip(names, ages)

# Convert the zip object to a list to print the result
print(list(combined))