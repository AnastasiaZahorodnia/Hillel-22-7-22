#while True:
user_value = input("Tell me something")

value_1 = ""
for letter in user_value:
    if letter.isupper() == True:
        value_1 = value_1 + letter
print(value_1)

collector_letters = ""
for index, element in enumerate(user_value):
    if element == " ":
        collector_letters += str(index)
print(collector_letters)

vowels_1 = ""
letters_2 = "aeuioyAEUIOY"
for vowels_letters in user_value:
    if vowels_letters in letters_2:
        vowels_1 += vowels_letters
print(vowels_1)



counter = 0

for letter_3 in user_value:
    counter += 1

    if counter == 3:
        print("counter achieved")
        break
    else:
        print("counter did not achieve")

print("loop is finished")
