def main():
    
    #multiple_WO()
    #multiple_W()
    #newlist()
    multiple_3()    
"""
def multiple_WO():
    multiples = []
    for x in range(1,11):
        multiples.append(7*x)
    print(multiples)
    
def multiple_W():
    multiples = [x*7 for x in range(1,11)]
    print(multiples)
    
def newlist():
    languages = ['Ruby', 'Go,', 'Python', 'Java', 'C', 'Perl']
    length_language = [len(language) for language in languages]
    print(length_language)   
""" 
def multiple_3():
    z = [x for x in range(0,101) if x%3==0]
    print(z)
  
if __name__ == "__main__":
    main()