# 元组， 不可以改变的类型
"""
如果元组中只有一个元素，需要加上一个逗号

推荐大家使用列表的生成式语法来创建列表

"""

# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('骆昊', 43, True, '四川成都')


a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>

# 打包操作
a = 1, 100, 200
print(type(a))
print(a)

# 解包操作
i,j,k = a
print(i,j,k)


# Python 中的元组和列表类型是可以相互转换的
infos = ('骆昊', 43, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['骆昊', 43, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')

