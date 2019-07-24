#!/usr/bin/env python3
round = 0 
while(True):
        round = round + 1 
        print('finish the movie title, "monty python\'s The life of ______"') 
        answer = (input().casefold())
        if (answer == ('Brian').casefold()):
                print('Correct')
                break
        elif(answer == ('shrubbery').casefold()):
                print('You gave the super secret answer')
                break
        elif(round == 3):
                print('Sorry, The answer was Brian.')
                break
        else:
            print('sorry try again!')
