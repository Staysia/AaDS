'''
Задание:
1.Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников:
https://tproger.ru/translations/the-best-datasets-for-machine-learning-and-data-science/
https://vc.ru/ml/150241-15-proektov-dlya-razvitiya-navykov-raboty-s-mashinnym-obucheniem
https://archive.ics.uci.edu/ml/index.php
https://habr.com/ru/company/edison/blog/480408/
https://www.kaggle.com/datasets/
2.Для прочитанного набора выполнить обработку в соответствии со своим вариантом. Библиотекой pandas пользоваться нельзя.

23.	Определить количество пассажиров на борту минимального и максимального возраста и сколько из них выжило.
'''



import csv

# Чтение данных из CSV файла
with open('titanic.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Считаем, что первая строка - это заголовок
    data = list(reader)  # Считываем все данные в список

# Индексы нужных колонок
age_index = header.index('Age')
survived_index = header.index('Survived')

# Списки для хранения возраста и информации о выживании
ages = []
survived = []

# Заполнение списков данными
for row in data:
    if row[age_index]:  # Проверяем, что возраст не пустой
        ages.append(float(row[age_index]))  # Добавляем возраст в список
        survived.append(int(row[survived_index]))  # Добавляем информацию о выживании

# Находим минимальный и максимальный возраст
min_age = min(ages)
max_age = max(ages)

# Подсчет количества пассажиров с минимальным и максимальным возрастом
count_min_age = sum(1 for a in ages if a == min_age)
count_max_age = sum(1 for a in ages if a == max_age)

# Подсчет выживших среди пассажиров с минимальным и максимальным возрастом
survived_min_age = sum(1 for i, a in enumerate(ages) if a == min_age and survived[i] == 1)
survived_max_age = sum(1 for i, a in enumerate(ages) if a == max_age and survived[i] == 1)

# Вывод результатов
print(f"Минимальный возраст: {min_age}, Количество пассажиров: {count_min_age}, Выживших: {survived_min_age}")
print(f"Максимальный возраст: {max_age}, Количество пассажиров: {count_max_age}, Выживших: {survived_max_age}")