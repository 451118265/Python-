import random
secret = random.randint(1,10)
print("随机函数")
temp = input("请猜测")
guess = int(temp)
while guess != secret:
    temp = input("错了，请重新输入")
    guess = int(temp)
    if guess = int(temp):
        print("正确")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
print("结束")
