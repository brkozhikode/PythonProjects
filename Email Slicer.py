#strip function removes white space if any
email = input("Enter Your Email: ").strip()
#find the index of ‘@’ symbol;
symbol_index = email.index("@")
#username is from start of string to the index of @
username = email[:symbol_index]
#username is from the index of @ to the end
domain_name = email[symbol_index+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)