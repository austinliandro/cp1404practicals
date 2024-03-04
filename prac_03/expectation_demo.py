"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
-  when the users enter a number that can't be converted to integer number.
2. When will a ZeroDivisionError occur?
- when the number is cannot divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By adding if else statement, if the denominator is == to zero, so it will print
the statement that it cannot divide by zero, else will calculate the fraction and print the value.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divided by 0!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished!")
