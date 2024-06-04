# WAP to merge two dictionaries
def main():
    Dict_1 = {"Student_1":"Anuva","Student_2":"Shreya","Student_3":"Shilpa","Student_4":"Neha"}
    Dict_2 = {"Student_5":"Subhashish","Student_6":"Prakash"}
    Dict_3 = Dict_1 | Dict_2
    print(Dict_3)

if __name__ == "__main__":
    main()