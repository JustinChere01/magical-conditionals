number = float(input("Enter a number: "))  # Convert input to a floating-point number

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Python program to find the largest number among three input numbers
# Change the values of num1, num2, and num3 for different results
num1 = 10
num2 = 14
num3 = 12

# Uncomment the following lines to take three numbers from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)