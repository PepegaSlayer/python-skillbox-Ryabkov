def ask_question(question):
    answer = input(question)
    print('А у меня не очень!')


def test():
    print('Функция 0')


def test1():
    print('Функция 1')


def test2():
    print('Функция 2')


def how_are_you():
    ask_question('Как дела? ')


def modified_test():
    how_are_you()
    test()


def modified_test1():
    how_are_you()
    test1()


def modified_test2():
    how_are_you()
    test2()


modified_test()
modified_test1()
modified_test2()