#1
def addall (start, stop):
    add = 0
    if start > stop:
        update_start = stop
        stop = start
    for i in range(update_start, stop):
        add += i
    if start < stop:
        for i in range(start, stop):
            add += i
    return add + stop
print(addall(4,0))

#2

def time(sec):
    if sec >= 86400:
        days = sec // (60 * 60 * 24)
        print(f"The number of days is {days}")
    if sec >= 3600:
        hours = sec % (60 * 60 * 24) // (60*60)
        print(f"The number of hours is {hours}")
    if sec >= 60:
        minutes = sec % (60*60*24) % (60*60) // 60
        print(f"The number of minutes is {minutes}")
    if sec >= 1:
        seconds = sec % (60*60*24) % (60*60) % 60
        print(f"The number of seconds is {seconds}")
    return None
print(time(100000))

#3
def sum(numbers):
    counter = 0
    for i in numbers:
        if isinstance(i, int):
            counter += i

    return counter
print(sum([3,4]))

def summa(a):
    counter = 0
    while counter == 0:
        counter += a
    return counter
a = [2,3]
total = sum(a)
print(summa(total))

def recursive(a):
    if a == 0:
        return 5
    else:
        return a * recursive(a - 1)
a = [3,2]
total_1 = sum(a)
print(recursive(total_1))

# 4
def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(8))

# 5
def main_decor(decor):
    def tomato():
        print("tomato")

    def meat():
        print("meat")

    def cheese():
        print("cheese")

    def bread():
        print("bread")

    return tomato(), meat(), cheese(), bread()

def main_func():
    print("Inside main function")
main_decor(main_func())