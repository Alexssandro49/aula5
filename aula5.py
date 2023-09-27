#encoding: latin-1

#Todas as questões feitas estão neste arquivo

#Crie uma lista com os números de 1 a 10 usando compreensão de lista.
numeros = [i for i in range(1, 11)]
print(numeros)

#Crie uma lista com os números ímpares de 1 a 50.
print("\n")
numeros_impares = [i for i in range(1, 51) if i % 2 != 0]
print(numeros_impares)

#Crie uma lista com as letras maiúsculas de uma string qualquer.
print("\n")
texto = "Teste Aqui as Palavras com inicial MaiúScULas"
letras_maiusculas = [char for char in texto if char.isupper()]
print(letras_maiusculas)

#Crie uma lista com o comprimento de cada palavra em uma string.
print("\n")
texto = "Teste Aqui as Palavras comprimento das Palavras"
comprimentos = [len(palavra) for palavra in texto.split()]
print(comprimentos)

#Crie uma lista com os números divisíveis por 3 e 5 de 1 a 30.
print("\n")
numeros_divididos = [i for i in range(1, 30) if i % 3 == 0 and i % 5==0]
print(numeros_divididos)

#Crie uma lista com as palavras de uma string que tenham mais de 3 letras.
print("\n")
texto = "Crie uma lista com as palavras de uma string que tenham mais de 3 letras"
palavras_maior_de_3 = [palavra for palavra in texto.split() if len(palavra)>3]
print(palavras_maior_de_3)

 #Crie uma lista com os números primos de 1 a 20.
print("\n")
def primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
primos = [i for i in range(1, 21) if primo(i)]
print(primos)

#Crie uma lista com as datas de todos os dias de janeiro em um ano bissexto
print("\n")
ano = 2020
datas_janeiro = [f"{dia:02}/01/{ano}" for dia in range(1, 32) if ano % 4 == 0]
print(datas_janeiro)

#Crie uma lista de strings com os primeiros 10 nomes da lista de nomes.
print("\n")
lista_de_nomes=["Ana","Bruno","Carla","Diego","Elena","Fábio","Gabriela","Hugo","Iris","João","Karla","Lucas","Maria","Nelson","Olívia"]
nomes=[lista_de_nomes[i] for i in range(10)]
print(nomes)

#Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas com as primeiras letras maiúsculas.
print("\n")
lista_de_nomes=["Ana","Bruno","carla","diego","Elena","fábio","Gabriela","hugo","Iris","João","Karla","Lucas","Maria","Nelson","Olívia"]
nomes = [nome for nome in lista_de_nomes if nome[0].isupper()]
nomes = nomes[:10]
print(nomes)

#Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas sem as vogais.
print("\n")
nomes=[lista_de_nomes[i].translate(str.maketrans('', '', 'aeiouáéíóúãõAEIOUÁÉÍÓÚÃÕ')) for i in range(10) ]
print(nomes)

#Concatenar elementos de sub-listas em uma única lista
print("\n")
listas = [[1, 2, 3],[4, 5],[6, 7, 8, 9]]
lista_concatenada = [item for sublista in listas for item in sublista]
print(lista_concatenada)

#Criar um dicionário a partir de duas listas
print("\n")
chaves = ['a', 'b', 'c']
valores = [1, 2, 3]
dicionario = {chave: valor for chave, valor in zip(chaves, valores)}
print(dicionario)