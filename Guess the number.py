#Guess the number :
#It's a game,
#where computer will generate a number for us and we have to guess it correctly.

import random # inbuilt module in python used to guess numbers in certain range.

def guess(x): # user define function.
    random_number = random.randint(1,x) # random.randint(1,x) it ranges from 1 to x = user's input number.
    guess = 0
    while guess != random_number: # the while loop will be executed until user's guessed number and random_number is same.
        guess = int(input(f"Guess the number between 1 to {x}: ")) # user's guessed number.
        if guess < random_number:
            print("hey, number you guessed is bit low")
        elif guess > random_number:
            print("hey, number you guessed is bit high")
    print(f'yay,congrats.you have guessed the number {random_number} correctly')

guess(int(input()))

print("-------------------------------------------------------------------------------------------------------------")

# here, computer guess's our number.
def computer_guess(x):
    low = 1 # setting boundaries as low and high.
    high = x # x value will be user's input value passed in the computer_guess().
    feedback = ''
    while feedback != 'c': #loop will get executed untill feedback == c.
        # first we have to check whether low and high are equal or not.
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could be high because low = high
        feedback = input(f"Is {guess} too high (H),too low(l),or correct (c)").lower() #user input h as too high, l as too low,c as in correct.
        if feedback == 'h':
            high = guess - 1 # if the high limit is more than the guessed number then we decrease the high limit, because guess number can't be more than high.
        elif feedback == 'l':
            low = guess + 1 # if the low limit is less than the guessed number than we increase the value of low.
    print(f'yay! The computer guessed the number,{guess}, correctly')

computer_guess(int(input()))