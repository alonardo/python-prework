# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:22:36 2022

@author: aalon
"""

# prompt = 'If you tell us who are, we can personalize the messages you see.'
# prompt += '\nWhat is your first name? '

# name = input(prompt)
# print('\nHello, ' + name + '!')

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#   print("\nYou're tall enough to ride!")
# else:
#   print("\nYou'll be able to ride when you're a little older.")

# number = input('Enter a number, and I will tell if it is odd or even: ')
# number = int(number)

# if number % 2 == 0:
#     print('\nThe number ' + str(number) + ' is even.')
# else:
#     print('\nThe number ' + str(number) + ' is odd. ')


# guest = input('How many people are dining in tonight? ')
# guest = int(guest)

# if guest >= 8:
#     print('\nIt will be a 20 minute wait.')
# else:
#     print('\nRight this way.')

# num = input('Give me a number: ')
# num = int(num)

# if num % 10 == 0:
#     print('\nThis is a multiple of 10.')
# else:
#     print('\nNot a multiple of 10.')

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = '\nTell me something, and I will repeat it back to you: '
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = '\nPlease enter the name of a city you have visited: '
# prompt += "\nEnter 'quit' when you have finished. "

# while True:
#     city = input(prompt)
    
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + '!')

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
    
#     print(current_number)

# prompt = '\nWhat toppings would you like on your pizza?'
# prompt += "\nEnter 'stop' once you've finished. "

# while True:
#     toppings = input(prompt)
#     if toppings == 'stop':
#         break
    
#     else:
#         print("\nI'll add " + toppings + ' to your pizza.')
    

# prompt = '\nWelcome to the theater!'
# prompt += '\nHow old are you? '
# age = input(prompt)
# age = int(age)



# if age < 3:
#     print('Your ticket is free! ')
# elif age >= 3 and age < 12:
#     print('Your ticket is $10. ')
# else:
#     print('Your ticket is $15. ')

# unconfirmed_users = ['jessa', 'marcus', 'danielle']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
    
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
    
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# responses = {}

# polling_active = True

# while polling_active:
#     name = input('\nWhat is your name? ')
#     response = input('\nWhich mountain would you like to climb someday? ')
    
#     responses[name] = response
    
#     repeat = input('\nWould you like to let another person respond? (yes/no) ')
#     if repeat == 'no':
#         polling_active = False
# print('\n--- Poll Results ---')
# for name, response in responses.items():
#     print(name + ' would like to climb ' + response + '.')

# print(responses.items())

# sandwich_orders = {}
# # finished_sandwiches = 

# orders = True

# while orders:
#     name = input('\nWhat is your name? ')
#     order = input('\nWhat sandwich would you like? ')
#     sandwich_orders[name] = name
#     sandwich_orders[order] = order
    
#     complete = input('\nAnything else to eat? (yes/no)')
#     if complete == 'no':
#         orders = False
        
# print(sandwich_orders)

# while False:
#     print('My', end=' ')
#     print('Name', end=' ')
#     continue
#     print('is', end=' ')
#     break
#     print ('chika-chicka', end=' ')
#     print('Slim Shady', end=' ')

# age = 1

# while age < 10:
#     if age % 2 == 1:
#         if age == 3:
#             print('ding', end=' ')
#         elif age == 4:
#             print('dong', end=' ')
#         elif age == 5:
#             print('the', end=' ')
#         print('which', end=' ')
#     age += 1
# print('is dead', end=' ')

# num = 1
# new_num = 0

# while num < 10:
#     for i in range(3):
#         new_num += 1
#     num += 2
#     print(num, new_num)
# print(new_num)

# x = 10
# my_list = ['Yaba', 'Daba', 'Doo']
# while x < 13:
#     for remark in my_list:
#         print(remark, end=' ')
#         x += 1


# i = 6
# while i<= 10:
#     for j in range(3):
#         i*=j+2
#         print(j, end = ' ')
#         break
    







