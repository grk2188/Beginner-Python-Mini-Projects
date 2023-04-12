

def main():
    print("Welcome to the email slicer program \n")

    email_input = input("Enter the email address: ")

    (username, domain) = email_input.split("@")
    (domain, extenstion) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extenstion)

main()

