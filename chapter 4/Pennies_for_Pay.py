''' Write a program taht calculates the amount of money a person would earn over a period
    of time if his or her salary is one penny the first day, two pennies the second day,
    and continues to double each day'''
total_pay = 0
number_of_days = int(input("Enter the number of days: "))

print("Days \t Salary(pennies)")
print("_______________________________")

for i in range(1,number_of_days+1):
    salary_penny = 2 ** (i - 1)
    salary_dallar = salary_penny/100
    total_pay += salary_dallar
    print(i,"\t",salary_dallar,"dollars")
    
print("____________________________")
print(f"Total pay: {total_pay}")
