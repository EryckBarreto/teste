"""
Dado a sequência de Fibonacci, onde se inicia 
por 0 e 1 e o próximo valor sempre será a soma dos 
2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva 
um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de 
Fibonacci e retorne uma mensagem avisando se o número 
informado pertence ou não a sequência.
"""

# Defini uma função com a fórmula fibonacci para
# poder verificar se está ou não na sequência

def fibonacci(n):
    
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    entrada = input("Informe um número ou digite 'sair' para encerrar: ")
    
    if entrada.lower() == "sair":
        print("Encerrando...")
        break
    
    # Primeiro fiz o programa verificar se foi "sair" e 
    # depois transformar a string em int
    try:
        numero_usuario = int(entrada)
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue

    # Aqui é para verificar se está ou não na sequência
    pertence = False
    i = 0
    while fibonacci(i) <= numero_usuario:
        if fibonacci(i) == numero_usuario:
            pertence = True
            break
        i += 1

    if pertence:
        print(f"O número {numero_usuario} pertence à sequência Fibonacci.")
    else:
        print(f"O número {numero_usuario} não pertence à sequência Fibonacci.")
