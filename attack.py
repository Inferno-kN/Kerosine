import time
from core.main_menu import menu


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


def attack_car2(data, name_car) -> bool:
    print(f"Вы подошли {name_car} машине")

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
                return data["health_car2"], data["hp_player"], data["count_burn_cars"]
            elif hide.lower() == "нет":
                print("Вы не сумели спрятаться, сосед вас заметил. Игра проиграна!")
                print("Вы проиграли!")
                time.sleep(3)
                menu()
                return None, data["hp_player"], data["count_burn_cars"]
            else:
                print("Проверьте корректность ввода")
                return attack_car2(data["health_car2"], data["damage"])
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return data["health_car2"],  data["hp_player"], data["count_burn_cars"]
        else:
            print("Проверьте корректность ввода")
            return attack_car2(data["health_car2"], data["damage"])




def attack_car3(data, name_car) -> bool:
    print(f"Вы подошли {name_car} машине")

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
                return data["health_car2"], data["hp_player"], data["count_burn_cars"]
            elif hide.lower() == "нет":
                print("Вы не сумели спрятаться, сосед вас заметил. Игра проиграна!")
                print("Вы проиграли!")
                time.sleep(3)
                menu()
                return None, data["hp_player"], data["count_burn_cars"]
            else:
                print("Проверьте корректность ввода")
                return attack_car2(data["health_car2"], data["damage"])
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return data["health_car2"],  data["hp_player"], data["count_burn_cars"]
        else:
            print("Проверьте корректность ввода")
            return attack_car2(data["health_car2"], data["damage"])




def attack_car4(data, name_car) -> bool:
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




def attack_car5(data, name_car) -> bool:
    print(f"Вы подошли {name_car} машине")

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
                return data["health_car2"], data["hp_player"], data["count_burn_cars"]
            elif hide.lower() == "нет":
                print("Вы не сумели спрятаться, сосед вас заметил. Игра проиграна!")
                print("Вы проиграли!")
                time.sleep(3)
                menu()
                return None, data["hp_player"], data["count_burn_cars"]
            else:
                print("Проверьте корректность ввода")
                return attack_car2(data["health_car2"], data["damage"])
        elif selection.lower() == "нет":
            print("Вы решили не поджигать машину.")
            return data["health_car2"],  data["hp_player"], data["count_burn_cars"]
        else:
            print("Проверьте корректность ввода")
            return attack_car2(data["health_car2"], data["damage"])