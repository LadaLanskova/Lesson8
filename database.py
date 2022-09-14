DIC_LOGIN = \
    {
        1: ('Konstantin', 'konstantin.txt'),
        2: ('Lada', 'lada.txt'),
        3: ('Vadim', 'vadim.txt'),
        4: ('Sergey', 'sergey.txt')
    }


def get_data(login):
    readed_data = []
    with open(DIC_LOGIN[login][1], mode='r', encoding='utf-8') as data:
        for line in data:
            readed_data.append(line.replace('\n', ''))
    data = list(map(lambda d: d.split('|'), readed_data))
    down_data = {}
    for i in data:
        down_data[i[0]] = i[1:]
    return down_data


def change_data(login, dict_data):
    uploaded_list = [f'{key}|{"|".join(dict_data[key])}' for key in dict_data]
    uploaded_str = '\n'.join(uploaded_list)
    with open(DIC_LOGIN[login][1], mode='w', encoding='utf-8') as data:
        data.write(uploaded_str)
    return True
