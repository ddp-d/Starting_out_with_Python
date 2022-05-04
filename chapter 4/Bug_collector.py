'''Programs that keeps a running total of the number of bugs
   collected during the five days.'''
total_bugs = 0

for i in range(1,6):
    bugs_per_day = int(input(f"Enter the number of bugs for day {i}: "))
    total_bugs += bugs_per_day
    
print(total_bugs)
