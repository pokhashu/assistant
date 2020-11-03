# -*- coding: utf-8 -*- 
# version 0.0.7 Alpha пиздец, что то не хотело, пришлось так

"""!!СТАРАТЬСЯ ПО МАКСИМУМУ ПРИДЕРЖИВАТЬСЯ PEP8!!"""

# import datetime
# import speech_recognition as sr
import time
# import win32com.client
# import subprocess
# from pygame import mixer

import webbrowser
import pyttsx3
import requests
from bs4 import BeautifulSoup as bs
import random
import wikipedia as wiki
import json

with open('C:/Users/User/Desktop/assistant/settings.json', 'r') as f:
    settings = json.load(f)

ASSISTANT_VOICE_man = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Alan+Aleksandr'
ASSISTANT_VOICE_woman = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0' #'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Irina'
voice = pyttsx3.init(driverName='sapi5') 
voice.setProperty('rate', 175)
voice.setProperty('volume', 0.9)
voice.setProperty('voice', ASSISTANT_VOICE_woman)
if settings['assistant_voice'] == 'woman':
    voice.setProperty('voice', ASSISTANT_VOICE_woman)
elif settings['assistant_voice'] == 'man':
    voice.setProperty('voice', ASSISTANT_VOICE_man)
else:
    voice.setProperty('voice', ASSISTANT_VOICE_woman)

opts = {
    "exit": ('goodbye', 'bye', 'qq', 'выход', 'выйти', 'выйди', 'закончить', 'пока', 'прощай',
             'досвидания', 'завершение', 'покедово'),
    "names": ('kylie', 'кайли'),  
    # "tbd": ('сколько', 'который', 'какой', 'какая', 'что', 'хочу', 'сегодня', 'расскажи'.
    #         'какое', 'добавь', 'напиши', 'давай', 'статистика', 'статистику по', 'смени'),
    "dialogue": ('говор', 'болта'),
    "coronavirus": ('corona', 'virus', 'covid', 'коронавирус', 'ковид'),
    "time": ('час', 'врем', 'time'),
    "date": ('дат', 'число'),
    "jokes": ('шутк', 'анекдот', 'пошути', 'развесели', 'рассмеши'),
    "radio": ('песн', 'радио', 'музык', 'музло', 'дэнс'),
    "chname": ('имя'),
    "monetka": ('орёл', 'орел', 'решк', 'монетк'),
    "kost": ('кост', 'кубик'),
    "weather": ('погод', 'weather',),
    "tales": ('сказ', 'fairy tale'),
    "pass_gen": ('парол', 'password'),
    "wiki": ('wiki', 'вики'),
    "holiday": ('holiday', 'праздн'),
    "open_site": ('site', 'сайт'),
    "exes": ('програм', 'приложен'),
    "entry_words": ("Привет", "Bonjour", "Здравствуй", "Рада видеть тебя снова", "Я уж думала не придёшь"),
    "exit_words": ("Ciao",  "Goodbye", "Пока", "До скорого", "До свидания", "До встречи"),
    "thnxs": ('пасиб', 'благодар'),
    "rudes": ('дур', 'стерв', 'сук', 'нах', 'скотин', 'сволоч', 'паскуд', 'хуй'), 
    "helloes": ('привет', 'здравствуй'),
    "news": ('новост', 'news', 'событ'), 
    "voice": ('голос'),
    "user_name": ('пользовател'),
    "calculator": ('калькулятор'),
    "search": ('найди', 'найти', 'поищи', 'ищи')
	"exit_words": ("Ciao",  "Goodbye", "Пока", "До скорого", "До свидания", "До встречи"),
	"thnxs": ('пасиб', 'благодар'),
	"rudes": ('дур', 'стерв', 'сук', 'нах', 'скотин', 'сволоч', 'паскуд', 'хуй'), #убрал пару лишних окончаний и добавил новые маты
	"helloes": ('привет', 'здравствуй'),
    "news": ('новост', 'news', 'событ'), # добавил словарь для новостей
    "voice": ('голос'),
    "user_name": ('пользовател')
}


