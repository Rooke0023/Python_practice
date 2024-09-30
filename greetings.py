"""Code created by GPT-4"""

# def validate_input(name):
#     if not isinstance(name, str):
#         return "It is not a string, so can't proceed further. Sorry."
    
#     elif len(name) == 0:
#         return "This is an empty string."
    
#     elif name.isalpha():
#         return "This is a non-empty alphabetic string. ✅"
    
#     else: 
#         return "This is a non-empty string, but it is not alphabetic."

# print(validate_input("Maruf"))
# print(validate_input("000"))
# print(validate_input(000))
# print(validate_input(""))

# def validate_input():
#     while True:
#         name = input("Enter your name: ")
        
#         # Check if the input is a non-empty, alphabetic string
#         if isinstance(name, str) and name.isalpha() and len(name) > 0:
#             print("This is a non-empty, alphabetic string. ✅")
#             break  # Exit the loop if the input is valid
#         else:
#             print("Invalid input. Please enter a non-empty, alphabetic string.")

# Call the function to start the validation process.


def validate_input():
    while True:
        name = input("What is your name?\n")
        if name.isalpha():
            return print ("This is a non-empty alphabetic string.")
        else:
            print("Please enter a valid name with only alphabetic characters.")

# Call the function
validate_input()
