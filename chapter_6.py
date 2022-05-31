# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:51:43 2022

@author: aalon
"""

jessa = {'food': 'rice', 'birthday': 'July 14th', 'Occupation':
         'Product Strategy Manager', 'status': 'single'}
print(jessa['food'])

print("Jessa's birthday is " + jessa['birthday'])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('Jessa is ' + jessa['status'] + '.')

jessa['status'] = 'married, bitches!'
print('Jessa is ' + jessa['status'] + '.')

alien_0 = {'color': 'green'}
print('The alien is ' + alien_0 ['color'])

alien_0['color'] = 'yellow'
print(alien_0['color'])

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# New position is old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + '.')

coral = {
    'name': 'coral',
    'birthday': 'october 8',
    'city': 'olympia'}

print('My name is ' + coral['name'].title() + '.')
print('My birthday is ' + coral['birthday'].title() + '.')
print('I live in ' + coral['city'].title() + '.')

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print('\nKey: ' + key.title())
    print('Value: ' + value.title())

for x, y in coral.items():
    print('\n' + x.title())
    print(y.title())

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite language is " +
          languages.title() + ".")
    
for name in favorite_languages.keys():
    print(name.title())

# So, .items() returns a a dict as a list?
# and .keys allows you to only look at the keys
# .keys() helps with readability, Pyhton will default to reading keys
# .values on the flipside
# i.e
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print('Hello ' + name.title() +
              ', I see your favorite language is ' +
              favorite_languages[name].title() + '!')

if 'erin' not in favorite_languages.keys():
    print('Please take our poll.')

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for participating.')
    
print('')

# Using .set to force unique values
print('Here are the following languages: ')
for language in set(favorite_languages.values()):
    print(language.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print('')
# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    

        
# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created
print('Total number of aliens: ' + str(len(aliens)))

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
      'with the following toppings: ')

for topping in pizza['toppings']:
    print('\t' + topping)
    
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
    

friends = {
    '1': {
        'first': 'scott',
        'last': 'varner',
        'age': '32',
        },
    '2': {
        'first': 'dane',
        'last': 'wilkes',
        'age': '32',
        },
    '3': {
        'first': 'ed',
        'last': 'mckonkie',
        'age': '30', 
        },
    }

for friend, friend_info in friends.items():
    print('\nFriend: ' + friend)
    full_name = friend_info['first'] + ' ' + friend_info['last']
    
    print('Full name: ' + full_name.title())
    print(friend_info['age'] + ' ' + 'years old.')
print('')


my_dict = {
    'name': 'Troy Aikman',
    'position': 'QB',
    'team': 'Dallas Cowboys',
    'age': 54,
    'weight': '220',
    'superbowls': ['XXVII', 'XXVIII', 'XXX'],
    'awards': {
        'super_bowl_mvp': 'XXVII',
        'probowl': [1991, 1992, 1993, 1994, 1995, 1996],
        'man_of_the_year': 1997
        }
    }

for key, value in my_dict.items():
    if value == 54:
        print('Old', end='')
    if value == 'age':
        print('54', end ='')
    print('x', end='')















# print(my_dict.get('awards', 'age'))

# print('')

# print(my_dict.get('awards', 'age')['probowl'])

# print('')

# print(len(my_dict['position']))

# print(my_dict.get('awards' , 'age')['probowl'][len(my_dict['position'])])

