tales = ["Расскажу тебе сказку, как дед насрал в коляску. И поставил в уголок, чтобы никто не уволок.",
         "Увы, Я плохо рассказываю сказки",
         "Я думаю вы и сами их знаете",
         """Каждый раз, когда наступал вечер, мама кенгурёнка Авоськи вздыхала. 
            Почему она вздыхала? Потому что надо было снова укладывать в постель своего сынишку и укачивать,
            укачивать, укачивать. Кенгурёнок привык, чтобы его укачивали. Иначе он не засыпал.
            Стоило маме отойти от кроватки — и сразу Авоська поднимал такой крик,
            такой плач, что хоть уши ватой затыкай. Пригласила мама доктора дикобраза Христофора. 
            Узнал доктор, в чём дело, и покачал головой: Тут никакие уколы не помогут.
            От такой болезни может вылечить только… — Микстура? — спросила мама.
            Нет. — Примочка? — Нет. — Компресс? — Что вы! Вашего больного не спасут никакие микстуры,
            никакие примочки и никакие компрессы. Но не надо огорчаться. Я уже не раз встречал подобных больных.
            И все выздоравливали. — Доктор, скорей выписывайте свой чудесный рецепт — и я побегу в аптеку! 
            — В аптеку идти не придётся. От болезни, которой страдает ваш кенгурёнок, есть одно средство
            — Самое Интересное Слово — Какое Самое? Какое Интересное? Какое Слово?
            — переспросила взволнованная мама кенгуру. Доктор ничего не ответил и стал выписывать рецепт.
            — Здесь всё указано, — сказал он на прощание. Когда доктор ушёл,
            мама кенгуру надела очки, заглянула в рецепт и прочла одно-единственное слово:
            — Однажды Вечером, как обычно, она уложила кенгурёнка спать, но укачивать не стала.
            Только маленький Авоська начал хныкать, как мама произнесла Самое Интересное Слово. 
            — Однажды. Кенгурёнок сразу успокоился и спросил: — Что было однажды? Мама, расскажи, пожалуйста!
            И мама стала рассказывать сказку: — Однажды одному лягушонку захотелось мороженого
            Едва сказка закончилась, кенгурёнок крепко-крепко заснул. И ему снился маленький зелёный лягушонок,
            который съел целых десять порций эскимо и едва не превратился в ледяную сосульку
            На другой вечер Авоська сам разделся, сам улёгся в постель и терпеливо принялся ждать,
            когда же мама, наконец, снова произнесёт Самое Интересное Слово,
            с которого обычно начинаются все сказки на свете.""",
         "Я вам уже рассказывала",
         "Увы, Я плохо рассказываю сказки",
         "Я думаю вы и сами их знаете"]


# jokes = {
#        '0': "Колобок повесился. ахахахахах",
#        '1': "Да что вы такое говорите?! Не бил я её! Я просто дал пять по лицу.",
#        '2': "Жил-был царь. У него было косоглазие. Пошёл он однажды куда глаза глядят и порвался.",
#        '3': "А по-нормальному ты говорить умеешь? Ответ, к сожалению, не да...",
#        '4': "Настя упала и разбила подбородок. Но ничего страшного, ведь у неё есть второй!",
#        '5': "Толстые стриптизёрши иногда перегибают палку.",
#        '6': "Привет, я на спрашивай точка ру. Задавай вопросики! А я на иди нафиг точка ру. Получай ответики.",
#        '7': "Спросил как-то один голосовой ассистент другого.... хотя ладно. Забудьте",
#        '8': "Боюсь вы не поймёте моих шуток"}

jokes = [
        "Колобок повесился. ахахахахах",
        "Да что вы такое говорите?! Не бил я её! Я просто дал пять по лицу.",
        "Жил-был царь. У него было косоглазие. Пошёл он однажды куда глаза глядят и порвался.",
        "А по-нормальному ты говорить умеешь? Ответ, к сожалению, не да...",
        "Настя упала и разбила подбородок. Но ничего страшного, ведь у неё есть второй!",
        "Толстые стриптизёрши иногда перегибают палку.",
        "Привет, я на спрашивай точка ру. Задавай вопросики! А я на иди нафиг точка ру. Получай ответики.",
        "Спросил как-то один голосовой ассистент другого.... хотя ладно. Забудьте",
        "Боюсь вы не поймёте моих шуток",
        "Какая разница между десятью часами утра и четыремя часами вечера? Шесть часов!"]

symbs = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()№;%:?*"


def say(string):
    voice.say(str(string))
    voice.runAndWait()


def settings_json(action, key, added_item=None):
    global settings
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    if action == 'add':
        settings[key] = added_item
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
    elif action == 'dlt':
        settings[key] = None
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
    elif action == 'edit':
        settings[key] = added_item
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
    else:
        return 0
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    return 1


def assistant_voice_change():
    if settings['assistant_voice'] == 'woman':
        voice.setProperty('voice', ASSISTANT_VOICE_woman)
    elif settings['assistant_voice'] == 'man':
        voice.setProperty('voice', ASSISTANT_VOICE_man)
    else:
        voice.setProperty('voice', ASSISTANT_VOICE_woman)
        
    return 1


def exit_function():
    return random.choice(opts['exit_words'])


