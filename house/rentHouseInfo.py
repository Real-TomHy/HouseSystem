from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from newShowInfo import ShowInfo
from addRentHouse import AddInfo
from del_RentHouseinfo import DelInfo
from searchRentInfo import SearchHouseInfo






class RentHouseInfo(object):
    def __init__(self,oldroot):
        """主界面基本设置"""
        # 关闭父窗口
        self.oldroot=oldroot
        self.oldroot.withdraw()
        # 创建窗口
        root = Tk()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 700
        high = 600
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))
        root.title('出租房屋信息')

        # 设置窗口的标题标签
        Label(root, text='房屋信息显示', bg='white', fg='blue', font=('宋体', 10)).pack(side=TOP, fill='x')

        # 创建表格并设置相关属性

        sb = Scrollbar(root)
        sb.place(relx=0.971, rely=0.028, relwidth=0.014, relheight=0.958)#relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958
        scrollBarx = Scrollbar(root, orient=HORIZONTAL)#水平滚动条
        scrollBarx.place(relx=0.05, rely=0.971, relwidth=0.958, relheight=0.024)

        self.tree_view = ttk.Treeview(root,show='headings', column=(
        'cus_id', 'cus_name', 'cus_cell', 'cus_type', 'cus_price', 'hous_type', 'hous_area', 'ren_situation',
        'hous_address', 'hous_situation'), yscrollcommand=sb.set, xscrollcommand=scrollBarx.set)
        # 即滚动条与页面内容的位置同步
        sb.config(command=self.tree_view.yview)
        scrollBarx.config(command=self.tree_view.xview)
        # 设置每列的属性
        self.tree_view.configure(yscrollcommand=sb.set)
        self.tree_view.column('cus_id', width=100, anchor="center")
        self.tree_view.column('cus_name', width=100, anchor="center")
        self.tree_view.column('cus_cell', width=100, anchor="center")
        self.tree_view.column('cus_type', width=100, anchor="center")
        self.tree_view.column('cus_price', width=100, anchor="center")
        self.tree_view.column('hous_type', width=100, anchor="center")
        self.tree_view.column('hous_area', width=100, anchor="center")
        self.tree_view.column('ren_situation', width=100, anchor="center")
        self.tree_view.column('hous_address', width=100, anchor="center")
        self.tree_view.column('hous_situation', width=100, anchor="center")
        # 设置每行的属性
        self.tree_view.heading('cus_id', text='客户编号')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'cus_id', False))
        self.tree_view.heading('cus_name', text='客户姓名')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'cus_name', False))
        self.tree_view.heading('cus_cell', text='联系方式')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'cus_cell', False))
        self.tree_view.heading('cus_type', text='房屋种类')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'cus_type', False))
        self.tree_view.heading('cus_price', text='每月价格')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'cus_price', False))
        self.tree_view.heading('hous_type', text='户型')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'hous_type', False))
        self.tree_view.heading('hous_area', text='房屋面积')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'hous_area', False))
        self.tree_view.heading('hous_address', text='房屋地址')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'hous_address', False))
        self.tree_view.heading('ren_situation', text='装修情况')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'ren_situation', False))
        self.tree_view.heading('hous_situation', text='房屋情况')#, command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'hous_situation', False))

        # 设置表格位置
        self.tree_view.place(relx=0.02, rely=0.3, relwidth=0.96)

        # 设置按钮，并固定位置
        rent=ShowInfo(self.tree_view)
        add=AddInfo()
        search=SearchHouseInfo(self.tree_view)
        Button(root, text="显示全部信息", command=lambda: rent.show_rentHouse()).place(relx=0.05, rely=0.2, width=80)
        Button(root, text="插入信息",command=lambda: add.createRoot()).place(relx=0.20, rely=0.2, width=80)
        Button(root, text="删除信息",command=lambda: DelInfo(self.item_text)).place(relx=0.35, rely=0.2, width=80)
        Button(root, text="查询信息",command=lambda: search.createRoot()).place(relx=0.50, rely=0.2, width=80)
        # Button(root, text="出租").place(relx=0.65, rely=0.2, width=80)
        Button(root, text="返回", command=lambda: self.goback(root)).place(relx=0.65, rely=0.2, width=80)


        # 绑定单击离开事件
        self.tree_view.bind('<ButtonRelease-1>', self.tree_view_click)
        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))

        # 事件循环
        root.mainloop()
        #返回事件
    def goback(self,root):
        root.destroy()
        self.oldroot.update()
        self.oldroot.deiconify()

    def tree_view_click(self, event):
        """点击表格中的一项数据后将其显示在相应文本框上"""
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "values")
            self.item_text=item_text
            # self.cus_id.set(item_text[0])
            # self.cus_name.set(item_text[1])
            # self.cus_cell.set(item_text[2])
            # self.cus_type.set(item_text[3])
            # self.cus_price.set(item_text[4])
            # self.hous_area.set(item_text[5])
            # self.hous_address.set(item_text[6])
            # self.ren_situation.set(item_text[7])
            # self.hous_situation.set(item_text[8])



    def callback(self, root):
        """退出时的询问"""
        if askokcancel("询问", "是否关闭该窗口?"):
            root.destroy()



