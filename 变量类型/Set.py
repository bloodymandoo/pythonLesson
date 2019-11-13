student = {'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student)

if 'Rose' in student:
  print('Rose 在集合中')
else:
  print('Rose 不在集合中')


a = set('abracadabra')
b = set('alacazam')

print(a - b) #a和b的差集
print(a | b) #a和b的并集
print(a & b) #a和b的交集
print(a ^ b) #a和b中不同时存在的元素