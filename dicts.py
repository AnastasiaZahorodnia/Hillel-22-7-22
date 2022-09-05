ascii_table = {i:chr(i) for i in range(0,128)}

value_user = input("Write here what you want ")
user_password = int(input("Password: "))
#string = (chr(ord(value_user)+user_password))

#result = ''.join(chr(ord(letter) + user_password) for letter in
#value_user)
#print(result)
import string

encoded = {l: string.ascii_lowercase[(index + user_password) % 26] for index, l in enumerate(string.ascii_lowercase)}
result = ''.join(encoded[letter] for letter in value_user)
print(result)

