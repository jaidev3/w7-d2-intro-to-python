# Create a robust program that validates user input for type, range, and empty input. Keep prompting the user until valid input is provided. Use try-except blocks to handle errors and ensure the program doesn't crash on invalid input.

def validate_age_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Input cannot be empty")
            if not user_input.isdigit():
                raise ValueError("Invalid Input, Please enter an valid age")
            value = int(user_input)
            if min_value is not None and value < min_value or max_value is not None and value > max_value:
                raise ValueError(f"Out of range, Please enter an age between {min_value} and {max_value}")
            return value
        except ValueError as e:
            print(f"{e}\n")
            print("Please try again.")

def main():
    print("User Age Validator")
    age = validate_age_input("Enter your age: ", 1, 120)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()