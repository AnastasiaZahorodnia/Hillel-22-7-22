
user_value = input("Tell me something")


add_capital_letters = ""
add_vowels = ""
vowels_letters = "aeuioyAEUIOY"
index_number = ""
counter = 0
is_break = False

for index, element in enumerate(user_value):

    if element.isdigit():
        counter = counter + 1
    else:
        counter = 0

    if counter == 3:
        print("counter achieved")
        is_break = True
        break

    if element == " ":
        index_number = index_number + str(index) + ","

    if element in vowels_letters:
        add_vowels += element

    if element.isupper():
        add_capital_letters += element

if is_break == False:
    print("Job is done")

print(add_vowels, index_number)
print(add_capital_letters)