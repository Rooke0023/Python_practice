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
    
#The __name__ variable is implicitly set for any module to be "__main__" when it is called from a terminal. When we import the module into another program, the variable then gets changed to the name of the module, i.e.Input_loop. So using this conditional makes it possible for us to import different elements inside this module separately without executing the main() function. Because, when we import this module into another program, this conditional becomes false.
if __name__=="__main__":
    main()