# Level №1 - Even number

import random

from brain_games.cli import welcome_user
name = welcome_user()

def brain_even():
    print('What is the result of the expression?')
    count = 0

    while count < 3:
        random_num1 = random.randint(1, 30)
        random_num2 = random.randint(1, 30)
        rand_ops = ['+', '-', '*']
        expression = str(random_num1) + random.choice(rand_ops) + str(random_num2)
        print("Question: " + str(expression))
        expression = eval(expression)
        user_input = input("Your answer: ")

        if int(user_input) == expression:
            print('Correct!')
            count += 1
        else:
            print(f"\'{user_input}\' is wrong answer;(. Correct answer was {expression}.")
            print("Let's try again, " + name)
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
        
brain_even()     

def main():
    if __name__ == '__main__':
        main()



