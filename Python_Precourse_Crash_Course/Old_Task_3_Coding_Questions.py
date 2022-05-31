# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:45:16 2022

@author: aalon
"""

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    print('hello_' + user_name + '!')
  
                
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
     for odd in range(100):
         if odd % 2 != 0:
             print(odd)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = max(a_list)
    print(max_num)
    return max_num
                
# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).
# A leap year is divisible by 4
# A leap year is not divisble by 100

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            if a_year % 400 == 0:
                a_year = False
            else:
                a_year = True
        else:
            a_year = False       
    else:
        a_year = False
        
    print(a_year)
    

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

consecutive_list = [2,3,4,5,6,7]
not_consecutive_list =[1,2,4,5]

def is_consecutive(a_list):

    consecutive = True
    for index, num in enumerate(a_list):
        if index + 1 < len(a_list) and index -1 >= 0:
            previous = a_list[index-1]
            current = num
            after = a_list[index+1]
            
            if current + 1 == after:
                consecutive = True
            else:
                consecutive = False
    print(consecutive)

