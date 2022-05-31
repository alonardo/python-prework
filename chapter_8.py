# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:26:43 2022

@author: aalon
"""
# No information needed in function
# def greet_user():
#     """Displat a simple greeting."""
#     print('Hello!')

# greet_user()

# Information inside parens is needed
# def greet_user(username):
#     """Displays a simple greeting"""
#     print('Hello, ' + username.title() + '!')

# greet_user('jessa')

# def display_message():
#     """Display message about learning Python"""
#     print('We are learning about functions in Chapter 8!')
    
# display_message()

# def favorite_book(book):
#     """Asks user for favorite book then prints favorite book"""
#     print('Your favorite book is ' + book.title() + '.')

# favorite_book('holes')

# def describe_pet(animal_type, pet_name):
#     """Gives information about a pet"""
#     print('\nI have a ' + animal_type + '.')
#     print('\nMy ' + animal_type + "'s name is " + pet_name.title() + '.')

# describe_pet('dog', 'furiosa')
# describe_pet(animal_type = 'dog', pet_name = 'peanut')

# def describe_pet(pet_name, animal_type='dog'):
#     """Gives information about a pet"""
#     print('\nI have a ' + animal_type + '.')
#     print('\nMy ' + animal_type + "'s name is " + pet_name.title() + '.')

# user_pet_name = input('\nWhat is your pets name?')
# user_animal_type = input('\nWhat type of animal do you have?')

# describe_pet(user_pet_name, user_animal_type)

# def make_shirt(text, size = 'large'):
#     print("This is a " + size + " shirt that reads '"  + text + "'.")
    
# make_shirt(size = 'small', text = 'I love python')
# make_shirt(text = 'I quit my job for this')

# def city(city, country):
#     print(city.title() + ' is the capital of ' + country.title() + '.')

# city('salt lake city', 'utah')

# def get_formatted_name(first_name, last_name, middle_name = ''):
#     """Returns a neatly formatted name"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('andre', middle_name = 'aaron', last_name = 'lonardo')
# print(musician)

# def build_person(first_name, last_name, age=''):
#     """Return a dictionary of info on a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age = 27)

# print(musician)

# def get_formatted_name(first_name, last_name, middle_name = ''):
#     """Returns a neatly formatted name"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# while True:
#     print('\nPlease tell me your name:')
#     print("(enter 'q' at any time to quit)")
    
#     f_name = input('First name: ')
#     if f_name == 'q':
#         break
#     l_name = input('Last name: ')
#     if l_name == 'q':
#         break
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print('\nHello, ' + formatted_name + '!')

# def city_country(city, country):
#     print(city.title() + ', ' +  country.title())

# city_country('manila', 'phillipinnes')


# def make_album(artist, album_title):
    
#     album_by_artist = {'Artist': artist.title(), 'Album Title': album_title.title()}
#     print(album_by_artist)
#     return album_by_artist

# make_album('jack johnson', 'in between dreams')
   
   
# def make_album():
        
#         user_artist = input('\nName an artist: ')
#         user_album = input('\nName an album: ')
        
        
#         album_by_artist = {'Artist': user_artist.title(), 'Album Title': user_album.title()}
#         return user_artist
#         return user_album
#         return album_by_artist
#         print(album_by_artist)

# make_album()

# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = 'Hello, ' + name.title() + '!'
#         print(msg)

# usernames = ['pepper', 'sofia', 'bella']
# greet_users(usernames)


# def print_models(unprinted_designs, completed_models):
    
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
        
#         print('Printing model: ' + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print('\nThe following models have been printed: ')

#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# friends = ['ed', 'scott', 'dane']

# def show_friends(friends):
#     for friend in friends:
#         print(friend)

# show_friends(friends)

# def make_great(friends):
#     for friend in friends:
#         print('The Great ' + friend.title() + '!')
        
# make_great(friends[:])
# print('Original names:')
# print('')
# print(friends)

# def make_pizza(size, *toppings):
#     """Print the list of toppings that have been requested"""
#     print('\nMaking a ' + str(size) +
#           '- inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepperoni', 'cheese', 'mushrooms')

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile


# user_profile = build_profile('albert', 'einstein',
#                               location='princeton',
#                               field='physics')

# print(user_profile)


# def gimmie_sandwich(*sandwich):
#     completed_sandwich = {}
#     print('Adding ' + str(sandwich))



# gimmie_sandwich('pickles', 'sand', 'worms')



# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     profile = {}
#     profile['First_name'] = first.title()
#     profile['Last_name'] = last.title()
#     for key, value in user_info.items():
#         profile[key] = value.title()
#     return profile


# user_profile = build_profile('andre', 'lonardo',
#                               Location='utah',
#                               Job='software engineering',
#                               Wife='jessa')

# print(user_profile)



# def car(manufacturer, model, **other):
#     car_profile = {}
#     car_profile['Manufacturer:'] = manufacturer.title()
#     car_profile['Model:'] = model.title()
#     for key, value in other.items():
#         car_profile[key] = value.title()
#     return car_profile

# car_build = car('subaru', 'outback',
#                 Color = 'silver',
#                 AWD = 'true',
#                 Heat_Seats = 'true')

# print(car_build)
    

# def make_pizza(size, *toppings):
#     """Print the list of toppings that have been requested"""
#     print('\nMaking a ' + str(size) +
#           '- inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepperoni', 'cheese', 'mushrooms')

# def blue_fairy():
#     return 'Always let your conscience be your guide'

# print(blue_fairy())

# def rafiki(lion):
#     print(lion + ' ' +
#     'Oh yes, the past can hurt. '+
#     'But the way I see it, '+
#     'you can either run from it or learn from it')

# rafiki('simba')

# def dory(fish, minutes_since_last_talked):
#     if minutes_since_last_talked > 10:
#         print('Who are you?', end=' ')
#     else:
#         if fish == 'Nemo':
#             print('Just keep swimming', end=' ')
#         else:
#             print('I dont know you', end=' ')

# print(dory('Nemo', 90))

# def emperor(word_a, word_b):
#     my_string=('The '+word_b+' that blooms ' +
#                'in adversity is the most ' +
#                'rare and '+word_a+' of all.')
#     return my_string

# word_1 = 'flower'
# word_2 = 'beautiful'
# print(emperor(word_b=word_1, word_a=word_2))

# def see_character(name, age, species='human'):
#     print(name,age,species)
    
# see_character('Ariel', 16, 'mermaid')

# x=5
# def some_func(x):
#     print(x, end=' ')
# print(x, end=' ')
# some_func(1)
# x = x -1
# print(x, end=' ')
# some_func(1)

# def fun_a(number):
#     return number + 5

# def fun_b(number):
#     return number * 2
# print(fun_a(fun_b(5)))

# def do_something(a_list):
#     my_string=''
#     for element in a_list:
#         my_string += element[0]
#     return my_string
# aladdin_characters = ['Jasmine', 'Aladdin', 'Fazahl', 'Abu', 'Razaoul']
# print(do_something(aladdin_characters))







