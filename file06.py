"""
about function
"""
"""


def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *=n
    return result

m = int(input('m ='))
n = int(input('n ='))
print(fac(m) // fac(n) // fac(m - n))


"""

from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):

        v =  randint(1, 6)
        print(v)
        total += v
        
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print('=', roll_dice())
# 摇三颗色子
print('=', roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

    