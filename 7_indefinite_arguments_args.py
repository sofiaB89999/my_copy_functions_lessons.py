# *args = allows you to pass mutiple non-key arguments
# **kwargs = allows you to pass multiple key-word arguments
#        * unpacking operator
#           1.positional 2.default 3.keyword 4.ARBITRARY

#Example 1:
# def add(*nums):
#     total = 0
#     for every arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5))

#Example 2:
# def display_name(*args):
#     for every arg in args:
#         print(arg, end="")

# display_name("Dr", "Spongebob", "Squarepants")

#Example 3:
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(F"{key} : {value}")
    #print(type(kwargs))    #<---- This prints out <class'dict'>n in the terminal so be careful

print_address(street="Kostner" , 
              city="Chicago", 
              state="Illinois", 
              zip="60652")

#Prints out this in terminal
# street : Kostner
# city : Chicago
# state : Illinois
# zip : 60652
#----------------------------------------------------------------------------------------------------------------------------------------------
# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"