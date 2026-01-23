# Main program with exception handling

from math_utils import add, divide

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Division:", divide(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Calculation completed successfully.")
    
    
print("\nMini Practice Completed Successfully")
