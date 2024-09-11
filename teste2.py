fibonacci = [0, 1]
numero = 89

while numero not in fibonacci and numero > fibonacci[-1]:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if numero in fibonacci:
    print(f'O número {numero} está na sequencia de fibonacci')
if numero < fibonacci[-1]:
    print(f'O número {numero} NÃO está na sequencia de fibonacci')
