from datetime import datetime
from vadim import create_job, delete_job, print_job, unlog_sys, exit_sys


def login():
    ok = False
    print('Добрый день! Необходимо залогиниться.')
    print('Представьтесь пожалуйста, кто Вы?')
    print(f'{names}\n')
    while not ok:
        l = input('Введите число от 1 до 4: ')
        if l.isdigit() and 1 <= int(l) <= 4:
            ok = True
        else:
            print('Вы ошиблись!')
    return l


def inp_date():
    ok = False
    while not ok:
        d = input('Введите дату в формате 01.01.2000: ')
        format = "%d.%m.%Y"
        try:
            ok =bool(datetime.strptime(d, format))
        except ValueError:
            print('Вы ошиблись!')
    return d


def inp_period():
    ok = False
    print('Выберите период времени')
    print(f'{period}')
    while not ok:
        t = input('Введите число от 1 до 3: ')
        if t.isdigit() and 1 <= int(t) <= 3:
            ok = True
        else:
            print('Вы ошиблись!')
    return t


def inp_menu():
    ok = False
    print('Что Вы хотите сделать? ')
    print(f'{menu}\n')
    while not ok:
        l = input("Введите число от 1 до 5: ")
        if l.isdigit() and 1 <= int(l) <= 5:
            ok = True
        else:
            print("Вы ошиблись!")
    return l


def inp_txt():
    return input('Опишите суть дела: ')


names = ("1. Константин 2. Лада 3. Вадим 4. Сергей")
menu = ('1. Создать дело 2. Удалить дело 3. Вывести все дела 4. Разлогиниться 5. Завершить работу программы')
period = ('1. Утро 2. День 3. Вечер')


close = False
while not close:
    name_kode = int(login())

    while True:
        menu_kode = int(inp_menu())
        match menu_kode:
            case 1:
                date = inp_date()
                time_kode = int(inp_period())
                text_delo = inp_txt()
                Flag1 = create_job(name_kode, date, time_kode, text_delo)
                if Flag1:
                    print('Дело успешно создано \n')
            case 2:
               date = inp_date()
               time_kode = int(inp_period())
               Flag2 = delete_job(name_kode, date, time_kode)
               if Flag2:
                   print('Дело успешно удалено \n')
            case 3:
               date = inp_date()
               print(print_job(name_kode, date))
            case 4:
                unlog_sys(name_kode)
                break
            case 5:
                exit_sys()
