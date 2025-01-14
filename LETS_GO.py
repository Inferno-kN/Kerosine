import time
import health
import json
from GUI import gui


data_game = {"health_player >>": 100, "inventory >>": ["Зажигалка", "Бутылка керосина"]}


def game_save(save):
    with open(save, 'w') as file:
        json.dump(data_game, file)
    print("Игра сохранена.")


def game_load(save):
    global data_game
    try:
        with open(save, 'r') as file:
            data_game = json.load(file)
        print("Игра загружена.")
        return True
    except FileNotFoundError:
        print("Файл не найден.")
        return False


def menu():
    while True:
        gui.print_info_message("menu")
        selection = input("Выберите опцию(введите название куда хотите перейти) >>")
        if selection.lower() == "начать игру":
            additional_menu()
        elif selection.lower() == "выход":
            print("Вы успешно вышли из игры!")
            break
        else:
            print("Произошла ошибка, проверьте верность ввода")


def additional_menu():
    T = game_load('add_save.json')
    if T:
        print("Продолжить")
    else:
        print("Сохранённой игры нет, начните новую игру")
        print("Новая игра")
        print("Назад")
    selection = input("Выберите опцию (введите название куда хотите перейти) >> ")
    if selection.lower() == "новая игра":
        start()
    elif selection.lower() == "продолжить" and T:
        print("Продолжение")
    elif selection.lower() == "назад":
        return
    else:
        print("Произошла ошибка, проверьте верность ввода")




def start():
    gui.print_info_message("hello")
    gui.print_info_message("input_name")
    Name_your_hero = gui.input_user_action()
    gui.hello_in_name(Name_your_hero)
    story = input()

    determination = input(Name_your_hero + " решает, что этой ночью надо сжечь машины."
" Вы вспоминаете, что у вас дома завалялась бутылка керосина и зажигалочка, да, та самая,"
" которую подарила ваша мама (нажмите Enter)")

    task = input("Твоя задача, " + Name_your_hero + ", выйти на улицу ночью, и пока соседи не видят,"
" поджечь их машины и скрыться, понял? (нажмите Enter)")

    print("Время на часах 00:00. Вы понимаете, что это время для того, чтобы выйти и сделать задуманное.")

    print("Вы выходите, но понимаете, что забыли дома бутылку керосина, и возвращаясь домой, Вы снова обдумываете делать ли вам это...")

    print("Наконец Вы собираетесь с мыслями, и действительно решаете, что это сделать необходимо.")

    print("Приходя домой, " + Name_your_hero + ", забирает бутылку керосина и кладёт к себе в инвентарь, где лежит ещё зажигалка.")

    print("Вы спустились вниз и уже готовитесь к нападению. Вас унижали 5 соседей, поэтому," + Name_your_hero + ", понимает, скольно нужно сжечь машин. ")

    players_data = {"hp_player":100,
                    "name": Name_your_hero,
                    "health_car1" : 100,  # Здоровье машины
                    "damage" : 10,
                    "count_burn_cars" : 0}

    result1 = attack_car1(players_data, "к первой")
    if not result1:
        return
    players_data["health_car1"] = 100

    result2 = attack_car1(players_data, "ко второй")
    if not result2:
        return

    players_data["health_car1"] = 100

    result3 = attack_car1(players_data, "к третьей")
    if not result3:
        return
    players_data["health_car1"] = 100

    result4 = attack_car1(players_data, "к четвертой")
    if not result4:
        return
    players_data["health_car1"] = 100

    result5 = attack_car1(players_data, "к пятой")
    if not result5:
        return
    players_data["health_car1"] = 100

    end(players_data)

def attack_car1(data, name_car) -> bool:
    print(f"Вы подошли {name_car} машине")

    flag = True
    while flag:
        selection = input("Вы хотите поджечь машину? Да или Нет >> ")
        if selection.lower() == "да":
            print("Вы подожгли машину! Осталось ждать 10 секунд и потом она сгорит.")
            distance_fire = input("Вы стоите близко к огню. Вы хотите отойти от машины или остаться на месте? Отойти или Остаться >> ")

            if distance_fire.lower() == "отойти":
                print("Вы отошли от машины и не получили урона от огня.")

            elif distance_fire.lower() == "остаться":
                print("Вы решили остаться рядом с горящей машиной и получили урон от огня!")
                data["hp_player"] -= 30

                if data["hp_player"] <= 0:
                    print("Вы умерли от ожогов! Соседи узнали что вы хотели поджечь их машины.")
                    print("Вы проиграли!")
                    time.sleep(3)
                    return False

                else:
                    print("Ваше здоровье =", data["hp_player"])
            else:
                print("Некорректный ввод. Вы автоматически отходите от машины.")

            for i in range(0, 10, 1):
                data["health_car1"] = data["health_car1"] - data["damage"]
                print("Здоровье машины = ", data["health_car1"])
                time.sleep(1)
            print("Машина успешно сгорела.")
            data["count_burn_cars"] += 1
            print("Количество сожжённых машин = ", data["count_burn_cars"])
            return True

        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return True

        else:
            print("Некорректный ввод, проверьте ввод")
            continue


