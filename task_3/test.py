import time
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
            from author import time_check, long_heavy
        except ImportError:
            assert False, 'Убедитесь, что не удалили функции time_check  и long_heavy из прекода'
        try:
            from author import cache_args
        except ImportError:
            assert False, 'Убедитесь, что cоздали функцию cache_args'
    
    def test_long_heavy(self):
        test_res = user_module.long_heavy(7)
        assert test_res == 14, 'Убедитесь, что не меняли функцию long_heavy из прекода'
        start_time = time.time()
        user_module.long_heavy(10)
        execution_time = round(time.time() - start_time, 1)
        assert execution_time == 1, (
            'Убедитесь, что над функцией long_heavy есть декоратор @time_check'
        )
        start_time2 = time.time()
        user_module.long_heavy(10)
        execution_time2 = round(time.time() - start_time2, 1)
        assert execution_time2 == 0, (
            'Убедитесь, что над функцией long_heavy есть декоратор @cache_args,'
            'а функция cache_args кеширует данные'
        )

    def test_print_funcs_work(self, capsys):
        print(user_module.long_heavy(11))
        correct_output = ['Время выполнения функции: 1.0 с', '22']
        capture = capsys.readouterr()
        assert correct_output[0] in capture.out, (
            'Убедитесь, что не удаляли print из функции time_check')
        assert correct_output[1] in capture.out, (
            'Проверьте, что не меняли функцию long_heavy из прекода')


# Тестирование строк user_code и output
# (если я правильно поняла условие, эти строки передаются платформой)
def test_student_code():
    patterns = {
        r'def time_check': 'Убедитесь, что не удалили функции time_check',
        r'def long_heavy': 'Убедитесь, что не удалили функции long_heavy',
        r'def cache_args': 'Убедитесь, что cоздали функцию cache_args',
        r'@cache_args': 'Убедитесь, что над функцией long_heavy есть декоратор @cache_args',
        r'@time_check': 'Убедитесь, что над функцией long_heavy есть декоратор @time_check',
        r'\w\s*=\s*({}|dict\(\))': 'Используйте для кеширования результатов словарь',
        r'if \s*\S+\s+in':
         'Убедитесь, что декоратор проверяет вызывается ли функция повторно, для этого подойдет конструкция if...in',
        r'(else|elif)':
         'Убедитесь, что декоратор записывает данные в словарь, если ранее они не кешировались'
    }
    for key in patterns:
        assert re.findall(f'{key}', user_code) != [], patterns[key]

    assert len(re.findall('return', user_code)) == 6, (
        'Проверьте, что ваша функция-декоратор возвращает результат '
        'и декорируемую функцию (можете подсмотреть как это происходит в time_check)'
    )

def test_student_output():
    correct_output = (
'''
Время выполнения функции: 1.0 с.
2
Время выполнения функции: 0.0 с.
2
Время выполнения функции: 1.0 с.
4
Время выполнения функции: 0.0 с.
4
Время выполнения функции: 0.0 с.
4
'''
)
    problem = 'Убедитесь, что не меняли порядок вызовов функций в прекоде'
    assert output == correct_output, problem
  