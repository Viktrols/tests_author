import pytest
import re

# здесь должен быть импорт Решения студента
import author as user_module
# импорт строк, которые предоставляет платформа (для проверки работы тестов я создала temp.py
# с такими строками)
from temp import user_code, output


# Тестирование модуля
class TestUserModule():
    def test_func_exist(self):
        try:
            from author import make_divider_of
        except ImportError:
            assert False, 'Убедитесь, что функция make_divider_of cуществует'
        try:
            from author import div2, div5
        except ImportError:
            assert False, (
                'Убедитесь, что вы не удалили создание функций div2 и duv5 из прекода'
            )
    
    def test_make_divider_of(self):
        test_func = user_module.make_divider_of(3)
        test_res = test_func(90)
        assert test_res == 90/3, (
            'Функция работает не правильно. Проверьте что на основе make_divider_of'
            'можно создавать производные функции, делящие переданный аргумент на определённое число.'
            'Убедитесь, что функция делит divisible на divider и возвращает результат')

    def test_print_funcs_work(self, capsys):
        div5 = user_module.make_divider_of(5)
        print(div5(50))
        capture = capsys.readouterr()
        assert '10.0' in capture.out , (
            'Убедитесь, что функция делит divisible на divider и возвращает результат')


# Тестирование строк user_code и output
# (если я правильно поняла условие, эти строки передаются платформой)
def test_student_code():
    patterns = {
        r'def make_divider_of\(divider\)':
         'Проверьте, что функция make_divider_of с аргументом divider существует',
        r'def division_operation\(divisible\)': 
         'Проверьте, что функция division_operation с аргументом divisible существует',
        r'def make_divider_of\(divider\):\s+def division_operation\(divisible\)':
         'Убедитесь, что функция division_operation вложена в функцию make_divider_of ',
    }
    for key in patterns:
        assert re.findall(f'{key}', user_code) != [], patterns[key]
    
    assert len(re.findall('return', user_code)) == 2, (
        'Проверьте, что ваша функция возвращает результат деления и функцию division_operation')


def test_student_output():
    correct_output = (
'''
5.0
4.0
2.0
'''
)
    assert output == correct_output, (
        'Убедитесь, что не меняли порядок вызовов функций в прекоде'
    )
