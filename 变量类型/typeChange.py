#int(x[,base]) int(x,base=10)
print(int())
print(int(3))
print(int(3.6))
print(int('12',16))
print(int('0xa',16))
print(int('10',8))

#float(x)
print(float(1))
print(float(112))
print(float(-123.6))
print(float('123'))

#complex(real[,imag])
print(complex(1,2))
print(complex(1))
print(complex("1"))
print(complex("1+2j"))

#str(x)
s = "python"
print(str(s))
dict1 = {'python':1}
print(str(dict1))

#repr(x) repr(object)
s = 'python'
print(repr(s))
dict1 = {"python":1}
print(repr(dict1))

#eval(str) #用来计算在字符串中的有效Python表达式，并返回一个对象
x = 7
print(eval('3*x'))
print(eval('pow(2,2)'))
print(eval('2+2'))
n = 81
print(eval('n + 4'))

#tuple(s)
s = 'www'
print(tuple(s))
list1 = ['python','taobao','baidu']
print(tuple(dict1))
dict1 = {'python':1}
print(tuple(dict1))
se = set('abcd')
print(tuple(se))

#list(s)
tu = (123,'googole','python','taobao')
print(list(tu))
s = 'abcd'
print(list(s))

#set(s)
print(set('abcd'))

#dict(d)
print(dict())
print(dict(a='a',b='b',c='c'))
print(dict(zip['one','two','three'],[1,2,3]))
print(dict([('one',1),('two',2),('three',3)]))

#frozense(s)

#chr(x)

#ord(x)

#hex(x)

#oct(x)
