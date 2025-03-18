import random

class RandomHelper:
    @staticmethod
    def get_name():
        names = ["Иван", "Артём", "Игорь", "Лев", "Ярослав", "Макс", "Егор"]
        return  random.choice(names)

    @staticmethod
    def get_surname():
        names = ["Ивано", "Петров", "Красов", "Черный", "Козлов", "Красивый", "Жук"]
        return random.choice(names)

    @staticmethod
    def get_address():
        street = ["Ленина", "Пушкина", "Красная", "Белая", "Большой", "Лесная", "Тупичок"]
        return f"улица {random.choice(street)}, {random.randint(1,100)}, кв.{random.randint(1,100)}"


    @staticmethod
    def get_phone():
        phone = [ "84961234567", "+79675688990"]
        return random.choice(phone)
