'''Write a program with a loop taht repetedly asks the user to enter a word
   and display the average length of the words entered, rounded to the nearest whole number'''
sum_of_length = 0
number_of_words = 0

while True:
    word = input("Enter word (or Enter to quit): ")
    if not word:
        break
    length = len(word)
    sum_of_length += length
    number_of_words += 1
    
#average length of the words entered
average_length = sum_of_length / number_of_words
print(f"Average length of the words entered: {round(average_length)}")
