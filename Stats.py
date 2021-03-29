from Globals import *


def stats_rec():
    '''
    Записывает в файл статистику (food, happy, sleep, time,name)

    Если закрыть игру, то сохраняет в файл статистику, если кот не мертв

    Если кот умирает, то очищает файл и флаг isempty изменяется значение на True
    для запуска стартового меню

    При запуске игры, если в файле есть статистика кота, то isempty остается False
    в таком случае стартовое меню не запускается, а запускается основное игровое окно
    '''

    stats = open("stats.txt", "r")
    n_time = time.time()
    stati = {'time': '', 'food': '', 'sleep': '', 'happy': '', 'name': ''}

    for i, line in enumerate(list(stats.readlines())):
        stati[list(stati.keys())[i]] = line

    if stati['time'] == '':
        MyGlobals.isempty = True
        stati['time'] = time.time()
    if stati['food'] == '':
        MyGlobals.isempty = True
        stati['food'] = "100"
    if stati['sleep'] == '':
        MyGlobals.isempty = True
        stati['sleep'] = '100'
    if stati['happy'] == '':
        MyGlobals.isempty = True
        stati['happy'] = '100'
    if stati['name'] == '':
        MyGlobals.isempty = True
        stati['name'] = 'NoName'

    time_loss = n_time - float(stati['time'])

    food_loss = time_loss // 10
    sleep_loss = time_loss // 20

    MyGlobals.cat.set_hunger(int(stati['food']))
    MyGlobals.cat.set_sleep(int(stati['sleep']))
    MyGlobals.cat.set_happiness(int(stati['happy']))
    MyGlobals.cat.set_hunger(max(6, MyGlobals.cat.pet_hunger - food_loss))
    MyGlobals.cat.set_sleep(max(6, MyGlobals.cat.pet_sleep - sleep_loss))
    MyGlobals.cat.set_happiness(max(6, MyGlobals.cat.pet_happiness - sleep_loss - food_loss))
    MyGlobals.cat.set_name(stati['name'])
