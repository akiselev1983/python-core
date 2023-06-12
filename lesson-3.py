"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін
"""
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = x * y
    def __add__(self, other):
        return self.area + other.area
    def __sub__(self, other):
        return self.area - other.area
    def __eq__(self, other):
        return self.area == other.area
    def __ne__(self, other):
        return self.area != other.area
    def __lt__(self, other):
        return self.area > other.area
    def __gt__(self, other):
        return self.area < other.area
    def __len__(self):
        return (self.x + self.y) * 2

s = Rectangle(5, 7)
s1 = Rectangle(2, 3)
print(s + s1)
print(s > s1)
print(s != s1)
#############################################################################
"""
створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення
"""
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, size_foot):
        super().__init__(name, age)
        self.size_foot = size_foot
        Cinderella.__count += 1
    @classmethod
    def get_count(cls):
        print(cls.__count)
class Prince(Human):
    def __init__(self, name, age, size_shoe):
        super().__init__(name, age)
        self.size_shoe = size_shoe

    def  find_cinderella(self, cinderellas:list[Cinderella]):
        for cinderella in cinderellas:
            if self.size_shoe == cinderella.size_foot:
                print(cinderella.__dict__)
                return
        print("Not found!!!")




cinderellas = [Cinderella('Olha', 25, 34), Cinderella('Sveta', 22, 32),Cinderella('Kamila', 29, 37),Cinderella('Tania', 28, 36)]
prince= Prince('Max', 30, 34)
prince.find_cinderella(cinderellas)
###############################################################################
"""
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом
  Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
Приклад:
Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))
    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
"""
from abc import ABC, abstractmethod
class Printable(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def print(self):
        pass
class Book(Printable):

    def print(self):
        print(f'Book: {self.name}')
class Magazine(Printable):

    def print(self):
        print(f'Magazine: {self.name}')
class Main:
    __printable_list:list[Printable] = []
    @classmethod
    def add(cls, item:Printable):
        if isinstance(item, Printable):
            cls.__printable_list.append(item)
        else:
            print("Ignored!!!")
    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()
class Car():
    pass

Main.add(Car())
Main.add(Magazine('magazine1'))
Main.add(Magazine('magazine2'))
Main.add(Magazine('magazine3'))
Main.add(Magazine('magazine4'))
Main.add(Book('book1'))
Main.add(Book('book2'))
Main.add(Book('book3'))

Main.show_all_books()
Main.show_all_magazines()


"""    
для перевірки ксассів використовуємо метод isinstance, приклад:


user = User('Max', 15)
shape = Shape()

isinstance(max, User) -> True
isinstance(shape, User) -> False
"""