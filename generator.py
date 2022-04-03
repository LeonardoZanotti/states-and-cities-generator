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
    'Tocantins',
    'Distrito Federal'
]

ufs = [
    'AC',
    'AL',
    'AP',
    'AM',
    'BA',
    'CE',
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
    'TO',
    'DF'
]

for i, state in enumerate(states):
    print("INSERT INTO tb_estado(nome_estado, sigla_estado)\nVALUES ('{}', '{}');\n".format(
        state, ufs[i]))


df = pd.read_csv('cities.csv', sep=';', encoding='latin-1').iloc[:, 0]

for row in df:
    print("INSERT INTO tb_cidade(nome_cidade, id_estado)\nVALUES ('{}', {});\n".format(
        row[2:], ufs.index(row[:2]) + 1))
