# result = 1 + 1
# value = 3
# print (value)
# new_variable = 13
# print (new_variable, type (new_variable))
# new_variable = "My shiny string"
# print(new_variable, type (new_variable))
# value: str = 13
# print(value)
# my_inst_value = 8
# print(id(my_inst_value))
# print(id(9))
# my_new_str = str (1)
# my_new_str = str (4.5)
#print(my_new_str)
#value_2 = int("3")
#print(value_2, type(value_2))
#number = 7 +  8.9
#print( number)

#operand_first = input("Please tell me first number")
#if (operand_first.isdigit() and operand_first == (result := int(operand_first))):
#    operand_first = int(operand_first)

#operand_second = input("Please tell me the second number")
#if (operand_second.isdigit() and operand_second == (result := int(operand_second))):
    operand_second = int(operand_second)

#operand_third = input("Please tell me action")

#if operand_third == "+":
#    result = operand_first + operand_second
#elif operand_third == "-":
#    result = operand_first - operand_second
#elif operand_first == "*":
#    result = operand_first * operand_second
#elif operand_third == "/":
#    result = operand_first / operand_second
#elif operand_third == "**":
#    result = operand_first ** operand_second
#else:
 #   result = "Error"

#print(result)
#
operand_first = input("Please tell me first number")
if operand_first:
    operand_first = int(operand_first)
else:
    operand_first = float(operand_first)
operand_second = input("Please tell me the second number")
if operand_second:
    operand_second = int(operand_second)
else:
    operand_second = float(operand_second)
operand_third = input("Please tell me action")

if operand_third == "+":
    result = operand_first + operand_second
elif operand_third == "-":
    result = operand_first - operand_second
elif operand_third == "*":
    result = operand_first * operand_second
elif operand_third == "/":
    result = operand_first / operand_second
elif operand_third == "**":
    result = operand_first ** operand_second
else:
    result = "Error"

print(result)
