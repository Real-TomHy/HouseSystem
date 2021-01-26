from database import Database
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
class AddInfo(object):
    def __init__(self):
        pass
        """主界面基本设置"""
    def insertRentPeopleInfo(self, cusPeo_id, cusPeo_name, cusPeo_cell, cusPeo_type, housPeo_type, housPeo_area, renPeo_situation):
        """添加信息"""
        db = Database()
        # print(cus_id, cus_name, cus_price, cus_type, hous_area, hous_type, cus_cell,
        #       ren_situation, hous_address, hous_situation)
        try:
            cusPeo_cell = int(cusPeo_cell)
            housPeo_area = int(housPeo_area)


            # print(cus_id.strip())
            if not(cusPeo_id.strip() and cusPeo_name.strip()  and cusPeo_type.strip()  and housPeo_type.strip()):
                raise ValueError
            if db.prepare(f"select * from RentingPeopleInfo where cusPeo_id='{cusPeo_id}'") == 0:
                sql = f"insert into RentingPeopleInfo values('{cusPeo_id}', '{cusPeo_name}', '{cusPeo_cell}', '{cusPeo_type}','{housPeo_type}','{housPeo_area}','{renPeo_situation}')"
                db.prepare(sql)
                db.update()
                showinfo("提示", "记录成功")
            else:
                showerror("记录失败", "记录失败")

        except ValueError:
            showerror("记录失败", "信息未填写完整或者输入有问题")

    def insertPurPeopleInfo(self, cusPeo_id, cusPeo_name, cusPeo_cell, cusPeo_type, housPeo_type, housPeo_area, renPeo_situation):
        """添加信息"""
        db = Database()
        # print(cus_id, cus_name, cus_price, cus_type, hous_area, hous_type, cus_cell,
        #       ren_situation, hous_address, hous_situation)
        try:
            cusPeo_cell = int(cusPeo_cell)
            housPeo_area = int(housPeo_area)


            # print(cus_id.strip())
            if not(cusPeo_id.strip() and cusPeo_name.strip()  and cusPeo_type.strip()  and housPeo_type.strip()):
                raise ValueError
            if db.prepare(f"select * from PurchasePeopleInfo where cusPeo_id='{cusPeo_id}'") == 0:
                sql = f"insert into PurchasePeopleInfo values('{cusPeo_id}', '{cusPeo_name}', '{cusPeo_cell}', '{cusPeo_type}','{housPeo_type}','{housPeo_area}','{renPeo_situation}')"
                db.prepare(sql)
                db.update()
                showinfo("提示", "记录成功")
            else:
                showerror("记录失败", "记录失败")

        except ValueError:
            showerror("记录失败", "信息未填写完整或者输入有问题")