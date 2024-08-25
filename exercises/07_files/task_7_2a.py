# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv


ignore = ["duplex", "alias", "configuration"]
file_name = argv[1]


with open(file_name) as file:
    for line in file:
        #print(all([line.find(word) == -1 for word in ignore]))
        if not line.startswith('!') and all([line.find(word) == -1 for word in ignore]) is True:
             print(line.rstrip())

