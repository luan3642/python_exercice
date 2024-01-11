my_tuple = (1, "hello", 3.4)

print(my_tuple[0])


print(len(my_tuple))


#tupla aninhada

nested_tuple = (1, (1,2,3), ["luan", "jorge"])

nested_tuple[2].append("lucas")

print(len(nested_tuple))

#tuple only item

single_item_tuple = (50,)

print(len(single_item_tuple))


#desempacotar uma tupla

tuplss = (20, 10, 30)

x,y,z = tuplss


print(x,y,z)