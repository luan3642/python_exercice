my_list = [1,5,6,98,5]

names = ["luan", "marcos", "jose"]


mixed_list = ["luan", 1.5, "hello", True]


print(mixed_list[0])

print(mixed_list[-1])


#slicing list
print(names[1:3])

#modify list 
names.append("luana")
names[0] = "josinha"

names.insert(2, "jacoo")

names.remove("luana")

del names[0]

print(names.pop())

for item in names:
    print(item)