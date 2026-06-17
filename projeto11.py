#               Controle de níveis de água

#                        Entrada
import colorama
from colorama import Fore, Style

niveis = [
    ['Crítco', 1, Fore.RED],
    ['Baixo', 2, Fore.YELLOW],
    ['Médio', 3, Fore.GREEN],
    ['Alto', 4, Fore.CYAN],
    ['Muito Alto', 5, Fore.BLUE]
]

#                      Processamento
def controle_de_niveis():
    try:
        while True:
#dado coletado do usuário podendo ser substituido por dado de sensor
            nivel_digitado = int(input("digite o nível mostrado: ")) 
            lista_dos_niveis = [nivel[1] for nivel in niveis]
            nivel_encontrado = nivel_digitado in lista_dos_niveis

            if nivel_encontrado:
                for nivel in niveis:
                    situacao_do_nivel = nivel[0]
                    numero_do_nivel = nivel[1]
                    cor_do_nivel = nivel[2]

                    if nivel_digitado == numero_do_nivel:
                        print(cor_do_nivel, "Atenção o nivel da água está", situacao_do_nivel, Style.RESET_ALL)

                break
            else:
                print(" O nível", nivel_digitado, "não é existente.\n Favor atentar-se a digitar um nível de água existente !!")
    except ValueError:
         print("Favor digitar números existentes e inteiros.")
#                          Saída
controle_de_niveis()