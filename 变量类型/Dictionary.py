dict1 = {}
dict1['one'] = '1'
dict1[2] = '2'
tinydict = {'name':'bloodymandoo','code':1,'site':'www.bloodymandoo.com'}

print(dict1['one'])
print(dict1[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dict1 = dict([('Python',1),('Google',2),('Taobao',3)])
print(dict1)

dict2 = {x:x**2 for x in (2,4,6)}
print(dict2)

dict3 = dict(Python=1,Google=2,Taobao=3)
print(dict3)
