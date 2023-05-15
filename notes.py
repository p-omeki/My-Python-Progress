   
 ## This is only applicable to tribranch 
 '''
The Tribranch is the feature branch of the main branch
    Now the code has two branches; tribranch and main branches
    '''
    ##Python multi-line continuation character
 '''
    Statements in python typically ends with a new line. However, python allows the use of line continuation character (\)
    that allows the line to continue.
    Statements between {},[] and () however don't need the character (\) to continue on to the next line
    The below statement works perfectly in Python..
    '''
    
 days =['Monday','Tuesday','Wednesday',
            'Thursday', 'Friday']
            
            
    ##Quotation and Comments in Python
 '''
    In python, there are 3 different types of quotation. Single (''), Double ("") and Triple(''' ''') quotes
    Check the examples below on quoatation in Python:
    '''
 word = 'Word'
 statement = "This is a statement"
 paragraph = '''This quote is used mostly in multi-line statements
            and paragraph blocks in python
            '''
    ##Comments
    #This statements is an example of a comments and it makes python codes to be easily readable to
    #humans. It also make it easy to understand code. Check example below:
            
    #First comment
 print ("Hello World") #Second comment
 #Python tuple and lists are similar, the only difference between the two is that 
 #~list are enclosed with brackets [] and it can be changed (elements) while tuple are 
 #~enclosed with parenthesis ()  and cannot be changed. Basically, tuples are 
 #~read-only lists.
 #Tuples are immutatble which means you can not change or update the value of a tuple
 #Types of python operators
   '''
   1. Arithmetic operators - Includes the Addition(+), Substraction(-), Multiplication(*), Modulus(%),Exponent(**), Floor division(//), etc.
   2. Bitwise operators.
   3. Relational(Comparisson) operators - Includes Equal(==), Not equal(!=), Greater than(>), Less than (<), etc.
   4. Logical operators - Includes the Logical AND,OR or NAND
   5. Assignment operators  - Includes the (=), (+=), (-=), etc.
   '''
  
  #Decision makeing in Python
   '''
    Decision making in Python is the anticipation of condition when executing a program.
    In Python, there is the if statement, if else and the nested if statement.
    In if statement, can only be used when we want only to find a TRUE statement. If the condition is true, the compiler executes the conditional code and if not it jumps to produce a False output.
    In if else statement, can only be used when we want both TRUE and FALSE statement. If the condition is true, it executes the if statmt. and if false it execute the else statement.
    Also, there's the elif statement, similar to if else but it can only be used when we want to execute multiple TRUE statements.
    The major difference between elif statement and if  else statement is that elif can be used to execute multiple TRUE statement while if else can only be used when executing at most one statement...
    Lastly, the nested if sttmt., it used when executing an if statement inside another if statement. Basically, I would say it's a combination of if else and elif statement.
    Construct if...elif...else
   '''
   #Dictionary in Python
   """
   Keys in dictionary are separated by (:) and the values are separated by commas (,) and the whole dictionary is enclosed by {}
   Keys within a dictionary are unique while the values may be of any type. Keys are immutable data types such as String, Numbers or Tuples.
    
   """
   #Example of a dictionary in Python
   dict = {'Name': 'Zara', 'Age': 10}
   print ,dict['Name']
   '''
   The "Name" in the dictionary above is the 'key' while "Zara" is the 'value'
   The Name and the Age right now are the immutable data types.
   Properties of Dictionary 
     1. More than one key entry is not allowed.
     2. Key should be immutable.
   '''
   #Functions in Python
   """
   A function is a block of organized, reusable code that is used to perform a single, related action. Functions in Python are defined as:
      1. Functions start with 'def' keyword which defines the function. It's followed by the function name and lastly a paranthesis.
      2. Any argument or parameters is defined inside the paranthesis or at times the parameters contain nothing in between them.
      3. Functions after defining and enclosing it with parameters is followed by (:) and it's indented.
      4. The function uses a return[] to exit an action
    The code below describes the above points;
    def printme( str ):
      "This prints a passed string into this function"
       print str
       return      
   """
   #Module in Python
   ##A module is a file consisting of Python code.It can define functions, classes and variables and also include runnable code.
   #Packages in Python
   ##A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and subpackages and sub-subpackages, and so on.
   #In Place operator in Python
   """The in place opeartor in python was introduced because it was found that it was not a good programming practise to specify two variables in one line of code.
   Though, it's logically correct, it's not advisable.
   Example, a variable age declared as : "age=age+1", now we can see that clearly there are two variable age declared on the line and so what the in place operator 
   does to the code is that, it will make it: "age+=1". Here, the inplace operator is "+=", also "-=" ,"*=", e.t.c.
   """