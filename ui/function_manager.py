# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_manager.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fitmanager(object):
    def setupUi(self, functionmanager):
        functionmanager.setObjectName(_fromUtf8("functionmanager"))
        functionmanager.setGeometry(QtCore.QRect(0, 0, 591, 303))
        self.gridLayout_2 = QtGui.QGridLayout(functionmanager)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.name_val = QtGui.QLineEdit(functionmanager)
        self.name_val.setObjectName(_fromUtf8("name_val"))
        self.gridLayout_2.addWidget(self.name_val, 1, 1, 1, 5)
        self.new_button = QtGui.QPushButton(functionmanager)
        self.new_button.setObjectName(_fromUtf8("new_button"))
        self.gridLayout_2.addWidget(self.new_button, 0, 6, 1, 1)
        self.save_button = QtGui.QPushButton(functionmanager)
        self.save_button.setEnabled(False)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.gridLayout_2.addWidget(self.save_button, 3, 6, 1, 1)
        self.label_2 = QtGui.QLabel(functionmanager)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.combo_list = QtGui.QComboBox(functionmanager)
        self.combo_list.setObjectName(_fromUtf8("combo_list"))
        self.gridLayout_2.addWidget(self.combo_list, 0, 0, 1, 6)
        self.scrollArea = QtGui.QScrollArea(functionmanager)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 453, 184))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.table_values = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.table_values.setRowCount(2)
        self.table_values.setColumnCount(2)
        self.table_values.setObjectName(_fromUtf8("table_values"))
        self.gridLayout.addWidget(self.table_values, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 6)
        self.label = QtGui.QLabel(functionmanager)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.string_val = QtGui.QLineEdit(functionmanager)
        self.string_val.setObjectName(_fromUtf8("string_val"))
        self.gridLayout_2.addWidget(self.string_val, 3, 1, 1, 5)

        self.retranslateUi(functionmanager)
        QtCore.QMetaObject.connectSlotsByName(functionmanager)

    def retranslateUi(self, functionmanager):
        functionmanager.setWindowTitle(_translate("fitmanager", "Dialog", None))
        self.new_button.setText(_translate("fitmanager", "Add Function", None))
        self.save_button.setText(_translate("fitmanager", "Save Function", None))
        self.label_2.setText(_translate("fitmanager", "Name", None))
        self.label.setText(_translate("fitmanager", "function y=", None))

