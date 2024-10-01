resposta = 3 
while (resposta != 0):
    print("Bem-vindo ao menu da calculadora!")
    print("Qual operação deseja fazer? Responda apenas número")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Encerrar")

    resposta = int(input("Opção: "))

    if resposta == 0:
        break

    elif resposta == 1:
        n1 = int(input("Digite o primeiro número para somar: "))
        n2 = int(input("Digite o segundo número para somar: "))
        print("Resposta da soma: ",n1+n2) 

    elif resposta == 2:
        n1 = int(input("Digite o primeiro número para subtrair: "))
        n2 = int(input("Digite o segundo número para subtrair: "))
        print("Resposta da subtração: ",n1-n2)

    elif resposta == 3: 
        n1 = int(input("Digite o primeiro número para multiplicar: "))
        n2 = int(input("Digite o segundo número para multiplicar: "))
        print("Resposta da multiplicação: ",n1*n2)

    elif resposta == 4:
        n1 = int(input("Digite o primeiro número para dividir: "))
        n2 = int(input("Digite o segundo número para dividir: "))
        print("Resposta da divisão: ",n1/n2) 

    else:
        print("Resposta inválida! Digite uma opção de 1 a 4.")

    






