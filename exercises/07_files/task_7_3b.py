# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_in = input('Enter VLAN number: ')
#result = {}
with open('CAM_table.txt') as file:
    for line in file:
        data = line.split()
        if data and data[0].isdigit() and data[0] == vlan_in:
            vlan, mac, ports = int(data[0]), data[1], data[-1]
            print(f'{vlan:<10}{mac:20}{ports:8}')


            #это для словаря
            #result.setdefault(vlan, []).append([vlan, mac, ports])

#for item in result[vlan_in]:
   # print('{:<10}{:20}{:8}'.format(*item))
