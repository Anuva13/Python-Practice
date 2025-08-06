def main ():
    
    print(full_emails([("alex@example.com", "Alex Diego"), ("anuva@example.com", "Anuva Das")]))
       
def full_emails(people):
    result = []
    #unpacking the values of the list people into variables and name
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result   

if __name__ == "__main__":
    main()