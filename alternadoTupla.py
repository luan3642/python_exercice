# alterando items usando a gambiarra

tupla_nomes = ["marcos", "luan"]

y = list(tupla_nomes)

tupla_nomes[0] = "caroline"

z = tuple(tupla_nomes)

for x in z:
    print(x)


# adicionando um item a uma tupla
    
tupla_carros = ["Honda", "toyota"]
lista = list(tupla_carros)
lista.append("fiat")

tupla_nova = tuple(lista)

print(tupla_nova)


# adicionando de outra forma

tupla_new = ("luan",)

x = ("caroline",)

tupla_new += x
print(tupla_new)


#removendo um item da tupla

dogs = ("pug", "golden retriver")
dogs_list = list(dogs)
dogs_list.remove("pug")

dogs_tuple_changeable = tuple(dogs_list)

print(dogs_tuple_changeable)

#deleta a tupla por completo

del(dogs_tuple_changeable)

print(dogs_tuple_changeable)
