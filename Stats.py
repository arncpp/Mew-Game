from Globals import MyGlobals
import time


def stats_rec():
    """
    Записывает в файл статистику (food, happy, sleep, time,name)
    Если закрыть игру, то сохраняет в файл статистику, если кот не мертв
    Если кот умирает, то очищает файл и флаг isempty изменяется
    значение на True для запуска стартового меню
    При запуске игры, если в файле есть статистика кота, то isempty
    остается False
    в таком случае стартовое меню не запускается, а запускается основное
    игровое окно
    """
    n_time = time.time()
    stats = {MyGlobals.stat_time: "", MyGlobals.stat_food: "",
             MyGlobals.stat_sleep: "", MyGlobals.stat_happy: "",
             MyGlobals.stat_health: "", MyGlobals.stat_name: ""}
    try:
        with open(MyGlobals.stats_file_name, "r") as stats_file:
            for i, line in enumerate(list(stats_file.readlines())):
                stats[list(stats.keys())[i]] = line
    except Exception:
        open(MyGlobals.stats_file_name, "w").close()

    if stats[MyGlobals.stat_time] == "":
        MyGlobals.isempty = True
        stats[MyGlobals.stat_time] = time.time()
    if stats[MyGlobals.stat_food] == "":
        MyGlobals.isempty = True
        stats[MyGlobals.stat_food] = MyGlobals.cat_max_stats
    if stats[MyGlobals.stat_sleep] == "":
        MyGlobals.isempty = True
        stats[MyGlobals.stat_sleep] = MyGlobals.cat_max_stats
    if stats[MyGlobals.stat_happy] == "":
        MyGlobals.isempty = True
        stats[MyGlobals.stat_happy] = MyGlobals.cat_max_stats
    if stats[MyGlobals.stat_health] == "":
        MyGlobals.isempty = True
        stats[MyGlobals.stat_health] = MyGlobals.cat_max_stats
    if stats[MyGlobals.stat_name] == "":
        MyGlobals.isempty = True
        stats[MyGlobals.stat_name] = MyGlobals.default_cat_name

    time_loss = n_time - float(stats[MyGlobals.stat_time])
    food_loss = time_loss // MyGlobals.stats_loss_divider
    sleep_loss = (time_loss // MyGlobals.stats_loss_divider *
                  MyGlobals.sleep_loss_mult)
    health_loss = (time_loss // MyGlobals.stats_loss_divider *
                   MyGlobals.health_loss_mult)
    MyGlobals.cat.set_hunger(int(stats[MyGlobals.stat_food]))
    MyGlobals.cat.set_sleep(int(stats[MyGlobals.stat_sleep]))
    MyGlobals.cat.set_happiness(int(stats[MyGlobals.stat_happy]))
    MyGlobals.cat.set_health(int(stats[MyGlobals.stat_health]))
    MyGlobals.cat.set_hunger(
        max(MyGlobals.min_stats, MyGlobals.cat.get_pet_hunger() - food_loss))
    MyGlobals.cat.set_sleep(
        max(MyGlobals.min_stats, MyGlobals.cat.get_pet_sleep() - sleep_loss))
    MyGlobals.cat.set_happiness(
        max(MyGlobals.min_stats,
            MyGlobals.cat.get_pet_happiness() - sleep_loss))
    MyGlobals.cat.set_health(
        max(MyGlobals.min_stats, MyGlobals.cat.get_pet_health() - health_loss))
    MyGlobals.cat.set_name(stats[MyGlobals.stat_name])
