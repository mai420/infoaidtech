
import random

def rules():
    print("Welcome to number guessing game!")
    print('Goal is to guess the number I have thought of')
    print('You will have 10 chances to do so and I might think of a number between 1 to 100')
    print('Hints will be provided. Lets see how many attempts will you take to guess the number! ')

def guess():
    
    x = random.randint(0,100)
    for i in range(10):
        y = int(input('enter a number: '))
        if x == y:
            print('correct!')
            break
        else:
            difference = abs(x - y)

            if difference > 20:
                print('u are very far')
            elif 10 <= difference < 20:
                print('you are very close try once more')
            else:
                print('extemely close')
    print('the number was: ' + str(x))
    print('your number was: ' + str(y))



def numberguessinggame():
    name = input('enter your name: ')
    print('hello ' + name  )
    guess()

numberguessinggame()

game = input('do u wonna play again? (Y/N): ')
while game.lower() == 'y':
    guess()
    game = input('do u wonna play again? (Y/N): ')

print('thank u for playing! ')
