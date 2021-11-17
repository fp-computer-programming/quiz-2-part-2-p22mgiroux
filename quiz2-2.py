# Author: MOG 11/17/21

import random

numbers = input("Input your three numbers seperated by a space: ")

number_list = numbers.split()

winning_numbers = random.sample(range(1,51),3)

points = 0
if int(number_list[0]) == winning_numbers[0] or int(number_list[0]) == winning_numbers[1] or int(number_list[0]) == winning_numbers[2]:
    points += 1
if int(number_list[1]) == winning_numbers[0] or int(number_list[1]) == winning_numbers[1] or int(number_list[1]) == winning_numbers[2]:
    points += 1
if int(number_list[2]) == winning_numbers[0] or int(number_list[2]) == winning_numbers[1] or int(number_list[2]) == winning_numbers[2]:
    points += 1

if points == 3:
    print("You won! 3/3 correct!")
elif points == 2:
    print("You got 2/3 correct.")
elif points == 1:
    print("You got 1/3 correct.")
else:
    print("You didnt get any correct. :(")