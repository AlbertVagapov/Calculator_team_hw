import constants
import logger_1_r_c
import rational
import user_interface
import func_comp_1
import print_result


def click_button():
    choice = user_interface.start_menu()
    logger_1_r_c.action_logger_head()
    c = float
    if choice == 1:
        action = user_interface.get_menu_rational()
        a, b = user_interface.get_arg()
        if action == 1:
            c = rational.sum(a, b)
            constants.data = [a, '0', '+', b, '0', c, '0']
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_rational(constants.data)
        elif action == 2:
            c = rational.sub(a, b)
            constants.data = [a, '0', '-', b, '0', c, '0']
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_rational(constants.data)
        elif action == 3:
            c = rational.mult(a, b)
            constants.data = [a, '0', '*', b, '0', c, '0']
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_rational(constants.data)
        elif action == 4:
            c = rational.div(a, b)
            constants.data = [a, '0', '/', b, '0', c, '0']
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_rational(constants.data)
        elif action == 5:
            c = rational.degree(a, b)
            constants.data = [a, '0', '**', b, '0', c, '0']
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_rational(constants.data)
        elif action == 6:
            c = rational.logarifm(a, b)
            constants.data = [a, '0', 'log', b, '0', c, '0']
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_rational(constants.data)
        elif action == 7:
            exit
        else:
            print(f'Введите значения из списка {len[constants.MENU_RATIONAL]}')
    elif choice == 2:
        action = user_interface.get_menu_complex()
        a_1, b_1, a_2, b_2 = user_interface.get_arg_complex()
        if action == 1:
            res_a, res_b = func_comp_1.sum_comp(a_1, b_1, a_2, b_2)
            constants.data = [a_1, b_1, '+', a_2, b_2, res_a, res_b]
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_comp(constants.data)
        elif action == 2:
            res_a, res_b = func_comp_1.subtraction_comp(a_1, b_1, a_2, b_2)
            constants.data = [a_1, b_1, '+', a_2, b_2, res_a, res_b]
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_comp(constants.data)
        elif action == 3:
            res_a, res_b = func_comp_1.multiplication_comp(a_1, b_1, a_2, b_2)
            constants.data = [a_1, b_1, '+', a_2, b_2, res_a, res_b]
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_comp(constants.data)
        elif action == 4:
            res_a, res_b = func_comp_1.division_comp(a_1, b_1, a_2, b_2)
            constants.data = [a_1, b_1, '+', a_2, b_2, res_a, res_b]
            logger_1_r_c.action_logger(constants.data)
            print_result.print_result_comp(constants.data)
        elif action == 5:
            exit
        else:
            print(f'Введите значения из списка {len[constants.MENU_COMPLEX]}')
    elif choice == 3:
        exit
    else:
        print(f'Введите значения из списка {len[constants.START_MENU]}')


if __name__ == '__main__':
    click_button()
