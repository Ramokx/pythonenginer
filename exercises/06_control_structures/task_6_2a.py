# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input()

octets = [num for num in ip.split('.')]
correct_ip = True
if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        if not octet.isdigit() or int(octet) > 255 or int(octet) < 0:
            correct_ip = False
if correct_ip is False:
    print("Неправильный IP-адрес")
else:
    octets = [int(oct) for oct in octets]
    if ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    elif 1 <= octets[0] <= 223:
        print('unicast')
    elif 224 <= octets[0] <= 239:
        print('multicast')
    else:
        print('unused')
