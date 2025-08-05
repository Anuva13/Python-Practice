def main():
    # List of emails
    emails = [
        "alice@example.com",
        "bob@example.com",
        "charlie@otherdomain.com",
        "dave@example.com"]
    
    old_domain = "@example.com"
    new_domain = "@newdomain.com"
       
    updated_emails = [replace_email_domain(email, old_domain, new_domain) for email in emails]

    for email in updated_emails:
        print(email)
    
def replace_email_domain(email, old_domain, new_domain):
    if old_domain in email:
        return email.replace(old_domain, new_domain)
    return email
        
if __name__ == "__main__":
    main()

