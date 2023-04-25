# Método 1

# entrada = input("Digite uma palavra ou frase: ")
# entrada_invertida = entrada[::-1]
# print(entrada_invertida)

# Método 2

def inverte_string(string):
    if len(string) == 0:
        return string
    else:
        return inverte_string(string[1:]) + string[0]

entrada = input("Digite uma palavra ou frase: ")
inverso_string = inverte_string(entrada)
print(inverso_string)
