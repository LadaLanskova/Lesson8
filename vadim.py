import sys

from database import get_data, change_data


def print_job(x, date, a = None):
    if a is None:
        a = get_data(x)
    a.setdefault(date, ['', '', ''])
    return a[date]


def create_job(x, date, time, txt, a = None):
    if a is None:
        a = get_data(x)
    a.setdefault(date, ['', '', ''])
    a[date][time - 1] = txt
    change_data(x, a)
    return True


def delete_job(x, date, time, a = None):
    if a is None:
        a = get_data(x)
    a.setdefault(date, ['', '', ''])
    a[date][time - 1] = ''
    change_data(x, a)
    return True

def farewell(): # сообщение при завершении работы с программой
    print('Спасибо за пользование программой. До новых встреч!')

def unlog_sys(x, a = None):
#    if a is None:
#        a = get_data(x)
#        print(a)
    print('До свидания. Ждем Вас снова!\n')
#    a = None
    return True


def exit_sys():
    print('Спасибо за пользование программой! Ждем снова')
    sys.exit()