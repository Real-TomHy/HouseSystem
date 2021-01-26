from database import Database
from tkinter.messagebox import *


class DelInfo(object):
    def __init__(self, item_text):
        """模糊删除"""
        db = Database()
        cusPeo_id=item_text[0]
        cusPeo_name=item_text[1]
        cusPeo_cell=int(item_text[2])
        cusPeo_type=item_text[3]
        housPeo_type=item_text[4]
        housPeo_area=int(item_text[5])
        renPeo_situation=item_text[6]

        # print(cus_id, cus_name, type(cus_price), cus_type, hous_area, hous_type, cus_cell,
        #       ren_situation, hous_address, hous_situation)
        try:
            sql = f'''select * from PurchasePeopleInfo where (cusPeo_id like '%{cusPeo_id}%')'''
            if (cusPeo_id) and db.prepare(sql):
                db.update()
                cus_tuple = db.cursor.fetchall()
                for i in range(len(cus_tuple)):
                    if askokcancel("提示", f"是否删除该求购信息(编号:{cus_tuple[i][0]} 姓名:{cus_tuple[i][1]} 联系方式:{cus_tuple[i][2]} 房屋种类:{cus_tuple[i][3]})"):
                        db.prepare(f"delete from PurchasePeopleInfo where (cusPeo_id like '%{cusPeo_id}%') limit 1")
                        db.update()
                        showinfo("提示", "删除成功")
            else:
                showerror("删除失败", "未查询到该求购信息")
        except ValueError:
            showerror("删除失败", "请重新删除")
