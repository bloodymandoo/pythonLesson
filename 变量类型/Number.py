a,b,c,d = 20,5.5,True,4+3j

print(type(a),type(b),type(c),type(d))

print(isinstance(a,int))

'''
isinstance和type的区别在于：
type()不会认为子类是一种父类型
isinstance()会认为子类是一种父类型
'''

class A:
  pass

class B(A):
  pass

print(isinstance(A(),A))
print(isinstance(B(),A))
print(type(A())==A)
print(type(B())==A)

#删除对象
del a
del b,c

#运算
print(5+4)#加
print(4.3-2)#减
print(3*7)#乘
print(2/4)#除
print(2//4)#除取整
print(17%3)#取余
print(2**5)#乘方
