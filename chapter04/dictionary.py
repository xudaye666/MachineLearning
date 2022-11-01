# 字典
mydict = {'a': 6.18, 'b': 'str', 'c': True}
print('A value: %.2f' % mydict['a'])
# 增加字典元素
mydict['a'] = 523
print('A value: %d' % mydict['a'])
print(f'keys: {mydict.keys()}')
print(f'values: {mydict.values()}')
for value in mydict.values():
    print(value)


mydict = {'a': 6.18, 'b': 'str', 'c': True}
# 删除特定元素
mydict.pop('a')
print(mydict)
# 删除字典的全部元素
mydict.clear()
print(mydict)



