operand_first = input("Please tell me first number")
if operand_first.isdigit():
    operand_first = int(operand_first)
else: operand_first = float(operand_first)
operand_second = input("Please tell me the second number")
if operand_second.isdigit():
    operand_second = int(operand_second)
else: operand_second = float(operand_second)
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