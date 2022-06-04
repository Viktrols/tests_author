import pytest
import re

# здесь должен быть импорт Решения студента
import author as user_module
# импорт строк, которые предоставляет платформа (для проверки работы тестов я создала temp.py
# с такими строками)
from temp import user_code, output 


# Тестирование модуля
class TestUserModule():
    def test_class_exists(self):
        try:
            from author import Contact
        except ImportError:
            assert False, 'Убедитесь, что класс Contact cуществует (проверьте нет ли опечаток)'
    def test_func_not_exists(self):
        try:
            from author import print_contact
        except ImportError:
            assert True, 'Убедитесь, что удалили функцию print_contact'
    
    def test_methods_exist(self):
        assert '__init__' in user_module.Contact.__dict__ , 'Проверьте, что вы не удалили метод __init__ в классе Contact'
        assert 'show_contact' in user_module.Contact.__dict__ , (
            'Убедитесь, что метод show_contact cуществует (проверьте нет ли опечаток)'
        )
    
    def test_objcets(self):
        try:
            from author import mike, vlad
        except ImportError:
            assert False, 'Убедитесь, что cоздали объекты mike и vlad'
        assert isinstance(user_module.mike, user_module.Contact), (
            'Убедитeсь что объект mike является экземпляром класса Сontact')
        assert isinstance(user_module.vlad, user_module.Contact), (
            'Убедитeсь что объект vlad является экземпляром класса Сontact'
        )
        parametres = ['name', 'phone', 'birthday', 'address']
        for param in parametres:
            assert hasattr(user_module.vlad, param) and hasattr(user_module.mike, param), (
                f'Проверьте, что вы не удалили необходимые параметры {parametres}'
                f'в классе и при создании объктов mike и vlad передали их'
            )

    def test_print_funcs_work(self, capsys):
        vlad = user_module.Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")
        user_module.vlad.show_contact()
        capture = capsys.readouterr()
        correct_output = [
        'Создаём новый контакт Владимир Маяковский',
        'Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893'
    ]
        problem1 = ('Убедитесь, что при создании экземпляра класса выводите'
                   '`Создаём новый контакт <name>`')
        problem2 = ('Убедитесь, что при вызове метода show_contact выводите'
                    'все параметры из прекода в нужном порядке')
        assert correct_output[0] in capture.out, problem1
        assert correct_output[1] in capture.out, problem2
        


# Тестирование строк user_code и output
# (если я правильно поняла условие, эти строки передаются платформой)
def test_student_code():
    patterns = {
    r'class Contact' : 'Проверьте, что создали класс Contact',
    r'def __init__' : 'Проверьте, что вы не удалили метод __init__ в классе Contact',
    r'print\(f"Создаём новый контакт {name}"\)': 'Проверьте, что вы не удалили print из метода __init__ в классе Contact',
    r'def show_contact\(self\)' : 'Убедитесь, что создали мeтод show_contact с параметром self',
    r'print\(f"{self\.name} — адрес: {self\.address}, телефон: {self\.phone}, день рождения: {self\.birthday}"\)':
     'Убедитесь, что в методе show_contact вы выводите строку из функции print_contact, заменив имя конкретного объекта на `self`',
    r'mike\s*=\s*Contact\("Михаил Булгаков",\s*"2-03-27",\s*"15\.05\.1891",\s*"Россия, Москва, Большая Пироговская, дом 35б, кв\. 6"\)':
     'Убедитесь, что создали экземпляр класса Contact mike с параметрами из прекода',
    r'vlad\s*=\s*Contact\("Владимир Маяковский",\s*"73-88",\s*"19\.07\.1893",\s*"Россия, Москва, Лубянский проезд, д\. 3, кв\. 12"\)':
     'Убедитесь, что создали экземпляр класса Contact vlad с параметрами из прекода',
    r'vlad\.show_contact\(\)':'Убедитесь, что вызвали метод show_contact для объекта vlad',
    r'mike\.show_contact\(\)':'Убедитесь, что вызвали метод show_contact для объекта mike'
}
    for key in patterns:
        assert re.findall(f'{key}', user_code) != [], patterns[key]
    
    assert re.findall(r'def print_contact', user_code) == [], 'Убедитесь, что удалили функцию print_contact'

def test_student_output():
    correct_output = [
        'Создаём новый контакт Михаил Булгаков',
        'Создаём новый контакт Владимир Маяковский',
        'Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891',
        'Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893'
    ]
    problem1 = ('Убедитесь, что при создании экземпляра класса выводите'
                '`Создаём новый контакт <name>`')
    problem2 = ('Убедитесь, что при вызове метода show_contact выводите'
                'все параметры из прекода в нужном порядке')
    assert correct_output[0] in output, problem1
    assert correct_output[1] in output, problem1
    assert correct_output[2] in output, problem2
    assert correct_output[3] in output, problem2
