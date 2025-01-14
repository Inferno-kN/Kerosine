from GUI import gui
from game.new_game import additional_menu


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
