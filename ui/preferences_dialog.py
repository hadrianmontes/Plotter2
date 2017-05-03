# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences_dialog.ui'
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

class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName(_fromUtf8("Options"))
        Options.resize(668, 370)
        self.gridLayout = QtGui.QGridLayout(Options)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Options)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tickmat1 = QtGui.QRadioButton(self.widget_2)
        self.tickmat1.setObjectName(_fromUtf8("tickmat1"))
        self.gridLayout_3.addWidget(self.tickmat1, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.widget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)
        self.label = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.tickmat2 = QtGui.QRadioButton(self.widget_2)
        self.tickmat2.setObjectName(_fromUtf8("tickmat2"))
        self.gridLayout_3.addWidget(self.tickmat2, 2, 1, 1, 1)
        self.tickcust = QtGui.QRadioButton(self.widget_2)
        self.tickcust.setObjectName(_fromUtf8("tickcust"))
        self.gridLayout_3.addWidget(self.tickcust, 2, 2, 1, 1)
        self.widget_4 = QtGui.QWidget(self.widget_2)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_5 = QtGui.QLabel(self.widget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtGui.QLabel(self.widget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.topcheck = QtGui.QCheckBox(self.widget_4)
        self.topcheck.setText(_fromUtf8(""))
        self.topcheck.setObjectName(_fromUtf8("topcheck"))
        self.gridLayout_4.addWidget(self.topcheck, 1, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.label_2 = QtGui.QLabel(self.widget_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.leftcheck = QtGui.QCheckBox(self.widget_4)
        self.leftcheck.setText(_fromUtf8(""))
        self.leftcheck.setObjectName(_fromUtf8("leftcheck"))
        self.gridLayout_4.addWidget(self.leftcheck, 2, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.label_3 = QtGui.QLabel(self.widget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.ytickcombo = QtGui.QComboBox(self.widget_4)
        self.ytickcombo.setObjectName(_fromUtf8("ytickcombo"))
        self.ytickcombo.addItem(_fromUtf8(""))
        self.ytickcombo.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.ytickcombo, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.xtickcombo = QtGui.QComboBox(self.widget_4)
        self.xtickcombo.setObjectName(_fromUtf8("xtickcombo"))
        self.xtickcombo.addItem(_fromUtf8(""))
        self.xtickcombo.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.xtickcombo, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_3.addWidget(self.widget_4, 3, 0, 1, 3)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Options)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        Options.setWindowTitle(_translate("Options", "Preferences", None))
        self.tickmat1.setText(_translate("Options", "Matplotlib 1", None))
        self.label.setText(_translate("Options", "Ticks", None))
        self.tickmat2.setText(_translate("Options", "Matplotlib2", None))
        self.tickcust.setText(_translate("Options", "Custom", None))
        self.label_5.setText(_translate("Options", "Left ticks", None))
        self.label_4.setText(_translate("Options", "Top ticks", None))
        self.label_2.setText(_translate("Options", "Xtick Direction", None))
        self.label_3.setText(_translate("Options", "Ytick DIrection", None))
        self.ytickcombo.setItemText(0, _translate("Options", "In", None))
        self.ytickcombo.setItemText(1, _translate("Options", "Out", None))
        self.xtickcombo.setItemText(0, _translate("Options", "In", None))
        self.xtickcombo.setItemText(1, _translate("Options", "Out", None))

