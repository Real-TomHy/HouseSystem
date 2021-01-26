from database import Database


class ShowInfo(object):
    def __init__(self, tree_view):
        self.tree_view=tree_view
    def show_rentHouse(self):
        """将所有信息显示在表格上"""
        db = Database()
        x = self.tree_view.get_children()
        for item in x:
            self.tree_view.delete(item)
        db.cursor.execute("select * from rentinghouseinfo")
        student_tuple = db.cursor.fetchall()
        for item in student_tuple:
            self.tree_view.insert("", 'end', values=item)

    def show_sellHouse(self):
        """将所有信息显示在表格上"""
        db = Database()
        x = self.tree_view.get_children()
        for item in x:
            self.tree_view.delete(item)
        db.cursor.execute("select * from SellHouseInfo")
        student_tuple = db.cursor.fetchall()
        for item in student_tuple:
            self.tree_view.insert("", 'end', values=item)

    def show_cusHousePeople(self):
        """将所有信息显示在表格上"""
        db = Database()
        x = self.tree_view.get_children()
        for item in x:
            self.tree_view.delete(item)
        db.cursor.execute("select * from RentingPeopleInfo")
        student_tuple = db.cursor.fetchall()
        for item in student_tuple:
            self.tree_view.insert("", 'end', values=item)

    def show_PurHousePeople(self):
        """将所有信息显示在表格上"""
        db = Database()
        x = self.tree_view.get_children()
        for item in x:
            self.tree_view.delete(item)
        db.cursor.execute("select * from PurchasePeopleInfo")
        student_tuple = db.cursor.fetchall()
        for item in student_tuple:
            self.tree_view.insert("", 'end', values=item)