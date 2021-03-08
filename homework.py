import random


# 作业
# 使用for循环实现1~100的之和
def sum100(num):
    """
    :param num: 若要计算100以内的，则传101
    :return: 返回数字之和
    """
    s = 0
    for i in range(num):
        s = s + i
    return s


# 然后在该循环中增加分支结构实现1~100的偶数和
def sum2(num):
    """
    :param num: 若要计算100以内的，则传101
    :return:
    """
    s = 0
    for i in range(num):
        if i % 2 == 0:
            s = s + i
    return s


# 直接使用for循环，实现1~100的偶数和
def sum3(num):
    """
    :param num: 若要计算100以内的，则传101
    :return:
    """
    s = 0
    for i in range(0, num, 2):
        s = s + i
    return s


#  猜数字游戏 计算出一个1~100之间的随机数由人来猜，计算机跟进人猜的数字进行对比，给出提示大一点，小一点，如果猜对了则结束游戏
def game():
    print("游戏开始！")
    basic_num = random.randint(1, 100)
    while True:
        num = input("请输入数字：")
        # 判断输入的是不是数字
        if num.isdigit():
            num = float(num)
            if num == basic_num:
                print("猜对了，游戏结束！")
                break
            elif num < basic_num:
                print("猜错了，请大一点！")
            elif num > basic_num:
                print("猜错了，请小一点！")
        else:
            print("输入格式不对，请确保输入的是正整数！")


game()



