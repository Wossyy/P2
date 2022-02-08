# 1. Dice roll
import random


def dice_roll():
    return random.randint(1, 6)


print("Your roll is: ")
print(dice_roll())


# 2. Joke teller
def joke():
    print("\nLet me tell you a joke!")
    jokes = ["What does a panda cook bamboo in? A pan, duh.",
             "Knock knock, who's there? Boo, Boo who? Why are you crying?",
             "How does Darth Vader like his toast? On the dark side."]
    randojoke = random.choice(jokes)
    return randojoke


print(joke())

# 3. current date
from datetime import date


def date_today():
    print("\nThe date for today is:")
    return date.today()


print(date_today())


# 4. Even or Odd
def eo(x):
    if x % 2 == 0:
        print("Your number is even!\n")
    else:
        print("Your number is odd!\n")


eo(int(input("\nPlease enter your number: ")))


# 5. Max of 3 numbers


def max(x, y, z):
    nums = [x, y, z]
    nums.sort()
    print(nums[-1])


max(input("Please enter your first number: "),
    input("Please enter your second number: "),
    input("Please enter your third number: "))


# alt 6. list sum
# def list_sum():
#     nums = [1, 2, 3]
#     print(sum(nums))
#
#
# list_sum()


# 6. List sum
def list_sum(list):
    sum = 0
    for nums in list:
        sum = nums + sum
    return sum


list = [1, 2, 3]
print(list_sum(list))


# 7. In range
def in_range(max):
    if max >= num:
        return True
    else:
        return False


max = int(input("Please enter a max number: "))
num = int(input("Please enter your number: "))
print(in_range(max))


# 8. Find evens
def find_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens


print(find_evens([1, 2, 3, 4]))


# 9. Greeting
def greet_me(name):
    if greeting == "y":
        greetings = ["What's up ", "Howdy ", "How are you? "]
        final = random.choice(greetings)
        return final + name
    elif greeting == "n":
        return "Hello " + name


name = input("Please enter your name: ")
greeting = input("Do you want a special greeting? Please enter y/n: ")
print(greet_me(name))


# 10. simple calculator
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2


print("Welcome to this calculator program!\nEnter + to add\nEnter - to subtract\nEnter / to divide\nEnter * to multiply")
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
operation = input("Please enter the operation you want to preform: ")
print(calculator(num1, num2, operation))
