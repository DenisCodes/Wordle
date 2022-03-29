import random
from termcolor import colored, cprint

#if the console being used supports ansi this will work otherwise it will print weird text
#change the variable bellow to true if the console doesn't support ansi
ansi = False

response = ['white', 'white', 'white', 'white', 'white']
#go = True
guess_num = 0

def list_maker(word):
    """
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('running list_maker...')
    print('from: ')
    print(word)
    """
    new_list = []
    for letter in word:
        new_list.append(letter)
        """
    print(new_list)
    print('to: ')
    print(new_list)
    """
    return new_list


def print_color(quess,colors):
    if ansi:
        position = 0
        """
        print(quess)
        print(str(len(quess)))
        print(str(len(colors)))
        print (colors)
        print('good')
        """
        """
        for position in range(len(quess)):
            #print(colors[position])
            #print(quess[position])
            print ('this' + str(position))
            print(str(quess[position]))
            #cprint(quess[position], colors[position], end='')
        for color in colors: 
            print(color)
            cprint(quess[position], color, end='') 
            #print(colored(letter, colors[position]), end="")
            position += 1
        """
        for letter in quess: 
            #print(letter)
            cprint(letter, colors[position], end='') 
            #print(colored(letter, colors[position]), end="")
            position += 1
        print('')
    #if the console being used supports ansi this will work otherwise it will print weird text
    #change the variable ansi on line 4 to False if your console doesn't support ansi
    else:
        output = ''
        for block in colors:
            if block == 'white':
                output = output + 'black' + " "
            else:
                output = output + block + " "
        print(output)
            

def length_checker(guess):
    """
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('running length_checker...')
    """
    if len(guess) == 5:
        """
        print('guess: ' + guess)
        print('guess length is: ' + str(len(guess)))
        print('accepted')
        """
        return guess  
    else: 
        print('The word you entered does not contain five letters... try again :)')
        guesses = input('Guess a FIVE letter word: ').lower()
        """
        print('guess: ' + guesses)
        print('guess length is: ' + str(len(guesses)))
        print('denied')
        """
        return length_checker(guesses)
    

def try_again(guessnum):
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #print('running try_again...')
    
    if guessnum >= 6:
        print('You have run out of guesses')
        #response = False
    else:
        guess_rem = 6 - guessnum 
        print('Guesses remaining: ' + str(guess_rem))
        guess = input('Guess a five letter word: ').lower()
        #print(guess)
        return guess


def checker(answer,guess,guessnum):
    """
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('running checker...')
    """
    global guess_num
    response = ['white', 'white', 'white', 'white', 'white']
    correct = ['green', 'green', 'green', 'green','green']
    #print('checker4')
    """
    print("answer: " + str(answer))
    print("guess: " + str(guess))
    """
    answer_ = list_maker(answer)
    guess_ = list_maker(guess)
    #print('checker3')
    position = 0
    for letter in guess_:
        if letter in answer_:
            #print(letter)
            response[position] = 'yellow'
            #print(response)
        position += 1
    position = 0
    for letter in guess_:
        if letter == answer_[position]:
            #print(letter)
            #print(response)
            response[position] = 'green' 
        position += 1
    if response == correct:
        print_color(guess_,response)
        print('Correct, the word was ' + guess)
        #print(response)
        #response = False
        guess_num = 69
        #print(guess_num)
    else:
        print_color(guess_,response)
        #print(guess + 'is not correct')
        guess_num += 1
        #print('result')





w = open('words.txt', 'r')
words = []
for word in w:
    words.append(word)
w.close()

answer = random.choice(words).strip().lower()
#print(answer)

while guess_num < 6:
    """
    print("new loop info: ")
    print(guess_num)
    print(response)
    """
    checker(answer,length_checker(try_again(guess_num)),guess_num)
if guess_num == 69:
    print('Well done')
else:
    print('You have run out of guesses')
    print('The word was: '+ answer)
    print('Try again next time')
