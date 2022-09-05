data_inf_user1 = set(input("Write here whatever you want "))
data_inf_user2 = set(input("Write here whatever you want "))

alpha_data = set()
not_same_numbers1 = set()
not_same_numbers2 = set()

for i in data_inf_user1.intersection(data_inf_user2):
    if i.isalpha():
        alpha_data.add(i)
    elif i.isdigit():
        not_same_numbers1.add(i)

print(f"True = {alpha_data}")
print(not_same_numbers1.symmetric_difference(not_same_numbers2))

#examples with |=, &=, -=, ^=

set_1 = {"a", "b", "c", "d", "e"}
set_2 = {"c", "d", "f", "d", "s"}
set_3 = {"d", "r", "t", "d", "a", "p"}

print(set_1 - set_2 - set_3)

print(set_1 | set_2 | set_3)

print(set_1 & set_2 & set_3)

print(set_1 ^ set_2 ^ set_3)