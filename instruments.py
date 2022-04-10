from config import *
from question_mode import *


def event_handler(event):
    if event.to_me and event.from_user:
        if base[event.user_id][0] == 13:

            if event.text.lower() == 'лайк':
                print('like')
                base[event.user_id][2][0] += 1
            elif event.text.lower() == 'дизлайк':
                base[event.user_id][2][1] += 1
                print('dislike')

            base[event.user_id][3][base[event.user_id][1]] = 8
            user_sender(event.user_id, 'Оке')
            base[event.user_id][0] = 0

        elif event.text.lower() == 'привет' and base[event.user_id][0] == 0:
            hello_world_operation(event)

        elif event.text.lower() == 'мем' and base[event.user_id][0] == 0:
            get_meme_operation(event)

        elif event.text.lower() == 'статистика' and base[event.user_id][0] == 0:
            get_state(event)

        elif event.text.lower() == 'вопросы' and base[event.user_id][0] == 0:
            base[event.user_id][0] = 0
            question_1(event)

        elif base[event.user_id][0] == 1:
            question_2(event)

        elif base[event.user_id][0] == 2:
            question_3(event)

        elif base[event.user_id][0] == 3:
            question_4(event)

        elif base[event.user_id][0] == 4:
            question_5(event)

        elif base[event.user_id][0] == 5:
            question_6(event)

        elif base[event.user_id][0] == 6:
            question_7(event)

        elif base[event.user_id][0] == 7:
            question_8(event)

        elif base[event.user_id][0] == 8:
            question_end(event)

        else:
            echo_operation(event)


def hello_world_operation(event):
    id = event.user_id
    msg = 'Привет вездекодерам!'
    user_sender(id, msg)


def echo_operation(event):
    id = event.user_id
    msg = 'Команды:\n' \
          '"Привет" - поприветствует\n' \
          '"Вопросы" - задаст 8 очень интересных вопросов и выдаст статистику ответов\n' \
          '"Мем" - выдаст мем\n' \
          '"Статистика" - покажет статистику лайков и дизлайков\n'
    user_sender(id, msg)


def get_state(event):
    msg = f'Твоя статистика взаймодействия с базой мемов:\n' \
          f'Лайков - {base[event.user_id][2][0]}\n' \
          f'Дизлайков - {base[event.user_id][2][1]}'
    vk_session.method('messages.send', {'user_id': event.user_id, 'message': msg, 'random_id': 0})


def get_meme_operation(event):
    keyboard_rate = VkKeyboard(inline=True)
    keyboard_rate.add_button('Лайк', color=VkKeyboardColor.POSITIVE)
    keyboard_rate.add_button('Дизлайк', color=VkKeyboardColor.NEGATIVE)

    output = random.choice(random_photo_key)
    counter = 0

    while base[event.user_id][3][random_photo_key.index(output)] == 8:

        output = random.choice(random_photo_key)

        if counter == 50:
            msg = 'Мемы кончились...'
            vk_session.method('messages.send', {'user_id': event.user_id, 'message': msg, 'random_id': 0})
            base[event.user_id][0] = 0
            return

        counter += 1

    try:
        vk_session.method('messages.send', {'user_id': event.user_id, 'random_id': 0,
                                            'attachment': output, 'keyboard': keyboard_rate.get_keyboard()})
    except:
        user_sender(event.user_id, 'Какая-то ошибка (((')

    base[event.user_id][1] = random_photo_key.index(output)
    base[event.user_id][0] = 13


def user_sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})
