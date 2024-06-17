import sys

def collatz(number):
    if (number % 2 == 0):
        number = number // 2
        print(number)
    else:
        number = 3 * number + 1
        print(number)
    return number

print("Enter Number:\n")
try: 
    num = int(input())
    while (num != 1):
        num = collatz(num)
except ValueError:
    print("Not a number")
    sys.exit();



