# Author: MOG 11/17/21

day = input("What day is it today (A-G)? ")

if day == "a" or day == "A":
    print("You have class today because it is A day.")
elif day == "b" or day == "B":
    print("You do not have class today because it is B day.")
elif day == "c" or day == "C":
    print("You have class today because it is C day.")
elif day == "d" or day == "D":
    print("You do not have class today because it is D day.")
elif day == "e" or day == "E":
    print("You have class today because it is E day.")
elif day == "f" or day == "F":
    print("You do not have class today because it is F day.")
elif day == "g" or day == "G":
    print("You do not have class today because it is G day.")
else:
    print("Please input a day, A-G.")