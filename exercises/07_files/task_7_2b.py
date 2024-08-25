# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv


ignore = ["duplex", "alias", "configuration"]
file_name = argv[1]
file_out = argv[2]


with open(file_name) as file, open(file_out, 'w') as fileout:
    for line in file:
        if not line.startswith('!') and all([line.find(word) == -1 for word in ignore]) is True:
             fileout.write(line)