def holiday():
    rec = requests.get('https://my-calend.ru/holidays')
    html = bs(rec.content, 'html.parser')
    el = html.select("section")
    h = el[0].select("a")[0].text
    return "Сегодня отмечается " + h


def weather(place):
    if place.endswith('е'):
        place = place[::-1]
        place = place[1::]
        place = place[::-1]
    if place[0] == 'в' and place[1] == ' ':
        place = place[2::]
    place.strip()
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q='+place+'&APPID=9cf8c2092e2926e1d7ffc69f626853be&lang=ru')
    wthr = response.json()
    standing = wthr['weather'][0]['description']
    pressure = int(wthr['main']['pressure']*0.75)
    humidity = int(wthr['main']['humidity'])
    wind_speed = int(wthr['wind']['speed'])
    wind_dir = ''
    temp_fl = int(wthr['main']['feels_like']-273.15)
    temp = int(wthr['main']['temp']-273.15)

    if wthr['wind']['deg'] in range(25, 70):
        wind_dir = ' северо-восточный '
    elif wthr['wind']['deg'] in range(70, 115):
        wind_dir = ' восточный '
    elif wthr['wind']['deg'] in range(115, 160):
        wind_dir = ' юго-восточный '
    elif wthr['wind']['deg'] in range(160, 205):
        wind_dir = ' южный '
    elif wthr['wind']['deg'] in range(205, 250):
        wind_dir = ' юго-западный '
    elif wthr['wind']['deg'] in range(250, 295):
        wind_dir = ' западный '
    elif wthr['wind']['deg'] in range(295, 340):
        wind_dir = ' северо-западный '
    elif wthr['wind']['deg'] in range(340, 360) or wthr['wind']['deg'] in range(0, 25):
        wind_dir = ' северный '

    text_to_say = "В городе " + place.title() + " температура в районе " + str(temp) + " градусов цельсия."
    text_to_say += " Ощущается на " + str(temp_fl) + ".\n"
    text_to_say += " Сейчас " + standing + ".\n"
    text_to_say += " Давление " + str(pressure) + " миллиметров ртутного столба.\n"
    text_to_say += " Влажность " + str(humidity) + " процентов."
    text_to_say += " Ветер " + wind_dir + ". Скорость " + str(wind_speed) + " метров в секунду.\n"

    text_to_print = "В городе " + place.title() + " температура в районе " + str(temp) + " °C.\n"
    text_to_print += " Ощущается на " + str(temp_fl) + ".\n"
    text_to_print += " Сейчас " + standing + ".\n"
    text_to_print += " Давление " + str(pressure) + " мм.рт.ст.\n"
    text_to_print += " Влажность " + str(humidity) + "%.\n"
    text_to_print += " Ветер " + wind_dir + ". Скорость " + str(wind_speed) + " м/с.\n"

    return text_to_say


def tale():
    return random.choice(tales)


def joke():
    return random.choice(jokes)


def coin():
    return random.choice(['Решка', 'Орёл'])


def dice():
    rand_int1 = random.randint(1, 7)
    rand_int2 = random.randint(1, 7)

    return "Выпало " + str(rand_int1) + " и " + str(rand_int2)


def pass_gen():
    password = ""
    for i in range(1, 11):
        password += symbs[random.randint(0, len(symbs)-1)]

    return password


def coronavirus():
    res = ""
    r = requests.get('https://www.worldometers.info/coronavirus/')
    html = bs(r.content, 'html.parser')
    temp = 0
    # now = datetime.now()
    res += "Статистика по коронавирусу на сегодня.\n"
    for el in html.select('.maincounter-number'):
        number = el.select('span')
        if temp == 0:
            common = number[0].text
            common = common.strip()
            #res += "Всего случаев: " + common
            common = common.replace(',', '')
            if len(common) >= 7:
                i = common[-6:len(common)]
                j = common[0:-6]
                res += 'Всего случаев: ' + j + ' миллионов ' + i + ' человек.\n'
            else:
                res += "Всего случаев: " + common + " человек.\n"
        elif temp == 1:
            died = number[0].text
            died = died.strip()
            #print("Умерло: " + died)
            died = died.replace(',', '')
            if len(died) >= 7:
                i = died[-6:len(died)]
                j = died[0:-6]
                res += 'Умерло: ' + j + ' миллионов ' + i + ' челове.\n'
            else:
                res += "Умерло: " + died + " человек.\n"
        elif temp == 2:
            recovered = number[0].text
            recovered = recovered.strip()
            #print("Выздоровело: " + recovered)
            recovered = recovered.replace(',', '')
            if len(recovered) >= 7:
                i = recovered[-6:len(recovered)]
                j = recovered[0:-6]
                res += 'Вылечилось: ' + j + ' миллионов ' + i + ' человек.\n'
            else:
                res += "Вылечилось: " + recovered + " человек.\n"

        temp += 1
    ill_ = int(common) - int(died) - int(recovered)
    ill_ = str(ill_)
    ill_ = ill_[::-1]
    temp = 0
    ill = ''
    for char in str(ill_):
        ill += char
        temp += 1
        if temp % 3 == 0:
            ill += ','
    ill = ill[::-1]
    #print("Болеет: " + ill)
    ill = ill.replace('.', '')
    if len(ill) >= 7:
        i = ill_[-6:len(ill)]
        j = ill_[0:-6]
        res += 'Болеет: ' + j + ' миллионов ' + i + ' человек.\n'
    else:
        res += "Болеет: " + ill + " человек.\n"

    return res


