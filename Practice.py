"""This function accepts an input from the user and prints a positive statement is the desired input is given and vice versa. The try/except block is used in occasions where we want to catch any kind of errors or exceptions."""
def main():
    try:
        x = int(input("What is x?\n"))
    except ValueError:      #if something goes wrong, this code is executed
        print("Please provide an integer as input. Try again.")
    else:           #else statement catches on the attention of the code after line 4 is positive.
        print(f"x is {x}")



main()