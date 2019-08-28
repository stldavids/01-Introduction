#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

bee = "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible."

print("Hello, my name is Stephanie Davidson!")
user_name = input("What's your name? ")
if user_name.strip().lower() == 'barry':
    user_bee = input('Have you seen The Bee Movie? ')
    if user_bee.strip().lower() == 'yes':
        print(bee)
    else:
        print('Oh, nevermind then :-)')
print('Hello ' + user_name + '! My favorite game is Fateful Remedies, coming in 2020.')
user_game = input("What's your favorite game? ")
print("I don't think I've played " + user_game + ", but I'm sure it's fun!")
print('My main concern for the class is that I will block on something with a simple solution.')
user_yn = input("Have you ever had that problem? ")
if user_yn.strip().lower() == 'yes':
    print(':)')
else:
    print(':(')
print("I'm excited to go to Indy Comic Con with my niece.")
user_cc = input("Have you ever gone to Indy Comic Con? ")
if user_cc.strip().lower() == 'yes':
    user_ccyn = input("Isn't it fun? ")
    if user_ccyn.strip().lower() == 'yes':
        print(':)')
    else: 
        print(':(')
else:
    print("You should go sometime!")
print('My stackoverflow number is 11980682.')
print('My Github URL is https://github.com/stldavids')