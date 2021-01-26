from database import Database
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
class SearchHouseInfo(object):
    def __init__(self,tree_view):
        self.tree_view=tree_view
        """主界面基本设置"""
    def createRoot(self):
        root = Tk()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 400
        high = 300
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))
        root.title('出租房屋信息查询')

        # 设置各个文本框的标签，并固定位置

        Label(root, text="户型").place(relx=0.05, rely=0.08, relwidth=0.2)
        Label(root, text="房屋种类").place(relx=0.5, rely=0.08, relwidth=0.2)
        Label(root, text="装修情况").place(relx=0.05, rely=0.38, relwidth=0.2)
        Label(root, text="房屋情况").place(relx=0.5, rely=0.38, relwidth=0.2)
        # Label(root, text="房屋地址").place(relx=0.04, rely=0.58, relwidth=0.2)
        #下拉列表
        comvalueHous_type = StringVar()  # 窗体自带的文本，新建一个值
        comboxlistHous_type = ttk.Combobox(root, textvariable=comvalueHous_type)
        comboxlistHous_type["values"] = ("三室一厅", "两室一厅", "一室一厅","单间","独门独院","其他")
        comboxlistHous_type.place(relx=0.7, rely=0.08, relwidth=0.2)  # 初始化
        comboxlistHous_type.current(0)#默认第一个


        comvaluecus_type = StringVar()  # 窗体自带的文本，新建一个值
        comboxlistcus_type = ttk.Combobox(root, textvariable=comvaluecus_type)
        comboxlistcus_type["values"] = ("楼房", "平房", "其他")
        comboxlistcus_type.place(relx=0.25, rely=0.08, relwidth=0.2)  # 初始化
        comboxlistcus_type.current(0)


        comvalueren_situatione = StringVar()  # 窗体自带的文本，新建一个值
        comboxlistren_situation = ttk.Combobox(root, textvariable=comvalueren_situatione)
        comboxlistren_situation["values"] = ("高档装修", "中档装修", "简单装修","无装修")
        comboxlistren_situation.place(relx=0.25, rely=0.38,relwidth=0.2)  # 初始化
        comboxlistren_situation.current(0)


        comvaluehous_situation = StringVar()  # 窗体自带的文本，新建一个值
        comboxlisthous_situation = ttk.Combobox(root, textvariable=comvaluehous_situation)
        comboxlisthous_situation["values"] = ("已出租", "未出租")
        comboxlisthous_situation.place(relx=0.7, rely=0.38,relwidth=0.2)  # 初始化
        comboxlisthous_situation.current(0)

        # 此处如果默认，直接写死了
        # # 设置各个文本框内容所对应的变量
        # self.cus_type = comboxlistcus_type.get()
        # self.hous_type = comboxlistHous_type.get()
        # self.ren_situation = comboxlistren_situation.get()
        # self.hous_situation = comboxlisthous_situation.get()

        #插入与取消
        Button(root, text="查询",command=lambda: self.searchInfo(comboxlistcus_type.get(),comboxlistHous_type.get(),comboxlistren_situation.get(),comboxlisthous_situation.get())).place(relx=0.3, rely=0.78, width=80)
        Button(root, text="取消",command=lambda: self.callback(root)).place(relx=0.7, rely=0.78, width=80)


        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))
        # 事件循环
        root.mainloop()

    def callback(self, root):
        """退出时的询问"""
        if askokcancel("询问", "是否关闭该窗口?"):
            root.destroy()

    def searchInfo(self, cus_type, hous_type,  ren_situation,
                   hous_situation):
        """查询信息"""
        print(cus_type,hous_type,ren_situation,hous_situation)
        #print(self.cus_type, self.hous_type, self.ren_situation, self.hous_situation)
        db = Database()
        x = self.tree_view.get_children()
        for item in x:
            self.tree_view.delete(item)
        # print(cus_id, cus_name, cus_price, cus_type, hous_area, hous_type, cus_cell,
        #       ren_situation, hous_address, hous_situation)
        try:
            # 该sql语句筛选出你模糊查询的各种数据（可以组合）
            sql = f'''select * from RentingHouseInfo where cus_type= '{cus_type}'
                               and hous_type ='{hous_type}' and ren_situation = '{ren_situation}' and hous_situation = '{hous_situation}'
                               '''
            # 只有文本框内有有效数据时才执行该语句
            if db.prepare(sql):
                db.update()
                showinfo("提示", "已完成查询")
                student_tuple = db.cursor.fetchall()
                for item in student_tuple:
                    self.tree_view.insert('', 'end', values=item)
            else:
                showerror("查询失败", "未查询到该类型房屋信息")
        except ValueError:
            showerror("查询失败", "重新查询")
        db.close()