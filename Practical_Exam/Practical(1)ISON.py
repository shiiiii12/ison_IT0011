#Rishi Nicolas M. Ison - TC21 - Practical Exam - Palindrome

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def check_numbers_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")

print("Checking numbers.txt for sum palindromes:\n")
check_numbers_file("numbers.txt")