from database import *

from house.fourFunction import *


class Login:
    def __init__(self):
        """创建登录界面"""
        self.db = Database()
        # 创建主窗口,用于容纳其它组件
        self.login_root = Tk()
        # 给主窗口设置标题内容
        self.login_root.title("登录系统")
        # 设置窗口大小和位置
        screenwidth = self.login_root.winfo_screenwidth()
        screenheight = self.login_root.winfo_screenheight()
        width = 500
        high = 300
        self.login_root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        # 创建画布
        self.canvas = Canvas(self.login_root, height=400, width=700)
        self.image_file = PhotoImage(file="123.gif")
        # 加载图片文件，并将图片置于画布上
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        # 放置画布（为上端）
        self.canvas.pack(side='top')

        # 创建账户标签
        Label(self.login_root, text='账户').place(x=90, y=70)
        # 创建密码标签
        Label(self.login_root, text='密码').place(x=90, y=95)

        account = StringVar()
        password = StringVar()
        # 创建一个账号输入框,并设置尺寸
        Entry(self.login_root, width=30, textvariable=account).place(x=140, y=70)
        # 创建一个密码输入框,并设置尺寸
        Entry(self.login_root, show='*', width=30, textvariable=password).place(x=140, y=95)

        # 创建一个登录系统的按钮
        Button(self.login_root, command=lambda: self.login(account, password), text="登录", width=10).place(x=155, y=120)
        # 创建一个注册系统的按钮
        Button(self.login_root, command=lambda: self.register(account, password), text="注册", width=10).place(x=250, y=120)

        mainloop()

    def login(self, account, password):
        """登录功能实现"""
        account = account.get()
        password = password.get()
        if account.strip() and password.strip():
            if self.db.prepare(f"select * from hous_user where user_account='{account}' and user_password='{password}'"):
                showinfo("提示", "登录成功")
                self.login_root.destroy()
                FourFuncyion()
            else:
                showerror("错误", "密码或账号错误请重新输入")
        else:
            showerror("错误", "账号信息没有输入完整")
    def register(self, account, password):
        """注册功能实现"""
        account = account.get()
        password = password.get()
        # 判断信息是否输入完整
        if account.strip() and password.strip():
            if self.db.prepare(f"select * from hous_user where user_account='{account}'") == 0:
                self.db.prepare(f"insert into hous_user values ('{account}', '{password}')")
                showinfo("提示", "注册成功")
            else:
                showerror("错误", "该账号已被注册")
        else:
            showerror("错误", "请输入完整的账号信息")







