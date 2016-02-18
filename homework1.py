#! /usr/bin/env python
# -*- coding: utf-8 -*-


import sys #подключаем библиотеку

if sys.version_info[0] == 2: # Если Python 2
    input_function = raw_input
else:
    input_function = input #Во всех других случаях
    
Score = 0 #создаём переменную Score (счет)

print(u'Начнём с простого')

while True:
    user_input = input_function(u'Вопрос 1: Сколько бит в байте? Твой ответ: ')
    if float(user_input) == 8 :
        print(u'\nВерно! В 1 байте %s бит' % user_input)
        Score = Score + 1
        print(u'Попыток: %s' % Score)
        break
    else:
        print(u'\n %s - это неправильно количество бит! Попробуй еще раз' % user_input)
        Score = Score + 1
        print(u'Попыток: %s' % Score)
        continue 
        
if Score == 1:
    print(u"Ответил правильно с первого раза! Тебе точно нужны эти курсы?!!")
else:
    print(u"Не расстраивайся! По окончании курса ты будешь верно отвечать на все вопросы с первой попытки")
    




while True:
    user_input = input_function('\nВопрос 2: Какой тип будет у переменной a = sys.maxsize + 1 в Python 2.7? \nВаш ответ: ')
    if str(user_input) == "long" :
        print('\nВерно! В Python 2.7 есть специальный тип long, для целых чисел, превыщающие sys.maxsize')
        Score = Score + 1
        print('Попыток: %s' % Score)
        break
    else:
        print('\n%s - это неправильно! Попробуй еще раз' % user_input)
        Score = Score + 1
        print('Попыток: %s \n' % Score)
        continue 
    
if Score == 2:
    print("Ты явно программист!!")
else:
    print("Повтори первую лекцию или посмотри различия 2.7 от 3 через гугл")




while True:
    user_input = input_function('\nВопрос 3: Чему будет равна переменная "с" если \na = "World" \nc = a[3]+a[1:2]+a[-1] ? \nВаш ответ: ')
    if str(user_input) == "lord" :
        print('\nВерно! ')
        Score = Score + 1
        print('Попыток: %s' % Score)
        break
    else:
        print('\n%s - это неправильно! Попробуй еще раз' % user_input)
        Score = Score + 1
        print('Попыток: %s \n' % Score)
        continue 

while True:
    user_input = input_function('\nВопрос 4: чему будет равно а = int("100"*2)/2? \nВаш ответ: ')
    if str(user_input) == "50050" :
        print('\n%s - это правильный ответ! ' % user_input)
        Score = Score + 1
        print('Попыток: %s' % Score)
        break
    else:
        print('\n%s - это неправильно! Попробуй еще раз' % user_input)
        Score = Score + 1
        print('Попыток: %s \n' % Score)
        continue 

if Score == 4:
    print('Поздравляю! Ты ответил на все вопросы c первого раза!!! Пора осваивать вторую лекцию! \nОбщее количество попыток %s' % Score)
elif Score > 4 and Score < 8:
    print("Ты справился с моими вопросами за %s попопыток. \nРекомендую пробежаться по первой лекции" % Score)
else:
    print("Повтори первую лекцию или посмотри различия 2.7 от 3 через гугл")







#new comment line