# Level №1 - Even number

import random

from brain_games.cli import welcome_user
name = welcome_user()

def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        random_num = random.randint(1, 100)
        print("Question: " + str(random_num))
        user_input = input("Your answer: ")

        if (random_num % 2 == 0 and user_input == 'yes') or (random_num % 2 != 0 and user_input == 'no'):
            print('Correct!')
            count += 1
        else:
            print(f"\'{user_input}\' is wrong answer;(. Correct answer was {'yes' if random_num % 2 == 0 else 'no'}.")
            print("Let's try again, " + name)
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
        
brain_even()     

def main():
    if __name__ == '__main__':
        main()



