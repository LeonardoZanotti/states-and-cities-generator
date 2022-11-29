#!/usr/bin/env python3
import csv

import pandas as pd

states = [
    'Acre',
    'Alagoas',
    'Amapá',
    'Amazonas',
    'Bahia',
    'Ceará',
    'Distrito Federal',
    'Espírito Santo',
    'Goiás',
    'Maranhão',
    'Mato Grosso',
    'Mato Grosso do Sul',
    'Minas Gerais',
    'Pará',
    'Paraíba',
    'Paraná',
    'Pernambuco',
    'Piauí',
    'Rio de Janeiro',
    'Rio Grande do Norte',
    'Rio Grande do Sul',
    'Rondônia',
    'Roraima',
    'Santa Catarina',
    'São Paulo',
    'Sergipe',
    'Tocantins'
]

ufs = [
    'AC',
    'AL',
    'AP',
    'AM',
    'BA',
    'CE',
    'DF',
    'ES',
    'GO',
    'MA',
    'MT',
    'MS',
    'MG',
    'PA',
    'PB',
    'PR',
    'PE',
    'PI',
    'RJ',
    'RN',
    'RS',
    'RO',
    'RR',
    'SC',
    'SP',
    'SE',
    'TO'
]

# sql
# for i, state in enumerate(states):
#     print("('{}', '{}'),".format(
#         ufs[i], state))

# json
# for i, state in enumerate(states):
#     print("{" + "\"id\": {}, \"nome\": \"{}\", \"sigla\": \"{}\"".format(i+1, state, ufs[i]) + "},")

df = pd.read_csv('cities.csv', sep=';', encoding='latin-1').iloc[:, 0]

i = 1

# sql
# for row in df:
#     print("({}, '{}', {}),".format(i, row[2:].replace(
#         '\'', '\'\''), ufs.index(row[:2]) + 1))
#     i += 1

# json
for row in df:
    print("{" + "\"id\": {}, \"nome\": \"{}\", \"estado\": {}".format(i, row[2:], ufs.index(row[:2]) + 1) + "},")
    i += 1


# for i, state in enumerate(states):
#     print("INSERT INTO tb_estado(nome_estado, sigla_estado)\nVALUES ('{}', '{}');\n".format(
#         state, ufs[i]))


# df = pd.read_csv('cities.csv', sep=';', encoding='latin-1').iloc[:, 0]

# for row in df:
#     print("INSERT INTO tb_cidade(nome_cidade, id_estado)\nVALUES ('{}', {});\n".format(
#         row[2:].replace('\'', '\'\''), ufs.index(row[:2]) + 1))
