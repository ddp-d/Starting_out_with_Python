'''Write a program that asks the user for the speed of a vehicle and the number of hours
   it has traveled. Use the loop to display the distance 
   the vechicle has traveled for each hour.'''
speed = int(input("What is the speed of the vechicle in mph? "))
time = int(input("How many hours has it traveled? "))


print("Hour \t Distance Traveled")
print("__________________________")

for i in range(1,time+1):
    distance = speed * i
    print(i,"\t", distance)
