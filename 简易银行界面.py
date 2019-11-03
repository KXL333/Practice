# 导入OS模块
import os

#自定义初始用用户数据
users = [{"user_name":"铭铭",
          "password":'123456',
          "money":10000},
        {"user_name": "彬彬",
        "password": "111111",
        "money":20000},
        {"user_name":"柯柯",
          "password":"654321",
          "money":10000}
]

USER = None

def wait_continue():
    input("按enter键继续。。。")

def clear():
    os.system("cls")

def save():
    clear()
    money = int(input("请输入您要存入的数额："))
    USER['money'] += money
    print("恭喜您存入%d元，余额为%d"%(money,USER['money']))
    wait_continue()

def take():
    while True:
        clear()
        money = int(input("请输入您取出的金额："))
        if money > USER["money"]:
            print("对不起，您的余额不足！当前余额为%d"%USER["money"])
            wait_continue()
        else:
            USER["money"] -= money
            print("恭喜！取出%d元，当前余额为%d"%(money,USER["money"]))
            wait_continue()
            return
def look():
    clear()
    print("当前余额为%d"%(USER["money"]))
    wail_continue()
def login():
    while True:
        clear()
        user_name = input("请输入用户名：")
        password = int(input("请输入密码："))
        for user in users:
           if user_name == user['user_name'] and password ==user['password']:
               global USER
               USER = user
           return       
        print("用户名或密码错误！请重新输入：")
        wait_continue()
def welcome():
    while True:
        clear()
        print("欢迎来到银行ICII系统")
        print("输入1登录界面")
        print("输入0退出系统")
        option = input("请输入您的选择：")
        if option == '1':
            login()
            return
        elif option == '0':
            exit()
        else:
            print('您输入有误！')
            wait_continue()
def index():
    while True:
        clear()
        print('欢迎来到ICII银行系统')
        print('输入1存钱')
        print('输入2取钱')
        print('输入3查询')
        print('输入0退出')
        option = input('请输入您的选择：')
        if option == '1':
            save()
        elif option == '2':
            take()
        elif option =='3':
            look()
        elif option == '0':
            exit(0)
        else:
            print('您输入有误！')
        wait_continue()

def main():
    welcome()
    index()

main()