def attack_car2(data):
    print("Вы подходите ко второй машине")

    flag = True
    while flag:
        selection = input("Вы хотите поджечь машину? Да или Нет >>")

        if selection.lower() == "да":
            print("Вы подожгли машину! Осталось ждать 10 секунд и потом она сгорит.")
            distance_fire = input("Вы стоите близко к огню. Вы хотите отойти от машины или остаться на месте? Отойти или Остаться >> ")

            if distance_fire.lower() == "отойти":
                print("Вы отошли от машины и не получили урона от огня.")

            elif distance_fire.lower() == "остаться":
                print("Вы решили остаться рядом с горящей машиной и получили урон от огня!")
                data["hp_player"] -= 30

                if data["hp_player"] <= 0:
                    print("Вы умерли от ожогов! Соседи узнали что вы хотели поджечь их машины.")
                    print("Вы проиграли!")
                    time.sleep(3)
                    return False

                else:
                    print("Ваше здоровье =", data["hp_player"])

            else:
                print("Проверьте корректность ввода")

            for i in range(0, 10, 1):
                data["health_car2"] -= data["damage"]
                print("Здоровье машины = ", data["health_car1"])
                time.sleep(1)

            print("Машина успешно сгорела")
            data["count_burn_cars"] += 1

            print("Количество сожжённых машин = ", data["count_burn_cars"])
            print("О нет! Сосед вышел, нужно что-то делать.")
            hide = input("Вы желаете спрятаться? Да или Нет >>")

            if hide.lower() == "да":
                print("Вы спрятались и сосед вас не заметил. Он ушёл звать на помощь.")
                return health_car2, health.hp_player, health.count_burn_cars
            elif hide.lower() == "нет":
                print("Вы не сумели спрятаться, сосед вас заметил. Игра проиграна!")
                print("Вы проиграли!")
                time.sleep(3)
                menu()
                return None, health.hp_player, health.count_burn_cars
            else:
                print("Проверьте корректность ввода")
                return attack_car2(health_car2, damage, inventory)
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return health_car2, health.hp_player, health.count_burn_cars
        else:
            print("Проверьте корректность ввода")
            return attack_car2(health_car2, damage, inventory)




def attack_car3(health_car3, damage, inventory):
    print("Вы подходите ко третьей машине")
    item1 = "Зажигалка"
    item2 = "Бутылка керосина"

    if item1 in inventory and item2 in inventory:
        selection = input("Вы хотите поджечь машину? Да или Нет >> ")
        if selection.lower() == "да":
            print("Вы подожгли машину! Осталось ждать 10 секунд и потом она сгорит.")
            distance_fire = input("Вы стоите близко к огню. Вы хотите отойти от машины или остаться на месте? Отойти или Остаться >> ")
            if distance_fire.lower() == "отойти":
                print("Вы отошли от машины и не получили урона от огня.")
            elif distance_fire.lower() == "остаться":
                print("Вы решили остаться рядом с горящей машиной и получили урон от огня!")
                health.hp_player -= 30
                if health.hp_player <= 0:
                    print("Вы умерли от ожогов! Соседи узнали что вы хотели поджечь их машины.")
                    print("Вы проиграли!")
                    time.sleep(3)
                    menu()
                    return None, health.hp_player
                else:
                    print("Ваше здоровье =", health.hp_player)
            else:
                print("Проверьте корректность ввода")

            for i in range(0, 10, 1):
                health_car3 = health_car3 - damage
                time.sleep(1)
            health_car3 = 0
            print("Машина успешно сгорела")
            health.count_burn_cars += 1
            print("Количество сожжённых машин = ", health.count_burn_cars)
            print("О нет! Сосед вышел, нужно что-то делать.")
            hide = input("Вы желаете спрятаться? Да или Нет >>")
            if hide.lower() == "да":
                print("Вы спрятались и сосед вас не заметил. Он ушёл звать на помощь.")
                return health_car3, health.hp_player, health.count_burn_cars
            elif hide.lower() == "нет":
                print("Вы не сумели спрятаться, сосед вас заметил. Игра проиграна!")
                print("Вы проиграли!")
                time.sleep(3)
                menu()
                return None, health.hp_player, health.count_burn_cars
            else:
                print("Проверьте корректность ввода")
                return attack_car3(health_car3, damage, inventory)
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return health_car3, health.hp_player, health.count_burn_cars
        else:
            print("Проверьте корректность ввода")
            return attack_car3(health_car3, damage, inventory)
    else:
        print("У вас нет необходимых предметов в инвентаре.")
        return health_car3, health.hp_player, health.count_burn_cars




