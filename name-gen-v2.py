#module imports
import random
import time

#list
boys = ["Ajax", "Juan", "Leon", "Hubert", "Akira", "Khalif", "Rafael", "Rafi", "Arkaia", "Reegan", "Rei", "Marvel"]
girls = ["Isabel", "Kochy", "Florie", "Ayska", "Rowie", "Aqila", "Michelle"]
mix = ["Ajax", "Juan", "Leon", "Hubert", "Akira", "Khalif", "Rafael", "Rafi", "Arkaia", "Reegan", "Rei", "Marvel", "Isabel", "Kochy", "Florie", "Ayska", "Rowie", "Aqila", "Michelle"]

#generation choice
print("Welcome to Rei's Random Name Generator!")
time.sleep(1.5)
print("Made by Reinhardt Matthew Hamdani")
time.sleep(1.5)
answer = input("Please choose which list to make (case sensitive) (boys, girls, mix) ")

#generation choice boys
if answer == "boys":
    print(random.choice(boys))
    time.sleep(1.5)
    input("Press anything to continue...")

#generation choice girls
elif answer == "girls":
    print(random.choice(girls))
    time.sleep(1.5)
    input("Press anything to continue...")

#generation choice mix
elif answer == "mix":
    print(random.choice(mix))
    time.sleep(1.5)
    input("Press anything to continue...")

#invalid choice
else:
    print("Invalid choice. Restart the program.")