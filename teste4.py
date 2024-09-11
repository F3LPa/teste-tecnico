faturamento_mensal = [
    {'nome': 'SP', 'valor': 67836.43, 'percentual': 0},
    {'nome': 'RJ', 'valor': 36678.66, 'percentual': 0},
    {'nome': 'MG', 'valor': 29229.88, 'percentual': 0},
    {'nome': 'ES', 'valor': 27165.48, 'percentual': 0},
    {'nome': 'Outros', 'valor': 19849.53, 'percentual': 0}
    ]

total_mensal = 0
for estado in faturamento_mensal:
    total_mensal += estado['valor']

print('Percentual de representação de cada estado no faturamento mensal:')
for estado in faturamento_mensal:
    estado['percentual'] = (estado['valor'] / total_mensal) * 100
    print(f'{estado['nome']} | {estado['percentual']:.2f}%')

print()