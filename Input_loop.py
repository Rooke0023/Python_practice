#The main purpose of this function is to call two additional functions. It prompts the user for an integer and then prints "meow" a corresponding number of times.
def main():
    number  = getnumber()
    meow(number)
    

#The purpose of this function is to ask for an integer input from the user and returns that number.
def getnumber():
    n = int(input("What's the number? "))
    return n

#This function generates a range of numbers based on the integer input, creates a loop that iterates over this range, and prints "meow" the specified number of times.
def meow(n):
    for _ in range(n):
        print("meow")
    
main()