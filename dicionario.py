#criando um dicionario 

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


# acessando um item
print(my_dict["model"])


#adicionando novo item

my_dict["color"] = "red"


#modificando um valor

my_dict["year"] = 2020


#removendo um item

del my_dict["brand"]


#iterando sobre o dicionario

for key in my_dict:
    print(key, my_dict[key])