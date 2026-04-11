from collections import Counter

#Pesquisa de opniao 


# Entrada
opinioes_coletadas = []

for i in range(10):
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    print('\n{}, qual sua opinião sobre o atendimento prestado?'.format(nome))
    print(' Excelente \n Bom \n Ruim')
    
    res = input(': ').strip().upper()
    
    while res not in ['EXCELENTE', 'BOM', 'RUIM']:
        res = input('Responda apenas com Excelente, \n Bom, \n ou Ruim \n : ').strip().upper()
    
    # Adiciona a resposta validada à lista
    opinioes_coletadas.append(res)
    print('Agradecemos sua opinião {}, adeus.\n'.format(nome))

# Processamento
contagem = Counter(opinioes_coletadas)

# Saída
print(' RESULTADO DA PESQUISA ')
print('Quantidade de opnioes Excelentes: {}'.format(contagem['EXCELENTE']))
print('Quantidade de opnioes Boas: {}'.format(contagem['BOM']))
print('Quantidade de opnioes Ruins: {}'.format(contagem['RUIM']))
