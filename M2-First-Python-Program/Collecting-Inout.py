import sys



print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)


'''

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg


'''

# Accepting user input

'''
Using this code as a foundation, update how parsecs is set. 
Start by creating a variable named parsecs_input and setting it to the result of input, which should prompt the user to enter the number of parsecs. Then convert parsecs_input to an integer by using int and storing it in parsecs. 
Finish by performing the calculation and displaying the result.
'''

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")