def attack_car4(health_car4, damage, inventory):
    print("Вы подошли к четвёртой машине")
    item1 = "Зажигалка"
    item2 = "Бутылка керосина"

    if item1 in inventory and item2 in inventory:
        selection = input("Вы хотите поджечь машину? Да или Нет >> ")
        if selection.lower() == "да":
            print("Вы подожгли машину! Осталось ждать 10 секунд и потом она сгорит.")
            distance_fire = input("Вы стоите близко к огню. Вы хотите отойти от машины или остаться на месте? Отойти или Остаться >> ")
            if distance_fire.lower() == "отойти":
                print("Вы отошли от машины и не получили урона от огня.")
            elif distance_fire.lower() == "остаться":
                print("Вы решили остаться рядом с горящей машиной и получили урон от огня!")
                health.hp_player -= 30
                if health.hp_player <= 0:
                    print("Вы умерли от ожогов! Соседи узнали что вы хотели поджечь их машины.")
                    print("Вы проиграли!")
                    time.sleep(5)
                    menu()
                    return None, health.hp_player
                else:
                    print("Ваше здоровье =", health.hp_player)

            for i in range(0, 10, 1):
                health_car4 = health_car4 - damage
                time.sleep(1)
            health_car4 = 0
            print("Машина успешно сгорела.")
            health.count_burn_cars += 1
            print("Количество сожжённых машин =", health.count_burn_cars)
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return health_car4, health.hp_player, health.count_burn_cars
        else:
            print("Некорректный ввод, проверьте ввод")
            return attack_car4(health_car4, damage, inventory)
    else:
        print("У вас нет необходимых предметов в инвентаре.")

    return health_car4, health.hp_player, health.count_burn_cars




def attack_car5(health_car5, damage, inventory):
    print("Вы подходите к пятой машине.")
    item1 = "Зажигалка"
    item2 = "Бутылка керосина"

    if item1 in inventory and item2 in inventory:
        selection = input("Вы хотите поджечь машину? Да или Нет >>")
        if selection.lower() == "да":
            print("Вы подожгли машину! Осталось ждать 10 секунд и потом она сгорит.")
            distance_fire = input("Вы стоите близко к огню. Вы хотите отойти от машины или остаться на месте? Отойти или Остаться >> ")
            if distance_fire.lower() == "отойти":
                print("Вы отошли от машины и не получили урона от огня.")
            elif distance_fire.lower() == "остаться":
                print("Вы решили остаться рядом с горящей машиной и получили урон от огня!")
                health.hp_player -= 30
                if health.hp_player <= 0:
                    print("Вы умерли от ожогов! Соседи узнали что вы хотели поджечь их машины.")
                    print("Вы проиграли!")
                    time.sleep(5)
                    menu()
                    return None, health.hp_player
                else:
                    print("Ваше здоровье =", health.hp_player)

            for i in range(0, 10, 1):
                health_car5 = health_car5 - damage
                time.sleep(1)
            health_car5 = 0
            print("Машина успешно сгорела")
            health.count_burn_cars += 1
            print("Количество сожжённых машин =", health.count_burn_cars)
            print("О нет! Сосед вышел, нужно что-то делать.")
            hide = input("Вы желаете спрятаться? Да или Нет >>")
            if hide.lower() == "да":
                print("Вы спрятались и сосед вас не заметил. Он ушёл звать на помощь.")
                return health_car5, health.hp_player, health.count_burn_cars
            elif hide.lower() == "нет":
                print("Вы не сумели спрятаться, сосед вас заметил. Игра проиграна!")
                print("Вы проиграли!")
                time.sleep(3)
                menu()
                return None, health.hp_player, health.count_burn_cars
            else:
                print("Проверьте корректность ввода")
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return health_car5, health.hp_player, health.count_burn_cars
        else:
            print("Проверьте корректность ввода")
            return attack_car5(health_car5, damage, inventory)
    else:
        print("У вас нет необходимых предметов в инвентаре.")
        return health_car5, health.hp_player, health.count_burn_cars


def end(data):
    if data["count_burn_cars"] == 0:
        print("Хорошая концовка")
    elif 5 > data["count_burn_cars"] > 0:
        print("Плохая концовка")
    elif data["count_burn_cars"] == 5:
        print("Средняя концовка")
    else:
        print("Непредвиденная ситуация")
























