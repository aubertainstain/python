import math

def soma():
    while True:
        print("\nOPERACAO: SOMA\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite a primeira parcela: "))
        if num1 == -0:
            break
        num2 = float(input("Digite a segunda parcela: "))
        total = num1 + num2
        print(f"RESULTADO: {num1:.2f} + {num2:.2f} = {total:.2f}")

def subtracao():
    while True:
        print("\nOPERACAO: SUBTRACAO\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite a primeira parcela: "))
        if num1 == -0:
            break
        num2 = float(input("Digite a segunda parcela: "))
        total = num1 - num2
        print(f"RESULTADO: {num1:.2f} - {num2:.2f} = {total:.2f}")

def multiplicacao():
    while True:
        print("\nOPERACAO: MULTIPLICACAO\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite o primeiro numero: "))
        if num1 == -0:
            break
        num2 = float(input("Digite o segundo numero: "))
        total = num1 * num2
        print(f"RESULTADO: {num1:.2f} x {num2:.2f} = {total:.2f}")

def divisao():
    while True:
        print("\nOPERACAO: DIVISAO\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite o primeiro numero: "))
        if num1 == -0:
            break
        num2 = float(input("Digite o segundo numero: "))
        if num2 != 0:
            total = num1 / num2
            print(f"RESULTADO: {num1:.2f} : {num2:.2f} = {total:.2f}")
        else:
            print("Nao existe divisao por zero!")

def potenciacao():
    while True:
        print("\nOPERACAO: POTENCIACAO\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite o numero: "))
        if num1 == -0:
            break
        n = float(input("Digite o indice: "))
        total = math.pow(num1, n)
        print(f"RESULTADO: {num1:.2f} elevado a {n:.2f} = {total:.2f}")

def radiciacao():
    while True:
        print("\nOPERACAO: RADICIACAO\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite um numero: "))
        if num1 == -0:
            break
        if num1 >= 0:
            n = float(input("Digite o indice: "))
            if n > 0:
                total = math.pow(num1, 1/n)
                print(f"RESULTADO: A raiz {n:.2f} de {num1:.2f} vale {total:.2f}")
            else:
                print("Nao existe raiz com indice negativo!")
        else:
            print("Nao existe raiz de numero negativo.")

def porcentagem():
    while True:
        print("\nOPERACAO: PORCENTAGEM\nOBS.:Digite -0 para sair")
        num1 = float(input("Digite um numero: "))
        if num1 == -0:
            break
        n = float(input("Digite a porcentagem: "))
        if n >= 0:
            total = (num1 * n) / 100
            print(f"RESULTADO: {n:.2f} por cento de {num1:.2f} vale {total:.2f}")
        else:
            print("Nao existe porcentagem negativa!")

def main():
    while True:
        print("\n>>>>CALCULADORA<<<<\nAutor: Lucas Pereira\nEstudante do curso técnico de Análise e Desenvolvimento de Sistemas")
        print("\n\tMENU DE OPCOES\nDigite + para adicao\nDigite - para subtracao\nDigite x para multiplicacao")
        print("Digite / para divisao\nDigite p para potenciacao\nDigite r para radiciacao\nDigite c para porcentagem\nDigite s para sair\n")
        opcao = input(">>> ").strip().lower()
        
        if opcao == '+':
            soma()
        elif opcao == '-':
            subtracao()
        elif opcao == 'x':
            multiplicacao()
        elif opcao == '/':
            divisao()
        elif opcao == 'p':
            potenciacao()
        elif opcao == 'r':
            radiciacao()
        elif opcao == 'c':
            porcentagem()
        elif opcao == 's':
            print("Saindo da calculadora!")
            break
        else:
            print("Opcao Invalida!")

if __name__ == "__main__":
    main()
