import math_operations as mo

def main():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()

        if choice == 'Q':
            print("Exiting program.")
            break
        elif choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 'D':
                    result = mo.divide(num1, num2)
                elif choice == 'E':
                    result = mo.exponentiate(num1, num2)
                elif choice == 'R':
                    result = mo.remainder(num1, num2)
                elif choice == 'F':
                    result = mo.summation(int(num1), int(num2))

                if result is not None:
                    print(f"Result: {result}")

            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")

        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()