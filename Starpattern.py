def print_star_like_object(size):
    if size % 2 == 0:
        print("Size must be an odd number for a symmetrical star-like object.")
        return
    
    center = size // 2
    
    for i in range(size):
        for j in range(size):
            if i == center or j == center or i == j or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Set the size for the star-like object
size = 7
print_star_like_object(size)