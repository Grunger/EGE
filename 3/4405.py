import csv

# ['Код', 'Название', 'Код страны', 'Район', 'Население']
cities = list(csv.reader(open('cities.csv')))[1:]
# ['Код', 'Название', 'Континент', 'Регион', 'Площадь', 'Год независимости',
# 'Население', 'ОПЖ', 'ВНД', 'ВНД_пред', 'Форма правления', 'Код столицы']
countries = list(csv.reader(open('countries.csv')))[1:]
# ['Код', 'Название', 'Код страны', 'Официальный', 'Процент']
langs = list(csv.reader(open('langs.csv')))[1:]

capitals = {country[11] for country in countries}
countries_more_10 = {country[0] for country in countries if
                 len([lang[2] for lang in langs if lang[2] == country[0] and float(lang[4].replace(',', '.')) > 10]) >= 2}
k = 0
for city in cities:
    if city[0] in capitals and int(city[4]) >= 100000 and city[2] in countries_more_10:
        k += 1
print(k)
