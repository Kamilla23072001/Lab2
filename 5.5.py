code = int(input('Введите код города:'))
min = int(input('Введите количество минут:'))

if code == 343:
    res = 15*min
    print('Екатеринбург, стоимость переговоров составляет -', res, 'рублей')
elif code == 381:
    res = 18*min
    print('Омск, стоимость переговоров составляет -', res, 'рублей')
elif code == 473:
    res = 13*min
    print('Воронеж, стоимость переговоров составляет -', res, 'рублей')
elif code == 485:
    res = 11*min
    print('Ярославль, стоимость переговоров составляет -', res, 'рублей')

"""Программа рассчитывает стоимость переговоров для каждого города в зависимости от количества минут"""
