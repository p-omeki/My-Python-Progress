## Variables in a python are memory location used to store values in a python program
## Variables are first created then values are assigned to them.
## Creating a variable below;
name = "Patrick Meki" #Creating a string variable
year = 3 #Creating  an integer variable
study = 3.2 #Creating  a floating point value variable

print (name)

##del (study) # Now, what this will do is that it will delete variable 'study' and if we try to print variable study it will bring an error!

##Local variable and Global variable
'''
The major difference in this is that in local variable, variables cannot be accessed outside a function
while in Global variable, variable can be accessed outside of a function. Below, it's a simple
Local and Global Variable difference
'''
#Local Variable
'''def sum(x,y):
    sum =x+y
    return sum
print (sum(5,10))'''
#Global Variable
x = 5
y = 10
def sum():
    sum = x+y
    return sum
print(sum()) 