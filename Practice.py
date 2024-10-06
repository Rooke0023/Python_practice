"""This function accepts an input from the user and prints a positive statement is the desired input is given and vice versa. The try/except block is used in occasions where we want to catch any kind of errors or exceptions."""
def main():
    try:
        x = int(input("What is x?\n"))
    except ValueError:      #if something goes wrong, this code is executed
        print("Please provide an integer as input. Try again.")
    else:           #else statement catches on the attention of the code after line 4 is positive.
        print(f"x is {x}")



<<<<<<< HEAD

#This function asks for an input from the user and calls the function "hello() which accepts one parameter"
def input():   
    name = input(f"What is your name?\n")
    hello(name)
    

#This function takes one parameter and prints a statement using the parameter   
def hello(x):   
    print(f"Hello {x}!")
   

#This function calls the print_row function which takes in one parameter
def main():
    print_row()
    
#This function generates a sequence of # symbols corresponding to the argument given to its parameter.
def print_row(row="cmon"):
    print("#", "@", "$" * row, sep="!")
    
    
main()

=======
main()
>>>>>>> 7697ddbea8f8b8e55cf21b41a585e8ba4a18fa2b
