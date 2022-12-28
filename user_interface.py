from constants import START_MENU, MENU_COMPLEX, MENU_RATIONAL
from checks import give_int
choose_option = 'Выберите действие из списка:\n'


def start_menu() -> int:
    """
    Выбор вида чисел(рациональное или комплексное)
    Returns:
       choice: Выбор пользователя -> int
    """
    for i, item in list(enumerate(START_MENU, start=1)):
        print(i, item, end='\n')
    choice = give_int(choose_option, 1, 3)
    return choice


def get_menu_rational() -> int:
    """
    Функция выводит все возможные действия с рациональными числами
    Returns:
       choice: Выбор пользователя -> int
    """
    for i, item in list(enumerate(MENU_RATIONAL, start=1)):
        print(i, item, end='\n')
    choice = give_int(choose_option, 1, 7)
    return choice


def get_menu_complex() -> int:
    """
    Функция выводит все возможные действия с комплексными числами
    Returns:
       choice: Выбор пользователя -> int
    """
    for i, item in list(enumerate(MENU_COMPLEX, start=1)):
        print(i, item, end='\n')
    choice = give_int(choose_option, 1, 5)
    return choice


def get_arg() -> float:
    '''
    Принимает от пользователя аргументы
    '''
    a = float(input('Введите первый аргумент\n'))
    b = float(input('Введите второй аргумент\n'))
    return a, b


def get_arg_complex() -> float:
    '''
    Принимает от пользователя аргументы
    '''
    a_1 = float(input('Введите действительную часть первого числа\n'))
    b_1 = float(input('Введите действительную часть первого числа\n'))
    a_2 = float(input('Введите действительную часть второго числа\n'))
    b_2 = float(input('Введите действительную часть второго числа\n'))
    return a_1, b_1, a_2, b_2


if __name__ == '__main__':
    choice = start_menu()
    if choice == 1:
        a, b = get_arg()
        get_menu_rational()
    elif choice == 2:
        # здесь должна быть проверка на комплексное число
        get_menu_complex
