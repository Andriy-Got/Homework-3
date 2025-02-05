from datetime import datetime #Бібліотека для першого завдання
import random #Бібліотека для другого завдання
import re #Бібліотека для Третього завдання
"""
Завдання № 1
"""
print(f"Завдання №1")
def get_days_from_today(date): #Функція яка обчислює кількість днів між сьогоднішньою датою і датою користувача
    user_day=datetime.strptime(date,"%Y-%m-%d").date() #Переводимо рядок у формат Date
    now=datetime.now().date() #дізнаєомсь сьогоднію дату
    return   (now-user_day).days
print(get_days_from_today("2022-11-10")) #Виклик функції

"""
 Завдання № 2
"""
print(f"Завдання №2")
def get_numbers_ticket(min, max, quantity):#Функція котра обирає задану кількість унікльних елмеентів
    number=set()
    while len(number)<quantity:#Цикл працює задану кількість разів
        number.add(random.randint(min,max)) #Додаємо до множини елементи

    return sorted(number)#Сортуємо і зберігаємо результат

print(get_numbers_ticket(1,9,4)) #Виклик функції
"""
Завдання № 3
"""
print(f"Завдання №3")
def normalize_phone(phone_number):#Функція яка очищає номери
    for phone in  phone_number:
        normal_phone=re.sub(r"\D+","",phone_number) #видаляємо зайві символи
        if not normal_phone.startswith("+"):#перевірка чи містить номер +
            if normal_phone.startswith("38"):
                normal_phone="+" + normal_phone
            else:
                normal_phone="+38" + normal_phone
        return normal_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)