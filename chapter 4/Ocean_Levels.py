'''Write a program that displays the number of millimeters that the ocean
   will have risen each year for the next 25 years.'''

rising_level = 1.6 #per year

print('Year \t', 'Milimeter')
for i in range(1, 26):
    level = i * rising_level
    print(format(i, '2.0f'), '\t', format(level, '5.2f'), 'milimeter')
