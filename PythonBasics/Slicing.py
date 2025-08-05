def main():
    
    phonenum = '2025551212'
    format_phone(phonenum)
    
def format_phone(phonenum):
    # The first 3 digits are the area code:
    area_code = "(" + phonenum[:3] + ")"
    # The next 3 digits are called the “exchange”:
    exchange = phonenum[3:6]
    # The last 4 digits are the line number:
    line = phonenum[-4:]
    # Put the pieces back together into a nicely formatted string:
    print(area_code + " " + exchange + "-" + line)

if __name__ == "__main__":
    main()
    