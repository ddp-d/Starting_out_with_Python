'''Write a program that predicts the approximate size of a population of organism.'''

starting_number = int(input("Enter the starting number of organisms: "))
average_increase = int(input("Enter the average daily increase (percentage): "))
number_of_days = int(input("Enter the number of days to multiply: "))


print("Day Approximate \t Population")
print(1,"\t \t \t",starting_number)
for i in range(2,number_of_days+1):
    starting_number += starting_number * average_increase / 100
    print(i,"\t \t \t",starting_number)
