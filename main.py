# Import
import random

# Função de soma dos números
def soma(cpf, multiplicador):
    total = 0
    for numero in cpf:
        total += int(numero) * multiplicador
        multiplicador -= 1
    resto = total % 11 

    if resto < 2:
        return '0'
    
    return str(11 - resto)

# Função de gerar o cpf
def gerador():
    # Gerando os 9 primeiros digitos em formato de string
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))

    # 10º digito
    cpf += soma(cpf, 10)

    # 11º digito
    cpf += soma(cpf, 11)

    # Formatando
    cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    # Print, return, qualquer forma que você quiser de usar!
    print(cpf)

gerador()