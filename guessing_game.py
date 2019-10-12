
from random import randint

def get_boundaries(past_guesses, answer):
    '''
    This function takes a list of past guesses and the answer value
    Sorts the list and returns the value to the left and right of the 
    answers index
    '''
    past_guesses.sort()
    idx = past_guesses.index(answer)
    lower,upper = past_guesses[idx - 1], past_guesses[idx + 1]
    
    if lower < 1:
        lower = 1
        
    if upper > 100:
        upper = 100
        
    return f'The number is between {lower} and {upper}'

def get_guess():
    '''
    This function takes no input
    get string input from the player, checks that it is an integer between 0 and 101
    and not other invalid inputs
    and returns a valid guess
    '''
    guess = input('What is your guess? ')

    while not (guess.isdigit() and int(guess) >= 1 and int(guess) <= 100):
        print('your guess must be a whole number between 1 and 100')
        guess = input('What is your guess? ')

    return int(guess)
    

def give_feedback(guess, answer):
    '''
    this function takes a value of guess and a value of answer
    determines the correct feedback
    and returns the feedback string
    '''
    if answer == guess:
        return ''
    if answer > guess:
        return "The answer is higher than that"
    else:
        return "The answer is lower than that"
    

print('I\'m going to think of a number between 1 and 100')
answer = randint(1,100)

past_guesses = [0,101,answer]

guess = ''

while answer != guess:
    guess = get_guess()
    past_guesses.append(guess)
    
    print(give_feedback(guess, answer))
    
    if answer == guess:
        break
    
    print(get_boundaries(past_guesses, answer))
    

print('Congratulations you win!')
