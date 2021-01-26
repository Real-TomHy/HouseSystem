from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from house.newShowInfo import ShowInfo
from house.del_cusHousePeople import DelInfo
from house.addPeople import *


class RentPeople(object):
    def __init__(self,oldroot):
        """主界面基本设置"""
        # 关闭父窗口
        self.oldroot = oldroot
        self.oldroot.withdraw()
        # 创建窗口
        root = Tk()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 700
        high = 600
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        root.title('求租信息记录')

        # 设置各个文本框的标签，并固定位置
        Label(root, text="客户编号：").place(relx=0, rely=0.05, relwidth=0.1)
        Label(root, text="客户姓名：").place(relx=0.21, rely=0.05, relwidth=0.1)
        Label(root, text="建筑面积：").place(relx=0.41, rely=0.05, relwidth=0.1)
        Label(root, text="联系方式：").place(relx=0.61, rely=0.05, relwidth=0.1)

        Label(root, text="户型：").place(relx=0, rely=0.15, relwidth=0.1)
        Label(root, text="房屋种类：").place(relx=0.25, rely=0.15, relwidth=0.1)
        Label(root, text="装修情况：").place(relx=0.55, rely=0.15, relwidth=0.1)




        # 设置各个文本框并固定位置
        self.id=Entry(root)
        self.id.place(relx=0.1, rely=0.05, relwidth=0.1, height=25)
        self.name=Entry(root)
        self.name.place(relx=0.3, rely=0.05, relwidth=0.1, height=25)
        self.area=Entry(root)
        self.area.place(relx=0.5, rely=0.05, relwidth=0.1, height=25)
        self.cell=Entry(root)
        self.cell.place(relx=0.7, rely=0.05, relwidth=0.15, height=25)


        # 创建表格并设置相关属性
        sb = Scrollbar(root)
        sb.place(relx=0.971, rely=0.028, relwidth=0.014,
                 relheight=0.958)  # relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958
        scrollBarx = Scrollbar(root, orient=HORIZONTAL)  # 水平滚动条
        scrollBarx.place(relx=0.05, rely=0.971, relwidth=0.958, relheight=0.024)

        self.tree_view = ttk.Treeview(root, show='headings', column=('cusPeo_id', 'cusPeo_name', 'cusPeo_cell', 'cusPeo_type','housPeo_type','housPeo_area','renPeo_situation'), yscrollcommand=sb.set, xscrollcommand=scrollBarx.set)
        # 即滚动条与页面内容的位置同步
        sb.config(command=self.tree_view.yview)
        scrollBarx.config(command=self.tree_view.xview)
        # 设置每列的属性
        self.tree_view.configure(yscrollcommand=sb.set)
        self.tree_view.column('cusPeo_id', width=150, anchor="center")
        self.tree_view.column('cusPeo_name', width=150, anchor="center")
        self.tree_view.column('cusPeo_cell', width=150, anchor="center")
        self.tree_view.column('cusPeo_type', width=150, anchor="center")
        self.tree_view.column('housPeo_type', width=150, anchor="center")
        self.tree_view.column('housPeo_area', width=150, anchor="center")
        self.tree_view.column('renPeo_situation', width=150, anchor="center")
        # 设置每行的属性
        self.tree_view.heading('cusPeo_id', text='客户编号')
        self.tree_view.heading('cusPeo_name', text='客户姓名')
        self.tree_view.heading('cusPeo_cell', text='联系方式')
        self.tree_view.heading('cusPeo_type', text='房屋种类')
        self.tree_view.heading('housPeo_type', text='户型')
        self.tree_view.heading('renPeo_situation', text='装修情况')
        self.tree_view.heading('housPeo_area', text='房屋面积')
        # 设置表格位置
        self.tree_view.place(relx=0.02, rely=0.3, relwidth=0.96)

        # 下拉列表
        comvalueHous_type = StringVar()  # 窗体自带的文本，新建一个值
        self.comboxlistHous_type = ttk.Combobox(root, textvariable=comvalueHous_type)
        self.comboxlistHous_type["values"] = ("三室一厅", "两室一厅", "一室一厅", "单间", "独门独院", "其他")
        self.comboxlistHous_type.place(relx=0.1, rely=0.15, relwidth=0.1)  # 初始化
        self.comboxlistHous_type.current(0)  # 默认第一个

        comvaluecus_type = StringVar()  # 窗体自带的文本，新建一个值
        self.comboxlistcus_type = ttk.Combobox(root, textvariable=comvaluecus_type)
        self.comboxlistcus_type["values"] = ("楼房", "平房", "其他")
        self.comboxlistcus_type.place(relx=0.35, rely=0.15, relwidth=0.1)  # 初始化
        self.comboxlistcus_type.current(0)

        comvalueren_situatione = StringVar()  # 窗体自带的文本，新建一个值
        self.comboxlistren_situation = ttk.Combobox(root, textvariable=comvalueren_situatione)
        self.comboxlistren_situation["values"] = ("高档装修", "中档装修", "简单装修", "无装修")
        self.comboxlistren_situation.place(relx=0.65, rely=0.15, relwidth=0.1)  # 初始化
        self.comboxlistren_situation.current(0)

        # 设置按钮，并固定位置
        rent = ShowInfo(self.tree_view)
        add = AddInfo()
        Button(root, text="显示信息", command=lambda: rent.show_cusHousePeople()).place(relx=0.5, rely=0.2, width=80)
        Button(root, text="记录信息", command=lambda: add.insertRentPeopleInfo(self.id.get(),self.name.get(),self.cell.get(),self.comboxlistcus_type.get(),self.comboxlistHous_type.get(),self.area.get(),self.comboxlistren_situation.get())).place(relx=0.05, rely=0.2, width=80)
        Button(root, text="删除信息",command=lambda: DelInfo(self.item_text)).place(relx=0.35, rely=0.2, width=80)
        Button(root, text="返回", command=lambda: self.goback(root)).place(relx=0.80, rely=0.2, width=80)







        # 绑定单击离开事件
        self.tree_view.bind('<ButtonRelease-1>', self.tree_view_click)

        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))

        # 事件循环
        root.mainloop()

    def tree_view_click(self,event):
        """点击表格中的一项数据后将其显示在相应文本框上"""
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "values")
            # print(item_text)
            self.item_text = item_text
            #先清空 后添加，否则添加的数据并不会覆盖原数据
            self.id.delete(0,"end")
            self.id.insert(0,item_text[0])
            self.name.delete(0,"end")
            self.name.insert(0,item_text[1])
            self.area.delete(0,"end")
            self.area.insert(0,item_text[5])
            self.cell.delete(0,"end")
            self.cell.insert(0,item_text[2])
            # print(len(self.comboxlistcus_type["values"]))
            for i in range (len(self.comboxlistcus_type["values"])):
                if item_text[3]==self.comboxlistcus_type["values"][i]:
                    self.comboxlistcus_type.current(i)
                    break
            for i in range (len(self.comboxlistHous_type["values"])):
                if item_text[4]==self.comboxlistHous_type["values"][i]:
                    self.comboxlistHous_type.current(i)
                    break
            for i in range (len(self.comboxlistren_situation["values"])):
                if item_text[6]==self.comboxlistren_situation["values"][i]:
                    self.comboxlistren_situation.current(i)
                    break
            # comboxlistcus_type.current()
            # self.stu_id.set(item_text[0])
            # self.stu_name.set(item_text[1])
            # self.stu_python.set(item_text[2])
            # self.stu_c.set(item_text[3])

    def callback(self, root):
        """退出时的询问"""
        if askokcancel("询问", "是否关闭该窗口?"):
            root.destroy()

     #返回事件
    def goback(self,root):
        root.destroy()
        self.oldroot.update()
        self.oldroot.deiconify()

