
user_value = input("Tell me something")


value_1 = ""
vowels_1 = ""
letters_2 = "aeuioyAEUIOY"
collector_letters = ""
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
        collector_letters += str(index)
        collector_letters += ","

    if element in letters_2:
        vowels_1 += element

    if element.isupper():
        value_1 = value_1 + element

if is_break == False:
    print("Job is done")

print(vowels_1, collector_letters, value_1 )