from PyQt5 import QtCore, QtGui, QtWidgets
		
class Shapka2():
    def setShapka2(table1, mode1):
        _translate = QtCore.QCoreApplication.translate						
        if (mode1 == 1):	
            table1.setColumnCount(6)
            table1.setColumnWidth(0, 140);
            table1.setColumnWidth(1, 240);
            table1.setColumnWidth(2, 90);		
            table1.setColumnWidth(3, 80);
            table1.setColumnWidth(4, 110);
            table1.setColumnWidth(5, 200);

            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(5, item)

            item = table1.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Логин"))
            item = table1.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Полное имя"))
            item = table1.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Год рождения"))
            item = table1.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Профессия"))
            item = table1.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Город"))
            item = table1.horizontalHeaderItem(5)
            item.setText(_translate("MainWindow", "Адрес электронной почты"))
        elif (mode1 == 2):	
            table1.setColumnCount(7)
            table1.setColumnWidth(0, 240);
            table1.setColumnWidth(1, 90);
            table1.setColumnWidth(2, 110);		
            table1.setColumnWidth(3, 180);
            table1.setColumnWidth(4, 110);
            table1.setColumnWidth(5, 100);
            table1.setColumnWidth(6, 100);

            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(5, item)
            item = QtWidgets.QTableWidgetItem()
            table1.setHorizontalHeaderItem(6, item)

            item = table1.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Полное имя"))
            item = table1.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Год рождения"))
            item = table1.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Профессия"))
            item = table1.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Город"))
            item = table1.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Дата ответа"))
            item = table1.horizontalHeaderItem(5)
            item.setText(_translate("MainWindow", "Номер ответа"))
            item = table1.horizontalHeaderItem(6)
            item.setText(_translate("MainWindow", "Значение ответа"))
							