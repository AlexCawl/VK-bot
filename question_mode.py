from config import *


def question_1(event):
    message = 'ФОРТИНАЙТИ ИЛИ БАБАДЖИ?'

    keyboard_1 = VkKeyboard(one_time=True)
    keyboard_1.add_button('ФОРТИНАЙТИ', color=VkKeyboardColor.PRIMARY)
    keyboard_1.add_button('БАБАДЖИ', color=VkKeyboardColor.SECONDARY)

    vk_session.method('messages.send',
                      {'user_id': event.user_id, 'message': message, 'random_id': 0,
                       'keyboard': keyboard_1.get_keyboard()})
    base[event.user_id][0] += 1


def question_2(event):
    try:
        base[event.user_id][4].append(event.text)
        message = f'{event.text} или ПЛЕЙСТЕЙШОН ФААЙФ?'
        keyboard_2 = VkKeyboard(one_time=True)
        keyboard_2.add_button(f'{event.text}', color=VkKeyboardColor.POSITIVE)
        keyboard_2.add_button('ПЛЕЙСТЕЙШОН ФААЙФ', color=VkKeyboardColor.NEGATIVE)
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                            'keyboard': keyboard_2.get_keyboard()})
    except:
        base[event.user_id][4].append('Sticker')
        message = f'Sticker или ПЛЕЙСТЕЙШОН ФААЙФ?'
        keyboard_2 = VkKeyboard(one_time=True)
        keyboard_2.add_button(f'Sticker', color=VkKeyboardColor.POSITIVE)
        keyboard_2.add_button('ПЛЕЙСТЕЙШОН ФААЙФ', color=VkKeyboardColor.NEGATIVE)
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                            'keyboard': keyboard_2.get_keyboard()})

    base[event.user_id][0] += 1


def question_3(event):
    try:
        base[event.user_id][4].append(event.text)
        message = f'{event.text} или ЛОДЖИТЕК?'

        keyboard_3 = VkKeyboard(one_time=True)
        keyboard_3.add_button(f'{event.text}', color=VkKeyboardColor.PRIMARY)
        keyboard_3.add_button('ЛОДЖИТЕК', color=VkKeyboardColor.POSITIVE)
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                            'keyboard': keyboard_3.get_keyboard()})
    except:
        base[event.user_id][4].append('Sticker')
        message = f'Sticker или ЛОДЖИТЕК?'

        keyboard_3 = VkKeyboard(one_time=True)
        keyboard_3.add_button(f'Sticker', color=VkKeyboardColor.PRIMARY)
        keyboard_3.add_button('ЛОДЖИТЕК', color=VkKeyboardColor.POSITIVE)
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                            'keyboard': keyboard_3.get_keyboard()})

    base[event.user_id][0] += 1


def question_4(event):
    base[event.user_id][4].append(event.text)
    message = 'У нас есть один классный геймдизайнер. Поиграешь?'

    keyboard_4 = VkKeyboard(inline=True)
    keyboard_4.add_vkapps_button(app_id=8131735, owner_id=-181108510, label="Классная игра", hash="sendKeyboard")
    keyboard_4.add_button('Нет', color=VkKeyboardColor.NEGATIVE)

    vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                        'keyboard': keyboard_4.get_keyboard()})
    base[event.user_id][0] += 1


def question_5(event):
    base[event.user_id][4].append(event.text)
    message = 'Что должен ответить Бен?'

    keyboard_5 = VkKeyboard(inline=True)
    keyboard_5.add_button('YEEES', color=VkKeyboardColor.POSITIVE)
    keyboard_5.add_button('No.', color=VkKeyboardColor.NEGATIVE)
    keyboard_5.add_line()
    keyboard_5.add_button('Хо-хо', color=VkKeyboardColor.PRIMARY)
    keyboard_5.add_button('Чпоньк', color=VkKeyboardColor.SECONDARY)

    vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                        'keyboard': keyboard_5.get_keyboard()})
    base[event.user_id][0] += 1


def question_6(event):
    base[event.user_id][4].append(event.text)
    message = 'Я хочу пиццы. Заплатишь?'

    keyboard_6 = VkKeyboard(inline=True)
    keyboard_6.add_vkpay_button(hash="action=transfer-to-group&group_id=74030368&aid=6222115")
    keyboard_6.add_line()
    keyboard_6.add_button('Денег нет', color=VkKeyboardColor.SECONDARY)

    vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                        'keyboard': keyboard_6.get_keyboard()})
    base[event.user_id][0] += 1


def question_7(event):
    base[event.user_id][4].append(event.text)
    message = 'Я не знаю кто ты, но я вычислю тебя по IP?'

    keyboard_7 = VkKeyboard(inline=True)
    keyboard_7.add_location_button()
    keyboard_7.add_button('Ну вычисляй...')

    vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                        'keyboard': keyboard_7.get_keyboard()})
    base[event.user_id][0] += 1


def question_8(event):
    base[event.user_id][4].append(event.text)
    message = 'Откроешь ссылку на классную группу?'

    keyboard_8 = VkKeyboard(inline=True)
    keyboard_8.add_openlink_button(label='Классная группа', link='https://vk.com/club197700721')
    keyboard_8.add_button('Открыл', color=VkKeyboardColor.POSITIVE)

    vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0,
                                        'keyboard': keyboard_8.get_keyboard()})
    base[event.user_id][0] += 1


def question_end(event):
    base[event.user_id][4].append(event.text)

    answers = ''
    for i in range(len(base[event.user_id][4])):
        answers += f'{i + 1}) {base[event.user_id][4][i]}\n'

    message = f'Закончили опрос. Твои ответы:\n{answers}'
    vk_session.method('messages.send', {'user_id': event.user_id, 'message': message, 'random_id': 0, })
    base[event.user_id][0] = 0
    base[event.user_id][4].clear()