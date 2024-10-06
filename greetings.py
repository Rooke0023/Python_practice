        


"""This function checks whether the input from the user is a string or not.

    Returns:
        Greetings: If the input is a string
        Correction: Prompts the user to input a valid name.
        
"""
def check():
    
    
    name = input("What is your name? ")
    while not name.isalpha():
        print("It is not a valid name. Please try again.")
        continue
    else: 
        print(f"Welcome {name}!")
        
# The foundation of the code to validate an input by the user
""" 1. Ask for an input from the user
    2. Check whether the input contains alphanumeric or not.
    3. Print greetings if validated. Otherwise reprompt.
"""


def validate_input(name):
    """Checks whether an input is alphanumceric or not and returns the argument. This function implicitly returns "None" value otherwise."""
        
    if name.isalpha():
        return name
    
    

def main():
    
    """This function checks for an input which is alphanumeric. If not, it loops back into prompting.
    It has some layers. 
    The first layer creates an infinite loop.
    The second layer uses the try/except block to catch any errors that might occur. It is quite general but it is a precautio against crashing the program.
    So the infinite loop contains the second layer. The except statement actually is redundant as it doesn't capture anything."""
    
    while True:
        try:
            x = input("What is your name? ")
            
            if validate_input(x):           #Here the if statement is triggered when this function is true. If this function is true, it returns the argument as defined in the function
                print(f"Welcome to the program {x}!")
                break
            else:
                print(f"Please input a correct prompt.") 
                    
        except:
            print(f"There has been error. Please do it again.")
            
    
main()
