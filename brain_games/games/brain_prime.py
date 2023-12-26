# Level №5 - Prime number

import random

from brain_games.cli import welcome_user

print("Welcome to the Brain Games!")
name = welcome_user()


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def brain_prime():
    print('"yes" if given number is prime. Otherwise answer "no"')
    count = 0

    while count < 3:
        random_num = random.choice(range(1, 50, 3))
        print("Question:", random_num)
        user_input = input("Your answer: ").lower()

        if ((is_prime(random_num) and user_input == 'yes')
                or (not is_prime(random_num) and user_input == 'no')):
            print('Correct!')
            count += 1
        else:
            correct_answer = 'yes' if is_prime(random_num) else 'no'
            print(f"'{user_input}' is wrong answer;(. "
                  f"Correct answer was {correct_answer}.")
            print("Let's try again, " + name + '!')
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
