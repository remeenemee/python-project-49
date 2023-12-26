# Level №3 - Greatest common divisor

import random
import math

from brain_games.cli import welcome_user

print("Welcome to the Brain Games!")
name = welcome_user()


def brain_gcd():
    print('Find the greatest common divisor of given numbers')
    count = 0

    while count < 3:
        random_num1 = random.randint(1, 30)
        random_num2 = random.randint(1, 30)
        expression = math.gcd(random_num1, random_num2)
        print("Question: " + str(random_num1) + " " + str(random_num2))
        user_input = input("Your answer: ")

        if int(user_input) == expression:
            print('Correct!')
            count += 1
        else:
            print(f"\'{user_input}\' is wrong answer;(. "
                  f"Correct answer was {expression}.")
            print("Let's try again, " + name + '!')
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
