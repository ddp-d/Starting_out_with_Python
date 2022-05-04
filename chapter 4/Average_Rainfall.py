'''Write a program thet uses nested loops to collect data and calculate
   the average rainfall over a period of years.'''
number_of_years = int(input("Enter the numbet of years: "))
number_of_months = 12

total_inches = 0

for i in range(1,number_of_years+1):
    for j in range(1,number_of_months+1):
        inches_of_rainfall = float(input(f"Enter the inches of rainfall for {j} month {i} year: "))
        total_inches += inches_of_rainfall

total_month = number_of_months * number_of_years
average = total_inches / total_month

print(f"The number of month - {total_month}.") 
print(f"The total inches of rainfall - {total_inches}.") 
print(f"The average rainfall per month for the entire period - {average}.") 
