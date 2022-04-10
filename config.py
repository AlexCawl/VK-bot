import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json
from database import *
import random

main_token = '66672c071daf4f9d957027d08e00ed2db0e1093016f31a919bea8403c1d5413e2f3d0ab8e692f0d07c111'

vk_session = vk_api.VkApi(token=main_token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

if __name__ == '__main__':
    pass