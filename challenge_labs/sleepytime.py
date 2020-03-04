#!/usr/bin/env python3

def toddler():
    diaper = input("Is the diaper wet? (Y or N)")
    if diaper == "Y":
        print("Change Diaper")
    elif diaper == "N":
        print("Give milk")
    else:
        print("You should have answered Y or N")

def teen():
    wakestate = input("Is the kid sleep walking (Y or N)")
    if wakestate == "Y":
        print("Walk back to bed")
    elif wakestate =="N":
        print("Ask why they decided it was a good idea to drink a monster?")
    else:
        print("You should have answered Y or N")

while True:
    try:
        age = int(input("Please Enter your child's age: "))
        break
    except ValueError:
        print("seriosly bro, maybe try a whole number")
if age >=0 and age <= 4:
    print("I see you have a todler, god bless")
    toddler()
elif age >= 5 and age <= 17:
    print("Well here you go")
    teen()
elif age > 18:
    print("Child out of range. Move out")
else:
    print("Try a positive number")
