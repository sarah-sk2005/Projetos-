# Programa de consumo mensal
#Autor: Sarah Ketlyn Teixeira da Silva Santos

# Entrada
print(' Olá, hoje irei te ajudar a descocrir o consumo mensal do seu aparelho')
nome = input(' Qual seu nome ? ')
aparelho = input('Por favor me diga o nome do seu aparelho: ')
potencia = int(input('Qual a potência em watts do aparelho {} ? '.format(aparelho)))
tempo = int(input('Quantas horas o aparelho {} é usado por dia ? '.format(aparelho)))

#Processamento
consumoMensal = (potencia*tempo*30)/1000
custo = (0.75*consumoMensal)

#Saída
print('O aparelho {} de {}W tem um consumo mensal de {} kWh, com um custo mensal estimado de R$ {:.2f}! '.format(aparelho,potencia,consumoMensal,custo))
print('Agradeço pela preferencia, tenha um bom dia {} !'.format(nome))