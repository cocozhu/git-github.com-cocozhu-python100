#代码演示了如何向列表中添加元素以及如何从列表中移除元素。

list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []

# 元组
t = (1,2,3,4)
print('t=',t)
print(t[2])
y = list(t)
print(y)
y[2] = 99
print(y,y[2])

# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
print(type(fruits_tuple))

import os
import time

def main():
    content = input("请输入滚动文字内容：")
    try:
        while True:
            # 清理屏幕上的输出
            if os.name == 'nt':
                os.system('cls')  # Windows
            else:
                os.system('clear')  # macOS/Linux

            print(content)
            # 休眠200毫秒
            time.sleep(0.2)
            # 滚动文字
            content = content[1:] + content[0]  # content[1:]提取从第二个字符到最后一个字符的子串。content[0] 提取第一个字符。
    except KeyboardInterrupt:
        print("\n程序已退出")

if __name__ == '__main__':
    main()
