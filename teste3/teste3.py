import json


class Faturamento:
    def __init__(self, caminho):
        self.caminho = caminho
    
        with open (self.caminho, 'r', encoding='utf8') as dias:
            self.registros = json.load(dias)


    def maior_faturamento(self):
        maior_faturamento = 0

        for registro in self.registros:
            valor_atual = registro['valor']

            if valor_atual > 0 and valor_atual > maior_faturamento:
                    maior_faturamento = valor_atual

        return maior_faturamento
    
    def menor_faturamento(self):
        menor_faturamento = 0
        for registro in self.registros:
            valor_atual = registro['valor']
            if (valor_atual > 0 and valor_atual < menor_faturamento) or menor_faturamento == 0:  
                menor_faturamento = valor_atual

        return menor_faturamento
    
    def media_faturamento(self):
        qtde_registros = 0
        total_faturamento = 0
        media = 0
        for registro in self.registros:
            valor_atual = registro['valor']

            if valor_atual > 0:
                qtde_registros += 1
                total_faturamento += valor_atual


        media = total_faturamento / qtde_registros

        return media

    def dias_superiores(self):
        media = self.media_faturamento()
        melhores_dias = 0
        for registro in self.registros:
            valor_atual = registro['valor']
            if valor_atual > media:
                melhores_dias += 1
        print(melhores_dias)
        return melhores_dias

try:    
    janeiro = Faturamento('teste2\\dados.json')
except FileNotFoundError:
    raise FileNotFoundError('Arquivo não encontrado, digite corretamente o caminho do arquivo')
except:
    raise Exception('Erro desconhecido, verifique a entrada do arquivo e tente novamente')

maior_faturamento = janeiro.maior_faturamento()
menor_faturamento = janeiro.menor_faturamento()
media_faturamento = janeiro.media_faturamento()
melhores_dias = janeiro.dias_superiores()

print('O maior faturamento do mês foi:', maior_faturamento)
print('O menor faturamento do mês foi:', menor_faturamento)
print('A media de faturamento foi:', media_faturamento)
print(f'O faturamento foi acima da média em {melhores_dias} dias')
