'''Write a program that lets the user enter a nonnegative integer
   then uses a loop to calculate the factorial of that number.'''

number = int(input("Enter the number: "))
factorial = 1

if number == 0:
    print(f"{number}! = {factorial}")
else:
    for i in range(1,number+1):
        factorial *= i
    print(f"{number}! = {factorial}")
