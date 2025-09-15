"""
O programa permite que o usuário gerencie uma lista de números digitados.
Ele pode adicionar números, que são automaticamente organizados em listas de pares e ímpares e mantém
a soma total atualizada. Também é possível excluir números, removendo-os da lista principal
e da lista correspondente de pares ou ímpares. Quando o usuário decide sair, o programa mostra a lista final,
o maior e menor número, os números pares e ímpares e a soma total. Se não houver números digitados,
avisa que a lista está vazia.
"""


# Lista principal e listas auxiliares
numeros = [] # guarda todos os números
list_par = []  # guarda apenas os pares
list_impar = []  # guarda apenas os ímpares
soma = 0  # acumula a soma de todos os números

# Loop infinito até o usuário digitar "sair"
while True:

    # Pergunta a ação do usuário
    pessoa = input("Digite adicionar, excluir ou sair: ").lower()

    # Caso o usuário queira adicionar um número
    if pessoa == "adicionar":
        numero = int(input("Digite o numero que deseja adiconar: "))

        # Adiciona à lista principal
        numeros.append(numero)
        numeros.sort() # Mantém a lista sempre ordenada

        # Classifica em par ou ímpar
        if numero % 2 == 0:
            list_par.append(numero)
            list_par.sort()

        else:
            list_impar.append(numero)
            list_impar.sort()

        # Atualiza a soma total
        soma += numero

        # Mostra o resultado parcial
        print(f"Numero {numero} Adicionado com sucesso!")
        print(f"Lista completa: {numeros}")
        print(f"Pares: {list_par}")
        print(f"Ímpares: {list_impar}")


    # Caso o usuário queira excluir um número
    elif pessoa == "excluir":

        # Remove um número da lista, se existir
        numero_remover = int(input("Digite o numero que deseja remover: "))
        if numero_remover in numeros:
            numeros.remove(numero_remover)

            # Remove também da lista de pares ou ímpares correspondente
            if numero_remover % 2 == 0 and numero_remover in list_par:
                list_par.remove(numero_remover)

            elif numero_remover % 2 == 0 and numero_remover in list_impar:
                list_impar.remove(numero_remover)

            print(f"{numero_remover} removido com sucesso!")


        else:
            print(f"Numero {numero_remover} não esta na lista")
            print(f"{numeros}")

    # Caso o usuário queira encerrar o programa
    elif pessoa == "sair":
        print("Encerrando o programa... " )

        if numeros: # só mostra estatísticas se houver números

            print(f"Lista final: {numeros}")
            print(f"O maior número foi {max(numeros)} e o menor foi {min(numeros)}")
            print(f"Numeros digitados par: {list_par}")
            print(f"Numeros digitados impar: {list_impar}")
            print(f"Soma total dos números: {soma}")

        else:
            print("Nenhum número foi digitado.")

        break # sai do while True e termina o programa

    # Caso o usuário digite algo inválido
    else:
        print("Opção inválida! Digite 'adicionar', 'excluir' ou 'sair'.")