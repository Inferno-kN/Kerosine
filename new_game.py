from GUI import gui
from action.attack import attack_car1, attack_car2, attack_car3,attack_car4,attack_car5

def additional_menu():
    T = False
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

    inventory = ["Зажигалка", "Бутылка керосина"]
    damage = 10
    health_car1 = 100  # Здоровье машины первого соседа
    health_car2 = 100
    health_car3 = 100
    health_car4 = 100
    health_car5 = 100
    health_player = 100
    health_car1 = attack_car1(health_car1, damage)
    health_car2 = attack_car2(health_car2, damage)
    health_car3 = attack_car3(health_car3, damage)
    health_car4 = attack_car4(health_car4, damage)
    health_car5 = attack_car5(health_car5, damage)
    health_cars = 100 * 5 #здоровье всех пяти машин