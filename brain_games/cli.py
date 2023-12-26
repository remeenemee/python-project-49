import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    result = (name, )
    print('Hello, ' + name + "!")
    return result[0]
