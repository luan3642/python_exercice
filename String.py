nome = "luan"

print(nome.upper())


lastNome = "MAGALHAES"

print(lastNome.lower())


#removedor de espacos do inico ao fim

string = " luan magalhaes "

print(string.strip())


print(string.replace("l", "x"))


carros = "jaguar, polo, gol"


nova_lista = carros.split(",")

print(nova_lista)



#concatenar string


a = "hello"
b = "world"


junta = a +" "+ b

print(junta)



# nao pode combinar string e int junto

# mas pode combinar usando o format

idade = 10
nomex = "ben {}"

print(nomex.format(idade))


# podemos usar caracter de escape para colocar aspas duplas numa string

xxx = "luan \" senior \"cargo"


print(xxx)