username = input("Please tell me your name")
print(username)
username_update = str.strip(username)
print(username_update)
print("Hello --> ", username_update.capitalize())
print("length of string", len(username_update))
print("reversed--> ", username_update[::-1])