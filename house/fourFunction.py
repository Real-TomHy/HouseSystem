from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from house.rentHouseInfo import *
from house.sellHouseInfo import *
from house.RentPeople import *
from house.PurchasePeople import *
class FourFuncyion(object):
    def __init__(self):
        """主界面基本设置"""
        # 创建窗口
        root = Tk()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 700
        high = 300
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))
        root.title('房屋中介管理系统')
        #  设置按钮，并固定位置
        Button(root, text="出租房屋信息管理", command=lambda:RentHouseInfo(root)).place(relx=0.05, rely=0.2, relwidth=0.15)
        Button(root, text="出售房屋信息管理", command=lambda:SellHouseInfo(root)).place(relx=0.25, rely=0.2, relwidth=0.15)
        Button(root, text="求租信息管理", command=lambda:RentPeople(root)).place(relx=0.5, rely=0.2, relwidth=0.15)
        Button(root, text="求购信息管理", command=lambda:PurchasePeople(root)).place(relx=0.7, rely=0.2, relwidth=0.15)
        Button(root, text="退出", command=lambda: self.callback(root)).place(relx=0.7, rely=0.8, relwidth=0.15)
        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))
        # 事件循环
        root.mainloop()


    def callback(self, root):
        """退出时的询问"""
        if askokcancel("询问", "是否关闭该窗口?"):
            root.destroy()
