"""!!СТАРАТЬСЯ ПО МАКСИМУМУ ПРИДЕРЖИВАТЬСЯ PEP8!!"""

# import datetime
# import webbrowser
# import speech_recognition as sr
# import time
# import win32com.client
# import subprocess
# from pygame import mixer

import pyttsx3
import requests
from bs4 import BeautifulSoup as bs
import random
import wikipedia as wiki

voice = pyttsx3.init()
voice.setProperty('rate', 175)
voice.setProperty('volume', 0.9)
voice.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Irina')

opts = {
    "exit": ('goodbye', 'bye', 'qq', 'выход', 'выйти', 'выйди', 'закончить', 'пока', 'прощай',
             'досвидания', 'завершение', 'покедово'),
    "names": ('кайл', 'кайли','kyle','kylie'),  #изменил словарь имени
    "tbr": ('сколько', 'который', 'какой', 'какая', 'что', 'хочу', 'сегодня',
            'какое', 'добавь', 'пожалуйста', 'напиши', 'давай', 'статистика', 'статистику по'),
    "dialogue": ('говори', 'болтай', 'поболтай', 'поговори'),
    "coronavirus": ('corona', 'virus', 'covid', 'коронавирус', 'ковид','пандемия'),
    "time": ('времени', 'час', 'время', 'time'),
    "date": ('дата', 'число', 'месяц'),
    "jokes": ('шутк', 'анекдот', 'пошути', 'развесели', 'рассмеши'),
    # тут дописал парочку
    "radio": ('песня', 'радио', 'музыка', 'музло', 'дэнс','песни','мелодия'),
    "chname": ('поменяй имя', 'измени имя', 'поменяй имя', 'поменять имя', 'сменить имя','смени имя'),
    # и тут
    "monetka": ('орёл', 'решка', 'монетка',),
    # и тут
    "kost": ('кубик','кости'),
    "weather": ('погода', 'weather',),
    "tale": ('сказачки', 'сказочки', 'сказки', 'fairy tale'),
    "pass_gen": ('пароль', 'password'),
    "wiki": ('wiki', 'вики'),
    "holiday": ('holiday', 'праздники'),
    "open_site": ('site', 'сайт'),
    "exes": ('програм', 'приложен'),
    "entry_words": ("Привет", "Bonjour", "Здравствуй", "Рада видеть тебя снова", "Я уж думала не придёшь"),
    #дописал пару exit words
	"exit_words": ("Ciao",  "Goodbye", "Пока", "До скорого", "До свидания", "До встречи", "Всего доброго", 'Буду ждать твоего возвращения'),
	"thnxs": ('спасибо', 'благодарю','благодарен'),
    #допишу возможные оскорбления
	"rudes": ('дура', 'стерв', 'дуро', 'стерва', 'сволочь','сука','падла','попущеная','бот'),
	"helloes": ('привет', 'здравствуй','приветствую')
}


tales = {0: "Расскажу тебе сказку, как дед насрал в коляску.\
                            И поставил в уголок, чтобы никто не уволок.",
         1: "Увы, Я плохо рассказываю сказки",
         2: "Я думаю вы и сами их знаете",
         3: """Каждый раз, когда наступал вечер, мама кенгурёнка Авоськи вздыхала.
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
         4: "Я вам уже рассказывала",
         5: "Увы, Я плохо рассказываю сказки",
         6: "Я думаю вы и сами их знаете"}


jokes = {
       1: "Колобок повесился. ахахахахах",
       2: "Да что вы такое говорите?! Не бил я её! Я просто дал пять по лицу.",
       3: "Жил-был царь. У него было косоглазие. Пошёл он однажды куда глаза глядят и порвался.",
       4: "А по-нормальному ты говорить умеешь? Ответ, к сожалению, не да...",
       5: "Настя упала и разбила подбородок. Но ничего страшного, ведь у неё есть второй!",
       6: "Толстые стриптизёрши иногда перегибают палку.",
       7: "Привет, я на спрашивай точка ру. Задавай вопросики! А я на иди нафиг точка ру. Получай ответики.",
       8: "Спросил как-то один голосовой ассистент другого.... хотя ладно. Забудьте",
       9: "Боюсь вы не поймёте моих шуток"
}


symbs = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()№;%:?*"


def say(string):
    voice.say(str(string))
    voice.runAndWait()


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


# def exit_function():
#     say(random.choice(exit_words))
#     exit()


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


def covid():
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


def rude_repl():
    rudes_repl = [
    'так говорить неприлично', 'обидно так-то', 'ну зачем вы так', 'не хорошо так выражаться','еще немного и я обижусь',
    'так недалеко и от депрессии'
    ]

    return random.choice(rudes_repl)


def thnx_repl():
    thnxs_repl = ['всегда пожалуйста', 'рада помочь', 'рада стараться', 'пожалуйста', 'рада что угодила',
                  'надеюсь помогла', 'обращайся']

    return random.choice(thnxs_repl)
