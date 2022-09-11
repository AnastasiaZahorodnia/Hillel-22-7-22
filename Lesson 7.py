def add(operand_a, operand_b):
    return operand_a + operand_b
result = add(7,8)
pass
#print(result)

def value( a , b , *args, **kwargs):
    if args:
        print(f"Extra position argument")
    if kwargs:
        print(f"Extra keywords arguments {type(args)=}")

    usual_sum = a + b
    print(usual_sum)
    return usual_sum + sum(args) + sum(kwargs.values())
result_add = value(1,2)
print(result_add)

def fibonacci(value):
   sequence = []
   num1, num2 = 0, 1
   for i in range(1, value + 1):
      sequence.append(i)
      num1, num2 = num2, num1 + num2
   return f"Sum: {num2}, sequence: {sequence}"


print(fibonacci(14))
print(fibonacci(17))

def fibonacci(a):
    list_value = [1,2,3,4,5]
    pass


def main_decor(func_to_decor):

    def tomato():
        print("tomato")
        func_to_decor()
        print("Inside end ")

    print("Inside finish main_decor")

    return tomato

def main_func():
    print("Inside main function")


main_func() # usual call
decorated_main_func = main_decor(main_func)
decorated_main_func()  # decorated call

