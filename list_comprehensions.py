valores = [x**2 for x in range(10)]


print(valores)


print(len(valores))


#checking elements in list

if 9 in valores:
    print("tem valor")


xs = [x for x in range(10)]

print(xs)


# imprimindo valores menores que 5

print([c for c in range(1,20) if c <= 5])

frutas = ["maca", "banana", "morango"]

new_fruits = [fruta.upper() for fruta in frutas]

print(new_fruits)