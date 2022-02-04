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


def list_sum(list):
    sum = 0
    for nums in list:
        sum = nums + sum
        return sum


list = [1, 2, 3]
print(list_sum(list))
