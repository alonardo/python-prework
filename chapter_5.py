# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:42:45 2022

@author: aalon
"""

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
for topping in requested_toppings:
    if topping in requested_toppings:
        print('True')
    else:
        print('False')

banned_users = ['Diana', 'Melanie', 'Trump']
user = 'Diana'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')
 
vegan_foods =['bread', 'vegetables', 'fruit']
selection = 'fruit'
if selection not in vegan_foods:
    print("I can't eat that. Not vegan.")
if selection in vegan_foods:
    print("Thank you, i'll eat that vegan food.")

age = 69
if age < 5:
    price = 5
elif age < 18:
    price = 10
elif age < 65:
    price = 15
else:
    price = 1
print('Cost of admission will be ' + str(price) + '.')
    

year = 26
if year < 1:
    print('You are a newborn')
elif year <12:
    print('You are a child')
elif year <18:
    print('You are a teenager')
elif year <25:
    print('You are technically an adult')
else:
    print('You are old as shit')

drink_order = ['coffee', 'half and half', 'vanilla']
for drink in drink_order:
    if drink == 'vanilla':
        print('Sorry, we are out of vanilla')
    else:
        print('Enjoy your ' + drink + '.')
print('')

requested_toppings = ['cheese', 'pepperoni', 'bbq chicken', 'pineapple', 'peppers']
available_toppings = ['pepperoni', 'bbq chicken', 'pineapple']

for request in requested_toppings:
    if request in available_toppings:
        print('We have ' + request + '.')
    else:
        print("Sorry, we don't have any " + request + ".")
 
    
 
not_welcome = ['diana', 'melanie']
guests = ['jeff', 'josue', 'derek']
vip = ['jed', 'clare', 'coral']
everyone = ['jed', 'clare', 'coral', 'jeff', 'josue', 'derek',
       'diana', 'melanie']

for guest in everyone:
    if guest in not_welcome:
        print("You aren't welcome. Please go home.")
    elif guest in guests:
        print('Please take a set over there.')
    elif guest in vip:
        print('Let me take you jacket. Would you like champagne or wine today?')
print('')

nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print(str(num) +'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')

# I could start writing a weight loss calculator
# Cuurent weight and target weight
# Amount of time to lose
# Age
# Activity level
# Basal metabolic rate
# hmmmmmmm

number = 8
if number <= 8:
    print('Number is greater than 8')
else:
    print('number is less than 8')

name = "Destiny's Child"
if name == "Destiny's Child":
    print("Say my name, say my name", end=" ")
print("If no one is around you", end=" ")
if name:
    print("Say baby I love you", end=" ")
else:
    print("If you ain't runnin' game", end =" ")

x = 5
y = 10
i = '5'
j = '10'
if x == i and x != y:
    print("Blackbird", end=" ")
else:
    print("singing", end=" ")
print("in the", end=" ")
if x < int(j) or i ==j:
    print("dead", end=" ")
else:
    print("of night", end=" ")
print('')

x = 5
print('A spoon', end=' ')
if x == 4 or x ==5:
    print('full of', end=' ')
elif x>=4:
    print('sugar', end=' ')
else:
    print('helps the medicine', end=' ')
print('go down', end=' ')
print('')






    



















