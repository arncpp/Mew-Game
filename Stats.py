from Globals import MyGlobals
import time


def stats_rec():
    '''
    Записывает в файл статистику (food, happy, sleep, time,name)

    Если закрыть игру, то сохраняет в файл статистику, если кот не мертв

    Если кот умирает, то очищает файл и флаг isempty изменяется
    значение на True для запуска стартового меню

    При запуске игры, если в файле есть статистика кота, то isempty
    остается False
    в таком случае стартовое меню не запускается, а запускается основное
    игровое окно
    '''
    n_time = time.time()
    stati = {"time": "", "food": "", "sleep": "", "happy": "",
             "health": "", "name": ""}
    try:
        with open("stats.txt", "r") as stats:
            for i, line in enumerate(list(stats.readlines())):
                stati[list(stati.keys())[i]] = line
            stats.close()
    except IOError:
        open("stats.txt", "w").close()
    if stati["time"] == "":
        MyGlobals.isempty = True
        stati["time"] = time.time()
    if stati["food"] == "":
        MyGlobals.isempty = True
        stati["food"] = "100"
    if stati["sleep"] == "":
        MyGlobals.isempty = True
        stati["sleep"] = "100"
    if stati["happy"] == "":
        MyGlobals.isempty = True
        stati["happy"] = "100"
    if stati["health"] == "":
        MyGlobals.isempty = True
        stati["health"] = "100"
    if stati["name"] == "":
        MyGlobals.isempty = True
        stati["name"] = "NoName"
    time_loss = n_time - float(stati["time"])
    food_loss = time_loss // 10
    sleep_loss = time_loss // 20
    health_loss = time_loss // 18
    MyGlobals.cat.set_hunger(int(stati["food"]))
    MyGlobals.cat.set_sleep(int(stati["sleep"]))
    MyGlobals.cat.set_happiness(int(stati["happy"]))
    MyGlobals.cat.set_health(int(stati["health"]))
    MyGlobals.cat.set_hunger(max(6, MyGlobals.cat.get_pet_hunger() - food_loss))
    MyGlobals.cat.set_sleep(max(6, MyGlobals.cat.get_pet_sleep() - sleep_loss))
    MyGlobals.cat.set_happiness(
        max(6, MyGlobals.cat.get_pet_happiness() - sleep_loss))
    MyGlobals.cat.set_health(max(6, MyGlobals.cat.get_pet_health() - health_loss))
    MyGlobals.cat.set_name(stati["name"])
