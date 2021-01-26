from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
def callback(cus_id):
    print(cus_id.get())
root = Tk()
# 设置窗口大小和并将位置设置到屏幕中央
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
width = 400
high = 300
root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))
root.title('出租房屋信息插入')
cus_id = StringVar()
Entry(root, textvariable=cus_id).place(relx=0.24, rely=0.09, relwidth=0.25, height=15)

Button(root, text="取消",command=lambda:callback(cus_id)).place(relx=0.7, rely=0.78, width=80)
root.mainloop()

