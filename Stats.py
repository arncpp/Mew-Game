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
    stats = {"time": "", "food": "", "sleep": "", "happy": "",
             "health": "", "name": ""}

    try:
        with open("stats.txt", "r") as stats_file:
            for i, line in enumerate(list(stats_file.readlines())):
                stats[list(stats.keys())[i]] = line
            stats_file.close()
    except IOError:
        open("stats.txt", "w").close()

    if stats["time"] == "":
        MyGlobals.isempty = True
        stats["time"] = time.time()
    if stats["food"] == "":
        MyGlobals.isempty = True
        stats["food"] = MyGlobals.cat_max_stats
    if stats["sleep"] == "":
        MyGlobals.isempty = True
        stats["sleep"] = MyGlobals.cat_max_stats
    if stats["happy"] == "":
        MyGlobals.isempty = True
        stats["happy"] = MyGlobals.cat_max_stats
    if stats["health"] == "":
        MyGlobals.isempty = True
        stats["health"] = MyGlobals.cat_max_stats
    if stats["name"] == "":
        MyGlobals.isempty = True
        stats["name"] = MyGlobals.default_cat_name

    time_loss = n_time - float(stats["time"])
    food_loss = time_loss // 10
    sleep_loss = time_loss // 20
    health_loss = time_loss // 18
    MyGlobals.cat.set_hunger(int(stats["food"]))
    MyGlobals.cat.set_sleep(int(stats["sleep"]))
    MyGlobals.cat.set_happiness(int(stats["happy"]))
    MyGlobals.cat.set_health(int(stats["health"]))
    MyGlobals.cat.set_hunger(
        max(6, MyGlobals.cat.get_pet_hunger() - food_loss))
    MyGlobals.cat.set_sleep(max(6, MyGlobals.cat.get_pet_sleep() - sleep_loss))
    MyGlobals.cat.set_happiness(
        max(6, MyGlobals.cat.get_pet_happiness() - sleep_loss))
    MyGlobals.cat.set_health(
        max(6, MyGlobals.cat.get_pet_health() - health_loss))
    MyGlobals.cat.set_name(stats["name"])
