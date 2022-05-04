'''Write a program that displays a table of distances in miles and their equivalent dostances 
   in kilometers, rounded to 2 decimal places.'''

one_mile = 1.60934 #one mile is equivalent to 1.60934

print("Miles \t Kilometers")
print("__________________________")

for i in range(10,81,10):
    kilometers = i * one_mile
    print(i,"\t", round(kilometers,2),"km")
