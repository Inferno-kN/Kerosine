from GUI.message import message_history as dict_mess


def print_info_message(key):
    print(dict_mess[key])


def hello_in_name(name):
    print(f"Приветствую, {name}! Вы являетесь добрым человеком, но вас окружали плохие люди. \n"
                                  "Почти каждый день вы терпели насмешки от своих соседей, которые постоянно \n"
                                  "над вами издевались и унижали. Вы решаете, что всё, время унижений подошло к \n"
                                  "концу, и хотите жестоко отомстить. Что ж, как говорится:'Один в поле не воин!' \n"
                                  "(нажмите Enter)}")


def input_user_action():
    return input(" >> ")