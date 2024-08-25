# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt') as file:
    for line in file:
        line = line.split()
        max_len = len("Outbound Interface    ")
        prefix, metric, netx_hop, last_update, outbound = line[1], line[2].strip('[]'), line[4].replace(',', ' '), line[5].replace(',',' '), line[6]
        print('Prefix'.ljust(max_len), prefix, '\nAD/Metric'.ljust(max_len), metric, '\nNext-Hop'.ljust(max_len), netx_hop,
              '\nLast update'.ljust(max_len), last_update, '\nOutbound Interface'.ljust(max_len), outbound)
        print()