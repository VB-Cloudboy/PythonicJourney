'''
If the test expression is False, the code in the body of the if statement is skipped, and the program continues running from the else statement. 
The syntax of an if/else statement is always:
'''
e=10
f=15
if e>f:
    print("E for Elephant is greater than F for Fish")
    # statement(s) to be run
else:
    print("F for Fish is smaller but faster than E for Elephant")
    # statement(s) to be run

'''
Work with elif, 
In Python, the keyword elif is short for else if. 
Using elif statements enables you to add multiple test expressions to your program. 
These statements run in the order in which they're written, so your program will enter an elif statement only if the first if statement is False. 
'''
a=33
b=64

if a<=b:
    print("a is less than or equal to b")
elif a==b:
    print("a is equal to b")

'''
Combine if, elif, and else statements
You can combine if, elif, and else statements to create programs with complex conditional logic. Remember that an elif statement is run only when the if condition is false. 
Also note that an if block can have only one else block, but it can have multiple elif blocks.
'''

m=234
n=345

if m>n:
    print("m is greater than n")
elif n>m:
    print("n is greater than m")
else:
    print("m is equal to n")

'''
Work with nested conditional logic
Python also supports nested conditional logic, meaning that you can nest if, elif, and else statements to create even more complex programs. 
To nest conditions, indent the inner conditions, and everything at the same level of indentation will be run in the same code block:
'''
g=5456
h=6782
i=8493

if g>h:
    if h>i:
        print("g is greater than h and h is greater than i")
    else:
        print("g is greater than h but less than i")
elif g==h:
    print("g is equal to h")
elif h==i:
    print ("h is equal to i")
else:
    print("i is greater than g & h")

'''
The or operator
You can connect two Boolean, or test, expressions by using the Boolean or operator. 
For the entire expression to evaluate to True, at least one of the subexpressions must be true. 
If none of the subexpressions is true, the whole expression evaluates to False. 
For example, in the following expression, the entire test expression evaluates to True, because one of the conditions in the subexpressions has been met:
'''    
exam_passing_score = 70

chintu_science= 38
chintu_geography = 32

if chintu_science >= 40 or chintu_geography >=40:
    print(chintu_science + chintu_geography)
    print ("chintu passed the exam")
else:
    print("Chintu didn't score more than 40 in one exam so failed")


