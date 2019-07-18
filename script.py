import os, re
import requests
import bs4
import time

date = '31.08.2019'

data = {
    'pa': 'express3',
    'sa': 'GET_P62G60_EVENT',
    'STEP': '1',
    'TIME': '',
    'FROM_STATION': '\u041D\u0443\u0440-\u0421\u0443\u043B\u0442\u0430\u043D-\u041D\u0443\u0440\u043B\u044B \u0436\u043E\u043B(2700152)',
    'TO_STATION': '\u0410\u0442\u044B\u0440\u0430\u0443(2704830)',
    'DATE': date,
}

while True:
    res = requests.post('https://epay.railways.kz/ktz4/proc', data=data)
    beauty = bs4.BeautifulSoup(res.text, "html.parser")
    schedule_item = beauty.select('.schedule-item')
    if schedule_item:
        route = ((re.search('<i class="fa fa-map-marker"></i> <span>(.+?)</span></a></th>',
                            str(schedule_item))).group(1))
        time_from = ((re.search('<span class="time-from">Время отправления: <big><b>(.+?)</b></big></span>',
                                str(schedule_item))).group(1))
        time_to = ((re.search('<span class="time-to">Время прибытия: <big><b>(.+?)</b></big></span>',
                              str(schedule_item))).group(1))
        plackart = ((re.search('<td>Плацкартный <span class="label">(.+?)</span></td>', str(schedule_item))).group(1))
        coupe = ((re.search('<td>Купе <span class="label">(.+?)</span></td>', str(schedule_item))).group(1))

        if int(plackart) > 1 or int(coupe) > 1:
            print(f"Маршрут поезда: {route}\n"
                  f"Дата отправления: {date}\n"
                  f"Время отправления: {time_from}\n"
                  f"Время прибытия: {time_to}\n"
                  f"Плацкартный: {plackart}\n"
                  f"Купе: {coupe}")
            os.system('afplay OmaeWaMouShindeiru.mp3')

    time.sleep(300)