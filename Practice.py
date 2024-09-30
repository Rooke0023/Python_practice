""" Defining a function to call another function can be beneficial because now the functions can be organized in whatever position needed and do not need to be necessarily written before they are called. That means, the hello function can be written and placed above the main function and when we call the main function which then calls the hello function, it will still work fine. """




#This function asks for an input from the user and calls the function "hello() which accepts one parameter"
def main():   
    name = input(f"What is your name?\n")
    hello(name)
    

#This function takes one parameter and prints a statement using the parameter   
def hello(x):   
    print(f"Hello {x}!")
   

