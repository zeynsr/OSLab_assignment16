from cProfile import label
import sqlite3
import qdarkstyle
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        self.con = sqlite3.connect("ConDatabase.db")
        self.My_cursor = self.con.cursor()
        self.nc = 0
        self. LoadData()
        
        self.ui.btn_add.clicked.connect(self.AddContact)
        self.ui.btn_delete.clicked.connect(self.Delete)
        self.ui.btn_deleteAll.clicked.connect(self.DeleteAll)
        self.ui.btn_default.clicked.connect(self.Default)
        self.ui.btn_dark.clicked.connect(self.Darkmood)
        


    def LoadData(self):
        self.My_cursor.execute("SELECT * FROM person")
        res = self.My_cursor.fetchall()

        

        for it in res:
            label = QLabel()
            self.nc += 1
            label.setText(str(self.nc) + " ◑  " +it[1] + " " + it[2] + "\n" + it[3])
            self.ui.verticalLayout.addWidget(label)
            

        print("Done✅")



    def AddContact(self):
        name = self.ui.name.text()
        family = self.ui.family.text()
        phonenumber = self.ui.PhNum.text()
        self.ui.name.setText("")
        self.ui.family.setText("")
        self.ui.PhNum.setText("")
        self.nc += 1
        self.My_cursor.execute(f"INSERT INTO person(id,name,family,PhoneNumber) VALUES( '{self.nc}','{name}','{family}','{phonenumber}')")    
        self.con.commit()

        lable = QLabel()
        lable.setText(str(self.nc) + " ◑  " + name + " " + family + "\n" + phonenumber)
        self.ui.verticalLayout.addWidget(lable)
        
        print("Add successfuly ✔")


    def Delete(self):
        id=self.ui.id.text()
        self.ui.id.setText("")

        self.My_cursor.execute(f"DELETE FROM person WHERE id ==\' {id}\'")
        self.con.commit()

        print("Deleted.")

        exit() 


    def DeleteAll(self):
        self.My_cursor.execute('DELETE FROM person;')
        self.con.commit()
        lable = QLabel()
        lable.setText("all contacts are deleted.")

        print("Done✅")


    def Darkmood(self):
        my_app.setStyleSheet(qdarkstyle.load_stylesheet())


    def Default(self):
        pass





my_app = QApplication()
window = MainWindow()
my_app.exec()