# Взять строку и посчитать сколько там слов
txt1 = 'Google создаст специальную команду для поиска багов в особо важных приложениях'
print(len(txt1.split(' ')))

# Взять строку и поделить её по пробелам и узнать тип данных каждого слова
txt2 = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'" 
txt2 = txt2.split(' ')
my_list = []
for i in txt2:
    try:
        my_list.append(float(i))
    except:
        my_list.append(i)

for i in my_list:
    print(type(i))

# Взять строку и сделать каждое её слово с большой буквы
txt3 = 'Хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(txt3.upper())

# Спросить у пользователя символ и поделить стоку по этому символу
txt4 = 'GitHub'
user_char = input('Введите символ: ') 
print(txt4.join(user_char))

# Взять строку и заменить все буквы Е на число 3
txt5 = 'Ботнет IPStorm, в которой ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
print(txt5.replace('е', '3'))

# Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом
txt6 = 'Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом'
first_part = txt6[0:int(len(txt6)/2)]
second_part = txt6[int(len(txt6)/2) : len(txt6)-1]
print(first_part.lower() + second_part.upper())

#Сделать из булева значения True - строку
txt7 = True
print(str(txt7))