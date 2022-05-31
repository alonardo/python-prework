# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:46:33 2022

@author: aalon
"""

message = 'Hello world!'
print(message)

message = 'Hellloooo!'
print(message)

# Makes uppercase at beginning of word
name = "ada lovelace"
print(name.title())

# Upper and lower case
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Concatenates strings using the +
first_name = 'andre'
last_name = 'lonardo'
full_name = first_name + ' ' + last_name

greeting = ('Hello ' + full_name.title() + '!')
print(greeting)
print('\thello')
print('\nhello')
print('\n\thello')

language = ('     Python   ')
print(language)

# Removes whitespace beginning at end
print(language.strip())

# Example of how to use quotes and apostrophe
test = ("One of Python's greatest strengths is its diverse community")
print(test)

name = ('Coral')
print('Hello, ' + name + '! Would you like to learn Python today?')

print(name.lower())
print(name.upper())
print(name.title())


famous_person = 'Coral'
print(famous_person + ' once said, "Good is the enemy of great."')

baby = '    Coral   '
print(baby)
baby_name = baby.strip()
print(baby.lstrip())
print(baby.rstrip())
print(baby)

age = 1
print('Happy ' + str(age) + 'st birthday!')

print(4 + 4)
print(2 * 4)
print(8 / 1)
print(2**3)
fav_num = 10
print(fav_num)
# Use comments more to detail what you're doing
import this
phrase = "John's shirt is green"
phrase=phrase.upper()
print(phrase)

phrase=" A "
new_phrase = phrase.lower().rstrip() + phrase * 3
new_phrase = new_phrase.strip()
print(new_phrase)

name = "Steve"
verb = "runs"
preposition = "to"
artivle = "the"
direct_object = "store"
print(
      direct_object.upper() + verb.title() + preposition.lower() + name.lower()
      )










