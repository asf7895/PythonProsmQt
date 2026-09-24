import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import dbf

#class ZagruzDialog(QtWidgets.QDialog):
class ErrorDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):                      # + parent
        super(ErrorDialog,self).__init__(parent)            #
        #super().__init__()
        self.parent = parent                              # 
        self.conn2 = parent.conn     

        self.setObjectName("ErrorWindow")
        self.setWindowTitle('Сообщение об ошибке')

        self.retranslateUi()
		
    def closeEvent(self, event):                            # +++
        self.parent.show()


    def retranslateUi(self):
        self.label1 = QtWidgets.QLabel(self)
        _translate = QtCore.QCoreApplication.translate
        self.setGeometry(100, 100, 740, 144)
        self.label1.setText(_translate("ErrorWindow", self.parent.errmsg1))
        self.label1.setGeometry(QtCore.QRect(40, 40, 675, 86))


