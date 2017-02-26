#i want people to guess a random number i thought of
#I need a random number
#I need a input
#I need a input comparing with random number and give feedback
#I want to give only 5 chances


import random

guess_ai = random.randint(1,20)
def guess_number():
    n=1
    while n <=5:
        user_input = input ("Guess a number ")
        diff_user_ai = int(int(user_input) - int(guess_ai))
        print (diff_user_ai)
        if int(user_input) in range (0,20):
            print ("Right track")
        else:
            print ("Enter a number between 1 and 20")
        if int(diff_user_ai)==0:
            print ("You guessed the right number " + str(user_input))
            break
        elif int(diff_user_ai) <=-5:
            print ("You are too low")
        elif 5 <= int(diff_user_ai):
            print ("You are too high")
        elif -2 <= int(diff_user_ai) <= 2:
            print ("You are very close")        
        
        n= n+1

guess_number()

print ("You are out of tries")                



