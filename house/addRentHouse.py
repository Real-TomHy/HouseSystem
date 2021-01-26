from database import Database
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
class AddInfo(object):
    def __init__(self):
        pass
        """主界面基本设置"""
    #test输入模块，输入绑定方法已经失效
    def testcallback(self,cus_id):
        print(cus_id)
        print(type(cus_id))
        newcys_id=int(cus_id)
        print(newcys_id)
        print(type(newcys_id))


    def createRoot(self):
        root = Tk()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 400
        high = 300
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))
        root.title('出租房屋信息插入')
        # 设置窗口的标题标签
        # Label(root, text='请输入插入房屋信息', bg='white', fg='blue', font=('宋体', 15)).pack(relx=0.05, rely=0.05, relwidth=0.1)

        # 设置各个文本框的标签，并固定位置
        Label(root, text="客户编号").place(relx=0.04, rely=0.08, relwidth=0.2)
        Label(root, text="客户姓名").place(relx=0.04, rely=0.18, relwidth=0.2)
        Label(root, text="每月价格").place(relx=0.04, rely=0.28, relwidth=0.2)
        Label(root, text="建筑面积").place(relx=0.04, rely=0.38, relwidth=0.2)
        Label(root, text="联系电话").place(relx=0.04, rely=0.48, relwidth=0.2)
        Label(root, text="户型").place(relx=0.5, rely=0.08, relwidth=0.2)
        Label(root, text="房屋种类").place(relx=0.5, rely=0.18, relwidth=0.2)
        Label(root, text="装修情况").place(relx=0.5, rely=0.28, relwidth=0.2)
        Label(root, text="房屋情况").place(relx=0.5, rely=0.38, relwidth=0.2)
        Label(root, text="房屋地址").place(relx=0.04, rely=0.58, relwidth=0.2)
        #下拉列表
        comvalueHous_type = StringVar()  # 窗体自带的文本，新建一个值
        comboxlistHous_type = ttk.Combobox(root, textvariable=comvalueHous_type)
        comboxlistHous_type["values"] = ("三室一厅", "两室一厅", "一室一厅","单间","独门独院","其他")
        comboxlistHous_type.place(relx=0.7, rely=0.08, relwidth=0.2)  # 初始化
        comboxlistHous_type.current(0)#默认第一个

        comvaluecus_type = StringVar()  # 窗体自带的文本，新建一个值
        comboxlistcus_type = ttk.Combobox(root, textvariable=comvaluecus_type)
        comboxlistcus_type["values"] = ("楼房", "平房", "其他")
        comboxlistcus_type.place(relx=0.7, rely=0.18, relwidth=0.2)  # 初始化
        comboxlistcus_type.current(0)


        comvalueren_situatione = StringVar()  # 窗体自带的文本，新建一个值
        comboxlistren_situation = ttk.Combobox(root, textvariable=comvalueren_situatione)
        comboxlistren_situation["values"] = ("高档装修", "中档装修", "简单装修","无装修")
        comboxlistren_situation.place(relx=0.7, rely=0.28,relwidth=0.2)  # 初始化
        comboxlistren_situation.current(0)


        comvaluehous_situation = StringVar()  # 窗体自带的文本，新建一个值
        comboxlisthous_situation = ttk.Combobox(root, textvariable=comvaluehous_situation)
        comboxlisthous_situation["values"] = ("已出租", "未出租")
        comboxlisthous_situation.place(relx=0.7, rely=0.38,relwidth=0.2)  # 初始化
        comboxlisthous_situation.current(0)


        # 设置各个文本框并固定位置
        entrycus_id= Entry(root)
        entrycus_id.place(relx=0.24, rely=0.09, relwidth=0.25, height=15)
        entrycus_name=Entry(root)
        entrycus_name.place(relx=0.24, rely=0.19, relwidth=0.25, height=15)
        entrycus_price=Entry(root)
        entrycus_price.place(relx=0.24, rely=0.29, relwidth=0.25, height=15)
        entrycus_area=Entry(root)
        entrycus_area.place(relx=0.24, rely=0.39, relwidth=0.25, height=15)
        entryhous_cell=Entry(root)
        entryhous_cell.place(relx=0.24, rely=0.49, relwidth=0.25, height=15)
        entryhous_address=Entry(root)
        entryhous_address.place(relx=0.24, rely=0.58, relwidth=0.55, height=25)

        # # 设置各个文本框内容所对应的变量
        # self.cus_type = comboxlistcus_type.get()
        # self.hous_type = comboxlistHous_type.get()
        # self.ren_situation = comboxlistren_situation.get()
        # self.hous_situation = comboxlisthous_situation.get()
        # InfoList=[self.cus_id,self.cus_name,self.cus_cell,self.cus_type,self.cus_price,self.hous_type,self.hous_area,self.ren_situation,self.hous_address,self.hous_situation]
        #插入与取消
        Button(root, text="插入",command=lambda: self.insertInfo(entrycus_id.get(),entrycus_name.get(),entrycus_price.get(),comboxlistcus_type.get(),entrycus_area.get(),comboxlistHous_type.get(),entryhous_cell.get(),comboxlistren_situation.get(),entryhous_address.get(),comboxlisthous_situation.get())).place(relx=0.3, rely=0.78, width=80)
        Button(root, text="取消",command=lambda: self.callback(root)).place(relx=0.7, rely=0.78, width=80)
        #test输入
        # Button(root, text="取消", command=lambda: self.testcallback(entrycus_cell.get())).place(relx=0.9, rely=0.78, width=80)

        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))
        # 事件循环
        root.mainloop()

    def callback(self, root):
        """退出时的询问"""
        if askokcancel("询问", "是否关闭该窗口?"):
            root.destroy()

    def insertInfo(self, cus_id, cus_name, cus_price, cus_type, hous_area, hous_type, cus_cell, ren_situation,
                   hous_address, hous_situation):
        """添加信息"""
        db = Database()
        # print(cus_id, cus_name, cus_price, cus_type, hous_area, hous_type, cus_cell,
        #       ren_situation, hous_address, hous_situation)
        try:
            cus_cell = int(cus_cell)
            cus_price = int(cus_price)
            hous_area = int(hous_area)

            # print(cus_id.strip())
            if not(cus_id.strip() and cus_name.strip()  and cus_type.strip()  and hous_type.strip()  and ren_situation.strip()and hous_address.strip() and hous_situation.strip()):
                raise ValueError
            if db.prepare(f"select * from rentinghouseinfo where cus_id='{cus_id}'") == 0:
                sql = f"insert into rentinghouseinfo values('{cus_id}', '{cus_name}', '{cus_cell}', '{cus_type}','{cus_price}','{hous_type}','{hous_area}','{ren_situation}','{hous_address}','{hous_situation}')"
                db.prepare(sql)
                db.update()
                showinfo("提示", "添加成功")
            else:
                showerror("添加失败", "添加失败")

        except ValueError:
            showerror("添加失败", "信息未填写完整或者输入有问题")