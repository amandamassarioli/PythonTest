print("Bem-vindo a calculadora!")
print("Qual operação deseja fazer? Responda apenas número")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

resposta = int(input())

if resposta == 1:
    n1 = int(input())
    n2 = int(input())
    print(n1+n2)

if resposta == 2:
    n1 = int(input())
    n2 = int(input())
    print(n1-n2)

if resposta == 3: 
    n1 = int(input())
    n2 = int(input())
    print(n1*n2)

if resposta == 4:
    n1 = int(input())
    n2 = int(input())
    print(n1/n2)

    