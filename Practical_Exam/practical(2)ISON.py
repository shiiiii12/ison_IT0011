#Rishi Nicolas M. Ison - TC21 - Practical Date converter

from datetime import datetime

def format_date():
    date_str = input("Enter the date (mm/dd/yyyy): ").strip()

    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        formatted_date = date_obj.strftime("%B %d, %Y")
        print("Date Output:", formatted_date)
    except ValueError:
        print("Invalid date format. Please use mm/dd/yyyy.")
        return  # Exit early if input is invalid

    while True:
        choice = input("Do you want to enter another date? (yes/no): ").strip().lower()
        if choice == "yes":
            format_date()  # Recursive call for another input
        elif choice == "no":
            print("Exiting program. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

format_date()() mo