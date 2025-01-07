# functions are a way to wrap your code
# into reusuable units

#Define a funtion
#YOU ONLY DEFINE THE FUNCTION ONCE
#whatever I pass inside the parantheses 
#Is called a parameter
#A parameter is a palceholder for future information

# def sayHello(name,age, street):
#     print(f"say hello {name} :D")
#     print("Hello Governor")
#     print(f"Welcome back {name}")
#     print(f"your age is {age}")
#     print(f"Your street is {street}")

# once you can define a function
# you can call or invoke the function as many times as you like
#when I pass information into the called function it is called an ---argument---
    
#sayHello("Sofi", 16, "Kostner")
#sayHello("Shey", 19, "59th Place")

#IT DOES MATTER THE WAY YOU PLACE IT AS IT ASSINGS VALUE BY ORDER

# def determineEligibility(age):
    #if your age is over 18 you can vote
    #otherwise you can'
    # if age >= 18:
    #     print("You can vote")
    # else:
    #     print("you have to wait :/")

#determineEligibility(12)
#determineEligibility(15)
#determineEligibility(19)

# def willYouGraduate(gpa,credits,SAT):
    #gpa :number variable
    #credits :number variable
    #passed SAT :boolean
#     if (gpa == 3.0) and (credits >= 28) and (SAT == True):
#         print("You passed, Good luck in college")
#     elif (gpa <3.0) or (credits <28) or (SAT != True):
#         print("Back to the drawing board.")
#     else:
#         print("Talk to your counselor")
    
# willYouGraduate(2.8,15,True)
# willYouGraduate(1.5,27,False)
# willYouGraduate(3,28,True)
    
#return = statement used to END A FUNCTION 
#And sent result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x,y):
    z= x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first= first.capitalize()
    last= last.capitalize()
    return first + " " + last

full_name = create_name("Spongebob", "Squarepants")
