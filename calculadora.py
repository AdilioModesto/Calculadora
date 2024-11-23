def somar(a, b):
    calculo = a + b
    return f'{a} + {b} = {calculo}'

def subtrair(a,b):
    calculo = a - b
    return f'{a} - {b} = {calculo}'

def multiplicar(a,b):
    calculo = a * b
    return f'{a} * {b} = {calculo}'

def dividir(a,b):
    if b == 0:
        return f"Erro: Divisão por 0"

    calculo = a / b
    return f'{a} / {b} = {calculo}'

def erro():
    print()
    print("Entrada Invalida")
    print("Digite novamente \n")


opcoes = [1, 2, 3, 4]

while True:
    try:
        print(" 1-Somar \n 2-Subtrair \n 3-Multiplicar \n 4-Dividir \n")

        opcao_escolhida = int(input("Digite uma das opcões acima que deseja usar: "))

        if opcao_escolhida not in opcoes:
            erro()
            continue
        
        a = int(input('Numero 1: '))
        b = int(input('Numero 2: '))

        if opcao_escolhida == 1:
            print(somar(a,b))
        elif opcao_escolhida == 2:
            print(subtrair(a,b))
        elif opcao_escolhida == 3:
            print(multiplicar(a,b))
        else:
            print(dividir(a,b))
        
        continuar = input("Deseja Continuar: ")
        if continuar.lower() != 'sim':
            break
    except:
        erro()

print("Calculadora encerrada")