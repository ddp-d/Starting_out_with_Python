'''Write a program with the loop that displays the projected 
   semester tuition amount for the next 5 years.'''

semester_tuition = 8000 #dollars
increase_percent = 1.03
number_of_years = 5

print("Projected semester tuition.")
print("____________________________")
for i in range(1,number_of_years+1):
    semester_tuition *= increase_percent
    print(round(semester_tuition,2))
