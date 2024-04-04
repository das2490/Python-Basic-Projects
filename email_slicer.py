def Email_slicer():
    email = input("Enter Your Email: ").strip()
    username = email[:email.index('@')]
    domain = email[email.index('@')+1:]
    result = (f"Your User name is '{username}' and domain is '{domain}'")
    return result
