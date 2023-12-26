# Level №1 - Even number

import random

from brain_games.scripts.brain_games import main

name = str(main())

def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        random_num = random.randint(1, 100)
        print("Question: " + str(random_num))
        user_input = input("Your answer: ")

        if ((random_num % 2 == 0 and user_input == 'yes')
                or (random_num % 2 != 0 and user_input == 'no')):
            print('Correct!')
            count += 1
        else:
            print(f"\'{user_input}\' is wrong answer;(. Correct answer was "
                  f"{'yes' if random_num % 2 == 0 else 'no'}.")
            print("Let's try again, " + name)
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
