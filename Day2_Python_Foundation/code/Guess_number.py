import random

def guess_number():
    num = random.randrange(1, 101, 1)
    print("请开始猜数游戏，数字范围为1-100")
    count = 10
    while count:
        guess = int(input("请输入你猜的数字："))
        if guess == num:
            print("恭喜你，猜对了！")
            break
        else:
            if guess > num:
                print("猜的数字大了，请再试一次！")
            else:
                print("猜的数字小了，请再试一次！")
        count -= 1
        if count == 0:
            print("很遗憾，你用完了猜的机会，正确答案是", num)
    return

if __name__ == '__main__':
    guess_number()