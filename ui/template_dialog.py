# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templater.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(584, 385)
        Dialog.setMouseTracking(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3, QtCore.Qt.AlignRight)
        self.ncol = QtGui.QSpinBox(self.widget)
        self.ncol.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ncol.setMinimum(1)
        self.ncol.setObjectName(_fromUtf8("ncol"))
        self.horizontalLayout.addWidget(self.ncol, QtCore.Qt.AlignLeft)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4, QtCore.Qt.AlignRight)
        self.nrow = QtGui.QSpinBox(self.widget)
        self.nrow.setMaximumSize(QtCore.QSize(50, 16777215))
        self.nrow.setMinimum(1)
        self.nrow.setObjectName(_fromUtf8("nrow"))
        self.horizontalLayout.addWidget(self.nrow)
        self.set_but = QtGui.QPushButton(self.widget)
        self.set_but.setObjectName(_fromUtf8("set_but"))
        self.horizontalLayout.addWidget(self.set_but, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.preview_but = QtGui.QPushButton(self.frame_2)
        self.preview_but.setObjectName(_fromUtf8("preview_but"))
        self.gridLayout_3.addWidget(self.preview_but, 1, 0, 1, 1)
        self.dialog_buttons = QtGui.QDialogButtonBox(self.frame_2)
        self.dialog_buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName(_fromUtf8("dialog_buttons"))
        self.gridLayout_3.addWidget(self.dialog_buttons, 1, 1, 1, 1)
        self.table_template = QtGui.QTableWidget(self.frame_2)
        self.table_template.setMouseTracking(True)
        self.table_template.setRowCount(0)
        self.table_template.setColumnCount(0)
        self.table_template.setObjectName(_fromUtf8("table_template"))
        self.table_template.horizontalHeader().setVisible(False)
        self.table_template.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.table_template, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "This will setup the grid that will be the basis of the geometry", None))
        self.label.setText(_translate("Dialog", "Select basis layout grid.", None))
        self.label_3.setText(_translate("Dialog", "Number of columns:", None))
        self.label_4.setText(_translate("Dialog", "Number of rows:", None))
        self.set_but.setText(_translate("Dialog", "Set", None))
        self.preview_but.setText(_translate("Dialog", "Preview", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

