'''Write a program that should display the time of their
fastest lap, the time of their slowest lap, and average lap time.'''
number_of_times = int(input("Enter the number of times that you have run: "))

total_time = []
for i in range(1,number_of_times+1):
    lap_time = float(input(f"Enter the lap time for {i} lap: "))
    total_time.append(lap_time)

average = sum(total_time)/number_of_times
print(f"Fastest time of your lap - {min(total_time)}mins")
print(f"Slowest time of your lap - {max(total_time)}mins")
print(f"Your average lap time - {average}mins")
