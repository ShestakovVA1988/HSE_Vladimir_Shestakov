#pip install lxml
#pip install requests
#pip install bautifulsoup4


from bs4 import BeautifulSoup
import requests
import json
import datetime
import statistics
import pathlib
import os

class ParserCBRF:

        def __init__(self):
            pass

        def start(self, stdate, enddate):
            try:
                sdate = datetime.datetime.strptime(stdate, "%d.%m.%Y")
                edate = datetime.datetime.strptime(enddate, "%d.%m.%Y")
            except:
                print('Ошибка! Введите даты в формате дд.мм.ГГГГ')
                exit()
            self.__parse_data_to_json(str(stdate),str(enddate))

        def __parse_data_to_json(self, stdate, enddate):
            url = f"https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01010&UniDbQuery.From={stdate}&UniDbQuery.To={enddate}"
            page = requests.get(url)
            # print(page.status_code)
            soup = BeautifulSoup(page.text, "html.parser")

            ntable = str(soup.findAll('td', class_=''))  # сразу упаковываем в строку
            ttable = ntable[ntable.find('<td>') + 4:].replace('</td>]', '')  # убираем лишнее
            items = ttable.split('</td>, <td>')  # убираем теги
            #print(items)
            tdata = {} #need to rework with list comprehensions
            for i in range(0, len(items) - 2, 3):  # упаковываем в словарь
                ddate = str(items[i]).split('.')
                rdate = datetime.date(int(ddate[2]), int(ddate[1]), int(ddate[0]))
                tdata[str(rdate)] = str(items[i + 2].replace(',', '.'))
            filepath = os.path.join(pathlib.Path(__file__).parent.resolve(), 'parsed_data','jsondump.json')
            with open(filepath, 'w') as nfile:  # сохраняем в json
                json.dump(tdata, nfile)

class XrateCBRF:

        def __init__(self):
            filepath = os.path.join(pathlib.Path(__file__).parent.resolve(), 'parsed_data', 'jsondump.json')
            self.jsdata = json.load(open(filepath))
            print(self.jsdata)

        def val_by_date(self, tdate):
            try:
                print(f"Значение на {tdate} составляет {self.jsdata[tdate]}")
            except:
                print('Значение не найдено')

        def last_val(self):
            last_v = max((x for x in self.jsdata.keys()), key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))
            print(f"Значение на последнюю дату ({last_v})  составляет {self.jsdata[last_v]}")

        def val_by_dates(self, stdate, enddate):
            try:
                sdate = datetime.datetime.strptime(stdate, "%Y-%m-%d")
                edate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
            except:
                print('Ошибка! Введите даты в формате гггг-мм-дд')
                exit()
            for it in self.jsdata:
                if (datetime.datetime.strptime(it, '%Y-%m-%d') >= sdate) and\
                        (datetime.datetime.strptime(it, '%Y-%m-%d') <= edate):
                    print(it, self.jsdata[it])

        def max_val_by_dates(self, stdate, enddate):
            try:
                sdate = datetime.datetime.strptime(stdate, "%Y-%m-%d")
                edate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
            except:
                print('Ошибка! Введите даты в формате гггг-мм-дд')
                exit()
            res = []
            for it in self.jsdata:
                if (datetime.datetime.strptime(it, '%Y-%m-%d') >= sdate) and\
                        (datetime.datetime.strptime(it, '%Y-%m-%d') <= edate):
                    res.append(self.jsdata[it])
            print(f"Максимальное значение за выбранный период - {max(res)}")

        def avg_val_by_dates(self, stdate, enddate):
            try:
                sdate = datetime.datetime.strptime(stdate, "%Y-%m-%d")
                edate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
            except:
                print('Ошибка! Введите даты в формате гггг-мм-дд')
                exit()
            res = []
            for it in self.jsdata:
                if (datetime.datetime.strptime(it, '%Y-%m-%d') >= sdate) and\
                        (datetime.datetime.strptime(it, '%Y-%m-%d') <= edate):
                    res.append(float(self.jsdata[it]))
            avg_val = round(statistics.mean(res), 4)
            print(f"Среднее значение за выбранный период - {avg_val}")


#check
nparser = ParserCBRF()
nparser.start('01.01.2022', '20.06.2023')

xrate = XrateCBRF()
xrate.val_by_date('2023-06-10')
xrate.last_val()
xrate.val_by_dates('2023-05-25', '2023-06-08')
xrate.max_val_by_dates('2023-05-25', '2023-06-08')
xrate.avg_val_by_dates('2023-05-25', '2023-06-08')
