# write a function that returns every other element from a list using enumerate()
def main():   

    print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
    
def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)
    return result    
    
if __name__ == "__main__":
    main()