
## 计算0到100的和
sum = 0
for x in range(0,101):
    sum += x

print(sum)


import random

answer = random.randint(1,10)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        break

    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足!')
        break
    
                

          
            