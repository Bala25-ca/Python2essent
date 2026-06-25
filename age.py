def validate_age():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age between 1 and < 121.")
        return

    print("Your age is:", age)
    if age < 0:
        print("Age cannot be negative.")
    elif age > 120:
        print("Age is too high.")
    else:
        print("Age is accepted.")

if __name__ == "__main__":
    validate_age()
