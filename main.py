# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit

import ListManager


class Ui_MainWindow(object):
    def __init__(self):
        self.cheese_list = ListManager.ListManager('canadianCheeseDirectory.csv', 'canadianCheeseDirectory.sqlite')
        self.cheese_list.csv_to_dataframe()
        self.cheese_list.dataframe_to_database_table()
        self.cheese_list.dataframe_to_list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 740)

        self.input_CheeseId = QLineEdit(MainWindow)
        self.input_CheeseNameEn = QLineEdit(MainWindow)
        self.input_ManufacturerNameEn = QLineEdit(MainWindow)
        self.input_ManufacturerProvCode = QLineEdit(MainWindow)
        self.input_ManufacturingTypeEn = QLineEdit(MainWindow)
        self.input_WebSiteEn = QLineEdit(MainWindow)
        self.input_FatContentPercent = QLineEdit(MainWindow)
        self.input_MoisturePercent = QLineEdit(MainWindow)
        self.input_ParticularitiesEn = QLineEdit(MainWindow)
        self.input_FlavourEn = QLineEdit(MainWindow)
        self.input_CharacteristicsEn = QLineEdit(MainWindow)
        self.input_RipeningEn = QLineEdit(MainWindow)
        self.input_Organic = QLineEdit(MainWindow)
        self.input_CategoryTypeEn = QLineEdit(MainWindow)
        self.input_MilkTypeEn = QLineEdit(MainWindow)
        self.input_MilkTreatmentTypeEn = QLineEdit(MainWindow)
        self.input_RindTypeEn = QLineEdit(MainWindow)
        self.input_LastUpdateDate = QLineEdit(MainWindow)
        self.input_editInput = QLineEdit(MainWindow)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(1250, 180, 75, 23))
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.deleteRecord)

        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(1250, 120, 75, 23))
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(self.showDialogAdd)

        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(1250, 150, 75, 23))
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(self.showDialogEdit)
        self.commit_button = QtWidgets.QPushButton(self.centralwidget)
        self.commit_button.setGeometry(QtCore.QRect(1250, 550, 75, 23))
        self.commit_button.setObjectName("Commit")
        self.commit_button.clicked.connect(self.cheese_list.commit_and_close)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(1250, 10, 75, 23))
        self.load_button.setObjectName("load_button")
        self.load_button.clicked.connect(self.loadData)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(00, 0, 1200, 720))
        self.tableWidget.setColumnCount(19)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sean Di Rienzo - Assignment #4"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.create_button.setText(_translate("MainWindow", "Create"))
        self.edit_button.setText(_translate("MainWindow", "Edit"))
        self.commit_button.setText(_translate("MainWindow", "Commit"))
        self.load_button.setText(_translate("MainWindow", "Load"))

    def loadData(self):
        self.tableWidget.clear()
        results = self.cheese_list.conn.execute("SELECT * FROM cheeseData")

        for row_number, row_data in enumerate(results):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def deleteRecord(self):

        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        self.tableWidget.removeRow(row)

        self.cheese_list.delete_at_index(row)

    def createRecord(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        tempObject = self.cheese_list.new_record(self.input_CheeseId, self.input_CheeseNameEn,
                                                 self.input_ManufacturerNameEn,
                                                 self.input_ManufacturerProvCode, self.input_ManufacturingTypeEn,
                                                 self.input_WebSiteEn, self.input_FatContentPercent,
                                                 self.input_MoisturePercent, self.input_ParticularitiesEn,
                                                 self.input_FlavourEn, self.input_CharacteristicsEn,
                                                 self.input_RipeningEn, self.input_Organic, self.input_CategoryTypeEn,
                                                 self.input_MilkTypeEn, self.input_MilkTreatmentTypeEn,
                                                 self.input_RindTypeEn, self.input_LastUpdateDate)

        self.cheese_list.add_record(tempObject)

        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0,
                                 QtWidgets.QTableWidgetItem(str(self.input_CheeseId)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1,
                                 QtWidgets.QTableWidgetItem(str(self.input_CheeseNameEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2,
                                 QtWidgets.QTableWidgetItem(str(self.input_ManufacturerNameEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3,
                                 QtWidgets.QTableWidgetItem(str(self.input_ManufacturerProvCode)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4,
                                 QtWidgets.QTableWidgetItem(str(self.input_ManufacturingTypeEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 5,
                                 QtWidgets.QTableWidgetItem(str(self.input_WebSiteEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 6,
                                 QtWidgets.QTableWidgetItem(str(self.input_FatContentPercent)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 7,
                                 QtWidgets.QTableWidgetItem(str(self.input_MoisturePercent)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 8,
                                 QtWidgets.QTableWidgetItem(str(self.input_ParticularitiesEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 9,
                                 QtWidgets.QTableWidgetItem(str(self.input_FlavourEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 10,
                                 QtWidgets.QTableWidgetItem(str(self.input_CharacteristicsEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 11,
                                 QtWidgets.QTableWidgetItem(str(self.input_RipeningEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 12,
                                 QtWidgets.QTableWidgetItem(str(self.input_Organic)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 13,
                                 QtWidgets.QTableWidgetItem(str(self.input_CategoryTypeEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 14,
                                 QtWidgets.QTableWidgetItem(str(self.input_MilkTypeEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 15,
                                 QtWidgets.QTableWidgetItem(str(self.input_MilkTreatmentTypeEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 16,
                                 QtWidgets.QTableWidgetItem(str(self.input_RindTypeEn)))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 17,
                                 QtWidgets.QTableWidgetItem(str(self.input_LastUpdateDate)))

    def editRecord(self):

        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        self.cheese_list.edit_at_index(row, column, self.input_editInput)
        self.cheese_list.edit_database_field(row, column, self.input_editInput)
        self.tableWidget.setItem(row, column,
                                 QtWidgets.QTableWidgetItem(str(self.input_editInput)))

    def showDialogAdd(self):

        text, okPressed = QInputDialog.getText(MainWindow, 'Input Dialog',
                                               'Enter your name:', QLineEdit.Normal)
        if okPressed:
            self.input_CheeseId = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'CheeseId', QLineEdit.Normal)
        if okPressed:
            self.input_CheeseNameEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'ManufacturerNameEn', QLineEdit.Normal)
        if okPressed:
            self.input_ManufacturerNameEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'ManufacturerProvCode', QLineEdit.Normal)
        if okPressed:
            self.input_ManufacturerProvCode = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'ManufacturingTypeEn', QLineEdit.Normal)
        if okPressed:
            self.input_ManufacturingTypeEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'WebSiteEn', QLineEdit.Normal)
        if okPressed:
            self.input_WebSiteEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'FatContentPercent', QLineEdit.Normal)
        if okPressed:
            self.input_FatContentPercent = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'MoisturePercent', QLineEdit.Normal)
        if okPressed:
            self.input_MoisturePercent = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'ParticularitiesEn', QLineEdit.Normal)
        if okPressed:
            self.input_ParticularitiesEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'FlavourEn', QLineEdit.Normal)
        if okPressed:
            self.input_FlavourEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'CharacteristicsEn', QLineEdit.Normal)
        if okPressed:
            self.input_CharacteristicsEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'RipeningEn', QLineEdit.Normal)
        if okPressed:
            self.input_RipeningEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'Organic', QLineEdit.Normal)
        if okPressed:
            self.input_Organic = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'CategoryTypeEn', QLineEdit.Normal)
        if okPressed:
            self.input_CategoryTypeEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'Enter your name', QLineEdit.Normal)
        if okPressed:
            self.input_MilkTypeEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'MilkTreatmentTypeEn', QLineEdit.Normal)
        if okPressed:
            self.input_MilkTreatmentTypeEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'RindTypeEn', QLineEdit.Normal)
        if okPressed:
            self.input_RindTypeEn = text

        text, okPressed = QInputDialog.getText(MainWindow, 'Field Creator', 'LastUpdateDateEn', QLineEdit.Normal)
        if okPressed:
            self.input_LastUpdateDate = text

        self.createRecord()

    def showDialogEdit(self):
        text, okPressed = QInputDialog.getText(MainWindow, 'Field Updater',
                                               "Replace with: ", QLineEdit.Normal)
        if okPressed:
            self.input_editInput = text
            self.editRecord()





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
