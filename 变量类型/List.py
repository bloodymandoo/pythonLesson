list = ['abcd',789,2.23,'python',70.2]
tinylist = [123,'python']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)

list[1] = 0
print(list)