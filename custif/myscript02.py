#!/usr/bin/env python3
print('What is your grade') 
grade = float(input())
letter  = 'Your letter grade is '
if grade > 90:
        letter = letter + 'A'
elif grade >= 80: 
        letter = letter + 'B'
else:
    letter = letter + 'F'
print(letter)
        
