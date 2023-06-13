"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
   (Хеш то що з ліва записувати не потрібно)
"""
# try:
#     with open('text.txt') as file, open('gmail.txt', 'w') as gm_fail:
#         for line in file:
#             if line.strip().endswith('@gmail.com'):
#                 gm_fail.write(line.split()[-1]+'\n')
#                 # print(line.split()[-1], file=gm_fail)
# except Exception as err:
#     print(err)
"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""
import json
from typing import TypedDict
Purchase = TypedDict('Purchase', {'id': int, 'name': str, 'price': int})
class NoteBook():
    def __init__(self):
        self.__file_name = input('Enter filename: ')
        self.__data:list[Purchase] = []
        self.__read_file()
        self.__menu()
    def __read_file(self):
        try:
            with open(self.__file_name) as file:
                self.__data = json.load(file)
        except (Exception,):
            pass
    def __write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__data, file)
        except Exception as err:
            print(err)
    def __get_all(self):
        for item in self.__data:
            print(item)
    def __add(self):
        pk = self.__data[-1]['id']+1 if len(self.__data) else 1
        name = input('Enter name of purchase: ')
        price = self.__input_int('Enter price of purchase: ')
        self.__data.append({'id': pk, 'name': name, 'price': price})
        self.__write_file()
    def __find(self):
        count = 0
        search = input('Enter what you want find: ')
        for item in self.__data:
            for value in item.values():
                if search == str(value):
                    print(item)
                    count += 1
                    break
        if not count:
            print('Not Found')
    def most_expensive(self):
        sorted_data = sorted(self.__data, key=lambda i: i['price'])
        if not sorted_data:
            print('List is empty')
            return
        print(sorted_data[-1])
    def delete(self):
        self.__get_all()
        pk = self.__input_int('Enter id for delete: ')
        index = next((i for i, v in enumerate(self.__data) if v['id']==pk), None)
        if index is None:
            print('Not Found')
            return
        del self.__data[index]
        self.__write_file()
    def __menu(self):
        while True:
            print('1) get all')
            print('2) add')
            print('3) search')
            print('4) most expensive')
            print('5) delete')
            print('9) exit')
            choice = input('Make you choice: ')
            match choice:
                case '1':
                    self.__get_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find()
                case '4':
                    self.most_expensive()
                case '5':
                    self.delete()
                case '9':
                    break
    @staticmethod
    def __input_int(msg)->int:
        while True:
            tmp = input(msg)
            if not tmp.isdigit():
                continue
            return int(tmp)

# NoteBook()


"""
*********Кому буде замало ось завдання з співбесіди
Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то 
брати наступне з того ж підсписку

в результат має записатись тільки 5 id

з даним списком мае вийти ось такий результат:
res = [1110, 1120, 1130, 1111, 1122]
"""
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

res = []
gens = []
for item in data:
    gens.append(i['id'] for i in item if i['id'] not in res)
print(gens)
while gens and len(res) < 5:
    gen = gens.pop(0)
    try:
        res.append(next(gen))
    except StopIteration:
        continue
    gens.append(gen)

print(res)