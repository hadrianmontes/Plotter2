# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(1038, 648)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/appicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.open = QtGui.QToolButton(Dialog)
        self.open.setEnabled(True)
        self.open.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/abrir.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.open.setIcon(icon1)
        self.open.setIconSize(QtCore.QSize(16, 16))
        self.open.setCheckable(False)
        self.open.setAutoRaise(False)
        self.open.setArrowType(QtCore.Qt.NoArrow)
        self.open.setObjectName(_fromUtf8("open"))
        self.horizontalLayout.addWidget(self.open)
        self.save = QtGui.QToolButton(Dialog)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout.addWidget(self.save, QtCore.Qt.AlignLeft)
        self.export_2 = QtGui.QToolButton(Dialog)
        self.export_2.setObjectName(_fromUtf8("export_2"))
        self.horizontalLayout.addWidget(self.export_2)
        self.undo = QtGui.QToolButton(Dialog)
        self.undo.setObjectName(_fromUtf8("undo"))
        self.horizontalLayout.addWidget(self.undo)
        self.redo = QtGui.QToolButton(Dialog)
        self.redo.setObjectName(_fromUtf8("redo"))
        self.horizontalLayout.addWidget(self.redo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.Layout_2 = QtGui.QGridLayout()
        self.Layout_2.setObjectName(_fromUtf8("Layout_2"))
        self.gridLayout_2.addLayout(self.Layout_2, 1, 0, 15, 1)
        self.layout_3 = QtGui.QGridLayout()
        self.layout_3.setObjectName(_fromUtf8("layout_3"))
        self.gridLayout_2.addLayout(self.layout_3, 1, 1, 15, 1)
        self.layout_4 = QtGui.QGridLayout()
        self.layout_4.setObjectName(_fromUtf8("layout_4"))
        self.gridLayout_2.addLayout(self.layout_4, 16, 0, 5, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.open.setText(_translate("Dialog", "open", None))
        self.save.setText(_translate("Dialog", "save", None))
        self.export_2.setText(_translate("Dialog", "export", None))
        self.undo.setText(_translate("Dialog", "undo", None))
        self.redo.setText(_translate("Dialog", "redo", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

