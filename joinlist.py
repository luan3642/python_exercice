#unir duas listas

lista = [1.2,3,4]

lista2 = ["luan", "marcos"]


juncao_lista = lista + lista2

print(juncao_lista)

#usando o metodo append
for x in lista:
    lista2.append(x)

print(lista2)


# usando o extend para adicionar no final da lista
lista.extend(lista2)
print(lista)