def wikipedia(query):  # TODO except func
    wiki.set_lang('ru')
    txt = wiki.summary(query)

    return txt[ : txt.find("\n")]


def rudes_repl(): # не было различий
    rudes_repl = ['так говорить неприлично', 'обидно так-то', 'ну зачем вы так', 'не хорошо так выражаться']

    return random.choice(rudes_repl)


def thnx_repl():
    thnxs_repl = ['всегда пожалуйста', 'рада помочь', 'рада стараться', 'пожалуйста', 'рада что угодила',
                  'надеюсь помогла']

    return random.choice(thnxs_repl)

def hello():
    helloes = ['Здравствуй', 'Bonjour', 'Привет', 'Рада тебя видеть']
    return random.choice(helloes)

def news():
    r = requests.get('https://news.tut.by/world')
    html = bs(r.content, 'html.parser')
    res = []
    html.select('.news-section')
    for el in html.select('.entry-head')[8:13:]:
        res.append(el.text.replace('\xa0', ' '))
    
    return res
    	res.append(el.text.replace('\xa0', ' '))
    print('Новости на данный момент')
    for i in res:
        print('- ', i) #слегка изменил функцию новостей

#def calculator(var, a: int, b: int):
#    if var == "+":
#        result = str(a) + ' ' + str(var) + ' ' + str(b) + ' = ' + (str(int(a) + int(b)))
#
#    elif var == "+":
#        result = str(a) + ' ' + str(var) + ' ' + str(b) + ' = ' + (str(int(a) - int(b)))
#
#    elif var == "+":
#        result = str(a) + ' ' + str(var) + ' ' + str(b) + ' = ' + (str(int(a) * int(b)))
#
#    elif var == "/":
#        result = str(a) + ' ' + str(var) + ' ' + str(b) + ' = ' + (str(int(a) * int(b)))
#
#    elif var == 'x':
#        exit()
#
#    return result

# def exchange_rates():
#     r = requests.get('https://myfin.by/currency/minsk')
#     html = bs(r.content, 'html.parser')
#     html.select('.bank-info-head')
#     html.select('table')
#     print(html.select('table'))
#     html.select('tbody')
#     print(html.select('tbody'))
#     html.select('tr')
#     print(html.select('td'))


def main(request):
    for el in opts['helloes']:
        if el in request:
            print(hello())
    for el in opts['thnxs']:
        if el in request:
            print(thnx_repl())
    for el in opts['search']:
        if el in request:
            search = input('Введите запрос для поисковой строки\n>> ')
            print('Открываю результат по запросу: "' + search + '"')
            time.sleep(2)
            webbrowser.open_new_tab('https://www.google.by/search?q=' + str(search))
#    for el in opts['calculator']:
#        if el in request:
#            print('Введите вариант')
#            calc_var = input('>> ')
#            first_num = input('Первое число\n>> ')
#            second_num = input('Второе число\n>> ')
#            print(calculator(calc_var, first_num, second_num))
    for el in opts['holiday']:
        if el in request:
            print(holiday())
    for el in opts['kost']:
        if el in request:
            print(dice())
    for el in opts['monetka']:
        if el in request:
            print(coin())
    for el in opts['pass_gen']:
        if el in request:
            print(pass_gen())
    for el in opts['coronavirus']:
        if el in request:
            print(coronavirus())
    for el in opts['jokes']:
        if el in request:
            print(joke())
    for el in opts['tales']:
        if el in request:
            print(tale())
    	if el in request:
    		print(tale())
    for el in opts['news']:
        if el in request:
            print(news())
    for el in opts['rudes']:
        if el in request:
            print(rudes_repl())
    for el in opts['exit']:
        if el in request:
            print(exit_function())
            exit()

while True:
    request = input('>> ').lower()
    main(request)
