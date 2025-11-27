# Q23: Write a program that accepts date of birth along with the other personal details. Throw an exception if an invalid date is entered.
from datetime import datetime

try:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

    try:
        valid_dob = datetime.strptime(dob, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Invalid Date of Birth! Please enter the date in DD-MM-YYYY format.")

    print("\n--- Personal Details ---")
    print("Name:", name)
    print("Age:", age)
    print("Date of Birth:", valid_dob.strftime("%d-%m-%Y"))

except Exception as e:
    print("Error:", e)

