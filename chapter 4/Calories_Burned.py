'''Program that uses a loop to display the number of calories
   burned after 10, 15, 20, 25, and 30 minutes.'''
cal_per_one_minute = 4.2

for i in range(10,31,5):
    cal_per_minutes = cal_per_one_minute * i
    print(f"Burned calories after {i} minutes - {cal_per_minutes}.")
