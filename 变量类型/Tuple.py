tuple = ('abcd',789,2.23,'python',70.2)
tinytuple = (123,'python')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)

tup1 = ()     #空元组
tup2 = (20,)  #一个元素，需要在元素后添加逗号
"""
1、与字符串一样，元组的元素不能修改
2、元组也可以被索引和切片，方法一样
3、注意构造包含0或1个元素的元组的特殊语法
4、元组也可以使用+操作符进行拼接
"""