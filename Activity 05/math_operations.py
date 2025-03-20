def divide(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))