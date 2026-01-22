import math

def Calculator():
    print("欢迎使用计算器！")
    print("我们提供了以下功能：")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("5.平方")
    print("6.开方")
    print("7.退出")
    while True:
        choice = int(input("请输入你的选择："))
        if choice == 1:
            add()
        elif choice == 2:
            sub()
        elif choice == 3:
            mul()
        elif choice == 4:
            div()
        elif choice == 5:
            square()
        elif choice == 6:
            sqrt()
        elif choice == 7:
            exit()
            break
    return

def add():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    print("结果为：",num1 + num2)

def sub():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    print("结果为：",num1 - num2)

def mul():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    print("结果为：",num1 * num2)

def div():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    print("结果为：",num1 / num2)

def square():
    num1 = int(input("请输入底数："))
    num2 = int(input("请输入指数："))
    print("结果为：",math.pow(num1,num2))

def sqrt():
    num1 = int(input("请输入数字："))
    print("结果为：",math.sqrt(num1))

def exit():
    print("欢迎下次使用！")

if __name__ == "__main__":
    Calculator()