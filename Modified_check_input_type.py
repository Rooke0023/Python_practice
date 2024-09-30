#Code by Chatgpt4
def check_input_type(name):
    try:
        # Check if the input is a valid string
        if isinstance(name, str):
            if not name:
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
        # Handle None case or other non-string types
        elif name is None:
            raise ValueError("Input cannot be None.")
        else:
            raise TypeError("Input must be a string.")
    except NameError:
        print("NameError: The input variable is not defined. Please provide a valid string.")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

