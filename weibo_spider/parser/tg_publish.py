import telebot
from telebot import types
import requests

# avmoo_bot token
bot_token = '1963044732:AAHTvIACGKbM8oaNHg1MuAebOtfDJKEP8LA'
tb = telebot.TeleBot(bot_token)

# headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}


def send_photo_message(chat_id, photo_urls, temp_file_name='temp', caption=''):
    response = requests.get(url=photo_urls, headers=headers)
    with open(temp_file_name, 'wb') as f:
        f.write(response.content)
        f.close()
    img = open(temp_file_name, 'rb')
    media_list = []
    media_list.append(types.InputMediaPhoto(media=img, caption=caption, parse_mode='Html'))
    tb.send_media_group(chat_id=chat_id, media=media_list)
    pass


def send_message(chat_id, caption):
    tb.send_message(chat_id=chat_id, text=caption, parse_mode='Html')
    pass


# 图片现在到本地，返回图片
def getFileFromUrl(url, file_name=None):
    if file_name is None:
        return ''
    response = requests.get(url=url, headers=headers)
    with open(file_name, 'wb') as f:
        f.write(response.content)
        f.close()
    img = open(file_name, 'rb')
    return img
    pass
