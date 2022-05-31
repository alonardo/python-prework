# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:13:03 2022

@author: aalon
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1].title())

message = 'My first bicycle was a ' + bicycles[2].title() + '.'
print(message)

friends = ['Ed', 'Dane', 'Scott', 'Danny', 'Jeff']
print(friends[0])
greeting = 'Hello ' + friends[0] + '!'
print(greeting)

transportation = ['Car', 'Motorcycle', 'Plane', 'Jetpack']
statement = 'I want to go to Washington using a ' + transportation[-1] + '!'
print(statement)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

bikes =[]
bikes.append('honda')
bikes.append('yamaha')
bikes.append('suzuki')
print(bikes)

bikes.insert(0, 'ducati')
print(bikes)

del bikes[0]
print(bikes)
print('')


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)
print('The last bike I owned was a ' + last_owned + '.')

motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

print('\nHello ' + friends[0] + '! Will you come hang out with me?')

unable = 'Ed'
friends.remove(unable)
print(friends)

friends.insert(0, 'Jessa')
print(friends)

friends.insert(0, 'Marcus')
friends.insert(2, 'Danielle')
friends.append('Dad')
print(friends)

dad = friends.pop()
print(friends)
print('Sorry, ' + dad + ' you cannot join.')

jeff = friends.pop()
print(friends)
print('Sorry, ' + jeff + ' you cannot join.')

danny = friends.pop()
print(friends)
print('Sorry, ' + danny + ' you cannot join.')

scott = friends.pop()
print(friends)
print('Sorry, ' + scott + ' you cannot join.')

dane = friends.pop()
print(friends)
print('Sorry, ' + dane + ' you cannot join.')

danielle = friends.pop()
print(friends)
print('Sorry, ' + danielle + ' you cannot join.')

del friends[0:]

print(friends)

cars = ['subaru', 'audi', 'bmw', 'toyota', 'nissan']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Temporary sorting, use sorted()
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

cars.reverse()
print(cars)

print(len(cars))

world = ['italy', 'japan', 'phillipines', 'conneticuit']
print(world)

print(sorted(world))

print(world)

world.reverse()
print(world)

world.sort()
print(world)

print(len(friends))
print(len(world))

for country in world:
    print('\nI want to visit ' + country + '.')
    print('They have tasty food.')
print('\nI hate flying though.')
print('')

pizzas = ['pepperoni', 'bbq chicken', 'margerita', 'cheese', 'vegan']

for pizza in pizzas:
    print('\nI like ' + pizza + ' pizza.')
print('Pizza really is the best.')
print('')

numbers = list(range(0,101))
print(numbers)

# (Start here, go until here, skip every one of this number)
even_numbers = list(range(2,100,2))
print(even_numbers)

squares = []
for value in range(0,11):
    squares.append(value**2)
print(squares)

# List comprehensions, simplify code, reduced lines of code
cubes = [value**3 for value in range(0,11)]
print(cubes)


print(min(numbers))
print(max(numbers))
print(sum(numbers))

for num in range(0,21):
    print(num)

milli = list(range(0,1000000))
print(sum(milli))

odd = list(range(1,21,2))
print(odd)
for num in odd:
    print(num)

three = list(range(0,30,3))
print(three)
for num in three:
    print(num)

names = ['luca', 'dima', 'gino', 'francesco', 'allesandro']
print(names[-1:])

print("Here's what i'd like to name our baby: ")
for name in names[:2]:
    print(name.title())


my_foods = ['pizza,', 'burritto', 'cake']
friend_food = my_foods[:]
print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_food)

my_foods.append('cannoli')
friend_food.append('ice cream')

print(my_foods)
print(friend_food)

dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

buffet = ('rice,', 'chicken', 'beef', 'salad')
for food in buffet:
    print(food)

buffet = ('rice', 'chicken', 'stew', 'cheese')
print('\nModified menu')
for food in buffet:
    print(food)
print('')

deck = ['pikachu', 'mew', 'mewtwo', 'charizard']
deck = deck.pop()
print(deck)


my_list = [1, 3.0, ["a", "b", ["A", "B", "C"], "d"], "John"]
print(my_list[2][2][0])

my_list = ['chicken wing', 'chicken wing', 'hot dog', 'bologna', 'chicken', 'macaroni']
my_string = ''
for index, object in enumerate(my_list):
    my_string += object + ' '
    if index == 3 or index == 4:
        my_string += 'and '
print(my_string)






