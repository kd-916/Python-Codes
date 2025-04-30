while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        print(f"Thank you! You entered the integer: {number}")
        break
    except ValueError:
        print("Error: That's not a valid integer. Please try again.")
