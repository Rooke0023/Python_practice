
#Importing the regular expression allows me to be more specific in targeting. I want to target strings with only special characters, hence it's use.
    
import re

#This is the original code

def check_input_type(name):
    
    """Checks for the input type and generates a statement saying what the input is
        Desired input is a string."""
        
    #I have put the digit filter at the top of alphanumeric because individual cases are better to be filtered first rather than mixed cases. The python code follows a control flow and my function as a programmer is to identify which criteria needs to be assessed first.
    
    #The reason of following this order is to always putting the specific condition at the top and more general ones at the bottom.
    
    #Checks for: alphabets, digits, alphanumericals, empty string, whitespaces, and special characters.

   
    if isinstance(name, str):
        if name.isalpha():
            print(f"It is a non-empty, alphabetic string.")
        elif name.isdigit():
            print(f"It contains only numbers as string and it is non-empty.")
        elif name.isalnum():
            print(f"It contains both alphabets and numbers and it is non-empty.")
        elif len(name)==0:
            print(f"It is an empty string.")   
        elif name.isspace():
            print(f"It is a string which has nothing written on it and has whitespaces.") 
        #Regex to detect special characters. The explanation for this code could be found at the end of this file. Read on.
        elif re.match("^[^a-zA-Z0-9\s]+$", name):      
            print(f"It contains only special characters.")
        else:
            print(f"It is a string with a mixture of special characters.")   
    else:
        print(f"It is not a string, so can't proceed further. Sorry.")
        

#Running some tests to see if the function properly works and it does.
        
print("")
check_input_type("Maruf")
check_input_type("Maruf123")
check_input_type("123")
check_input_type(" ")
check_input_type("")
check_input_type(123)
check_input_type("@")
check_input_type("@@@")
check_input_type("@123")


# Code by Claude 3 opus

#What I like about the code below is that it starts with the very specific condition I, as the primary benefactor of this function, look forward to accomplish. That being: not wanting any data types other than a string. 

#The purpose of an if/else condition is to address the most specific condition first. As the flow progresses, the conditions become increasingly broad and inclusive.


def check_input_type(name):
    if not isinstance(name, str):
        print("It is not a string, so can't proceed further. Sorry.")
    elif not name:
        print("It is an empty string.")
    elif name.isspace():
        print("It is a string, but it contains only whitespace.")
    elif name.isalpha():
        print("It is a non-empty, alphabetic string.")
    elif name.isdigit():
        print("It contains only numbers as string and it is non-empty.")
    elif name.isalnum():
        print("It contains both alphabets and numbers and it is non-empty.")
    else:
        print("It is a string, but it contains special characters or spaces.")

print("")
check_input_type("Maruf")
check_input_type("Maruf123")
check_input_type("123")
check_input_type(" ")
check_input_type("")
check_input_type(123)
check_input_type("@m.")
check_input_type("@123")

#This code snippet is supposed to match only special characters
#In regex, starting with ^ and ending with $ means start to finish, literally. This means that from start to finish of this string, it contains at least one special character.

import re
if re.match("^[^a-zA-Z0-9\s]+$", "1@@@"):      
    print(f"It contains one or more special characters.")
else: 
    print("False.")


#This code snippet is supposed to find just one special character in the string to return True. For that the anchors ^ and $ are used. Here, it means that the string in question is just one character from start to finish.

import re
if re.match("^[^a-zA-Z0-9\s]$", "!!!!"):      
    print(f"It contains one special character.")
else: 
    print("False.")