import random
global getNum
getNum = random.randint(1,10)   #随机生成一个一到十的整数
print("----------文字游戏-Verson1.1----------")
a = input("猜一个数字:")
b = int(a)  #类型转化
# 判断是否回答正确
if b != getNum:
    timesLeft = 3   #剩余的次数
    for times in range (1,3):   #回答错误，进入3次循环
        timesLeft = timesLeft - 1   #每次循环次数减一
        if (b == getNum):
            break               #如果答对，结束循环；答错提示
        elif (b > getNum):
            print('大了ヾ(•ω•`)o')
        elif (b < getNum):
            print('小了(*￣3￣)╭')
        a = input(f"你还有{timesLeft}次机会:")
        b = int(a)
    if (b == getNum):           #循环结束后判断是否答对
        print('恭喜答对！ヾ(≧▽≦*)o')
    else:
        print('算了吧，你猜不到的！(～﹃～)~zZ')
else:
    print('恭喜答对！ヾ(≧▽≦*)o')