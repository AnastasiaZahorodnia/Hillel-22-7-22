compare_1 = 3 != 5
print(compare_1, type(compare_1))
compare_2 = 3 < 5
print(compare_2)

match_1 = 5 == 5
print(match_1)
match_2 = 5 >= 5
print(match_2)
match_3 = 5 <= 5
print(match_3, type(match_3))

true_01 = (True and True) or False
print(true_01, type(true_01))
true_02 = True or (True and False)
print(true_02, type(true_02))
true_03 = True and (True or False)
print(true_03)
true_04 = True or True or False
print(true_04)
true_05 = True and True and not False
print(true_05)

number_1 = None == 7
print(number_1)
number_2 = "" == 10-1
print(number_2)