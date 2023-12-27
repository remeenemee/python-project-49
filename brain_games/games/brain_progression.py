# Level №4 - Geometric_progression

import random

from brain_games.cli import welcome_user

print("Welcome to the Brain Games!")
name = welcome_user()


def brain_progression():
    print('What number is missing in the progression?')
    count = 0

    while count < 3:
        random_num1 = random.randint(1, 100)
        random_num2 = random_num1 + 20
        random_step = random.randint(2, 4)
        if random_num1 > random_num2:
            random_num1, random_num2 = random_num2, random_num1
        list_nums = [*range(random_num1, random_num2, random_step)]
        random_index = random.choice(range(len(list_nums)))
        result = str(list_nums[random_index])
        list_nums[random_index] = '..'
        list_nums = ' '.join(str(num) for num in list_nums)
        print("Question: " + list_nums)
        user_input = input("Your answer: ")

        if user_input == result:
            print('Correct!')
            count += 1
        else:
            print(f"\'{user_input}\' is wrong answer;(. "
                  f"Correct answer was {result}.")
            print("Let's try again, " + name + '!')
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
