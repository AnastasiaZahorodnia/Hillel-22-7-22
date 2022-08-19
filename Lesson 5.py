user_value = input("Lets go")

value_1 = ""
collector_letters = ""
vowels_1 = ""
counter = 0

for index, letter in enumerate(user_value):
    if letter.isupper():
        value_1 = value_1 + letter

    if letter == " ":
        collector_letters += str(index)

    if letter in "aeuioyAEUIOY":
        vowels_1 += letter

    if letter.isdigit():
        counter = counter + 1
        if counter == 3:
            print("counter achieved")
            break
        else:
            counter = 0
            print("counter did not achieve")

print("loop is finished")

print()
print(value_1)
print(collector_letters)
print(vowels_1)