# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotter.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1106, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/appicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.layout_1 = QtGui.QHBoxLayout()
        self.layout_1.setObjectName(_fromUtf8("layout_1"))
        self.open = QtGui.QToolButton(self.centralwidget)
        self.open.setFocusPolicy(QtCore.Qt.TabFocus)
        self.open.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/abrir.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.open.setIcon(icon1)
        self.open.setObjectName(_fromUtf8("open"))
        self.layout_1.addWidget(self.open)
        self.save = QtGui.QToolButton(self.centralwidget)
        self.save.setFocusPolicy(QtCore.Qt.TabFocus)
        self.save.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.save.setIcon(icon2)
        self.save.setObjectName(_fromUtf8("save"))
        self.layout_1.addWidget(self.save)
        self.export_2 = QtGui.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/export.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.export_2.setIcon(icon3)
        self.export_2.setObjectName(_fromUtf8("export_2"))
        self.layout_1.addWidget(self.export_2)
        self.undo = QtGui.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.undo.setIcon(icon4)
        self.undo.setObjectName(_fromUtf8("undo"))
        self.layout_1.addWidget(self.undo)
        self.redo = QtGui.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.redo.setIcon(icon5)
        self.redo.setObjectName(_fromUtf8("redo"))
        self.layout_1.addWidget(self.redo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_1.addItem(spacerItem)
        self.gridLayout.addLayout(self.layout_1, 0, 0, 1, 2)
        self.layout_3 = QtGui.QGridLayout()
        self.layout_3.setObjectName(_fromUtf8("layout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.layout_3, 1, 1, 15, 1)
        self.layout_4 = QtGui.QGridLayout()
        self.layout_4.setObjectName(_fromUtf8("layout_4"))
        self.plot_table = QtGui.QTableWidget(self.centralwidget)
        self.plot_table.setMaximumSize(QtCore.QSize(16777215, 120))
        self.plot_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plot_table.setObjectName(_fromUtf8("plot_table"))
        self.plot_table.setColumnCount(0)
        self.plot_table.setRowCount(0)
        self.layout_4.addWidget(self.plot_table, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.layout_4, 16, 0, 5, 2)
        self.layout_2 = QtGui.QGridLayout()
        self.layout_2.setObjectName(_fromUtf8("layout_2"))
        self.properties_tab = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.properties_tab.sizePolicy().hasHeightForWidth())
        self.properties_tab.setSizePolicy(sizePolicy)
        self.properties_tab.setMaximumSize(QtCore.QSize(550, 16777215))
        self.properties_tab.setObjectName(_fromUtf8("properties_tab"))
        self.figure_tab = QtGui.QWidget()
        self.figure_tab.setObjectName(_fromUtf8("figure_tab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.figure_tab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.frame = QtGui.QFrame(self.figure_tab)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_9 = QtGui.QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_17 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_9.addWidget(self.label_21, 4, 0, 1, 2)
        self.label_18 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_9.addWidget(self.label_18, 1, 0, 1, 3)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_19 = QtGui.QLabel(self.frame_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout.addWidget(self.label_19)
        self.ncol_template = QtGui.QSpinBox(self.frame_3)
        self.ncol_template.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ncol_template.setMinimum(1)
        self.ncol_template.setObjectName(_fromUtf8("ncol_template"))
        self.horizontalLayout.addWidget(self.ncol_template)
        self.label_20 = QtGui.QLabel(self.frame_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout.addWidget(self.label_20)
        self.nrow_template = QtGui.QSpinBox(self.frame_3)
        self.nrow_template.setMaximumSize(QtCore.QSize(50, 16777215))
        self.nrow_template.setMinimum(1)
        self.nrow_template.setObjectName(_fromUtf8("nrow_template"))
        self.horizontalLayout.addWidget(self.nrow_template)
        self.set_template_but = QtGui.QPushButton(self.frame_3)
        self.set_template_but.setObjectName(_fromUtf8("set_template_but"))
        self.horizontalLayout.addWidget(self.set_template_but)
        self.gridLayout_9.addWidget(self.frame_3, 2, 0, 1, 3)
        self.advanced_template_but = QtGui.QPushButton(self.frame)
        self.advanced_template_but.setObjectName(_fromUtf8("advanced_template_but"))
        self.gridLayout_9.addWidget(self.advanced_template_but, 5, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.figure_tab)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.joiny_but = QtGui.QPushButton(self.frame_2)
        self.joiny_but.setObjectName(_fromUtf8("joiny_but"))
        self.gridLayout_3.addWidget(self.joiny_but, 1, 2, 1, 1)
        self.optimize_space_but = QtGui.QPushButton(self.frame_2)
        self.optimize_space_but.setObjectName(_fromUtf8("optimize_space_but"))
        self.gridLayout_3.addWidget(self.optimize_space_but, 1, 0, 1, 1)
        self.joinx_but = QtGui.QPushButton(self.frame_2)
        self.joinx_but.setObjectName(_fromUtf8("joinx_but"))
        self.gridLayout_3.addWidget(self.joinx_but, 1, 1, 1, 1)
        self.joinxy_but = QtGui.QPushButton(self.frame_2)
        self.joinxy_but.setObjectName(_fromUtf8("joinxy_but"))
        self.gridLayout_3.addWidget(self.joinxy_but, 1, 3, 1, 1)
        self.label_22 = QtGui.QLabel(self.frame_2)
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 4)
        self.gridLayout_8.addWidget(self.frame_2, 1, 0, 1, 1)
        self.properties_tab.addTab(self.figure_tab, _fromUtf8(""))
        self.axis_prop = QtGui.QWidget()
        self.axis_prop.setObjectName(_fromUtf8("axis_prop"))
        self.gridLayout_2 = QtGui.QGridLayout(self.axis_prop)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame_5 = QtGui.QFrame(self.axis_prop)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_11 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.label_6 = QtGui.QLabel(self.frame_5)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_11.addWidget(self.label_6, 0, 0, 1, 1)
        self.decimal_but = QtGui.QPushButton(self.frame_5)
        self.decimal_but.setObjectName(_fromUtf8("decimal_but"))
        self.gridLayout_11.addWidget(self.decimal_but, 1, 0, 1, 1)
        self.semilogx_but = QtGui.QPushButton(self.frame_5)
        self.semilogx_but.setObjectName(_fromUtf8("semilogx_but"))
        self.gridLayout_11.addWidget(self.semilogx_but, 1, 1, 1, 1)
        self.semilogy_but = QtGui.QPushButton(self.frame_5)
        self.semilogy_but.setObjectName(_fromUtf8("semilogy_but"))
        self.gridLayout_11.addWidget(self.semilogy_but, 1, 2, 1, 1)
        self.loglog_but = QtGui.QPushButton(self.frame_5)
        self.loglog_but.setObjectName(_fromUtf8("loglog_but"))
        self.gridLayout_11.addWidget(self.loglog_but, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 2)
        self.frame_4 = QtGui.QFrame(self.axis_prop)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_10.addWidget(self.label_3, 1, 2, 1, 1)
        self.xmin_val = QtGui.QDoubleSpinBox(self.frame_4)
        self.xmin_val.setDecimals(4)
        self.xmin_val.setMinimum(-99999.99)
        self.xmin_val.setMaximum(99999.99)
        self.xmin_val.setSingleStep(0.5)
        self.xmin_val.setObjectName(_fromUtf8("xmin_val"))
        self.gridLayout_10.addWidget(self.xmin_val, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_10.addWidget(self.label_4, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.xmax_val = QtGui.QDoubleSpinBox(self.frame_4)
        self.xmax_val.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.xmax_val.setDecimals(4)
        self.xmax_val.setMinimum(-99999.99)
        self.xmax_val.setMaximum(99999.99)
        self.xmax_val.setSingleStep(0.5)
        self.xmax_val.setObjectName(_fromUtf8("xmax_val"))
        self.gridLayout_10.addWidget(self.xmax_val, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_10.addWidget(self.label_2, 1, 1, 1, 1)
        self.ymin_val = QtGui.QDoubleSpinBox(self.frame_4)
        self.ymin_val.setDecimals(4)
        self.ymin_val.setMinimum(-99999.99)
        self.ymin_val.setMaximum(99999.99)
        self.ymin_val.setSingleStep(0.5)
        self.ymin_val.setObjectName(_fromUtf8("ymin_val"))
        self.gridLayout_10.addWidget(self.ymin_val, 3, 1, 1, 1)
        self.ymax_val = QtGui.QDoubleSpinBox(self.frame_4)
        self.ymax_val.setDecimals(4)
        self.ymax_val.setMinimum(-99999.99)
        self.ymax_val.setMaximum(99999.99)
        self.ymax_val.setSingleStep(0.5)
        self.ymax_val.setObjectName(_fromUtf8("ymax_val"))
        self.gridLayout_10.addWidget(self.ymax_val, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_10.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 2)
        self.frame_6 = QtGui.QFrame(self.axis_prop)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_12 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.label_23 = QtGui.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_12.addWidget(self.label_23, 0, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.frame_6)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_12.addWidget(self.label_25, 1, 1, 1, 1)
        self.xlabel_box = QtGui.QLineEdit(self.frame_6)
        self.xlabel_box.setObjectName(_fromUtf8("xlabel_box"))
        self.gridLayout_12.addWidget(self.xlabel_box, 1, 2, 1, 1)
        self.ylabel_box = QtGui.QLineEdit(self.frame_6)
        self.ylabel_box.setObjectName(_fromUtf8("ylabel_box"))
        self.gridLayout_12.addWidget(self.ylabel_box, 2, 2, 1, 1)
        self.label_24 = QtGui.QLabel(self.frame_6)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_12.addWidget(self.label_24, 2, 1, 1, 1)
        self.setlabels_but = QtGui.QPushButton(self.frame_6)
        self.setlabels_but.setObjectName(_fromUtf8("setlabels_but"))
        self.gridLayout_12.addWidget(self.setlabels_but, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_6, 2, 0, 1, 2)
        self.frame_8 = QtGui.QFrame(self.axis_prop)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_14 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_27 = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_14.addWidget(self.label_27, 0, 0, 1, 1)
        self.showlegend = QtGui.QCheckBox(self.frame_8)
        self.showlegend.setObjectName(_fromUtf8("showlegend"))
        self.gridLayout_14.addWidget(self.showlegend, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 3, 0, 1, 2)
        self.properties_tab.addTab(self.axis_prop, _fromUtf8(""))
        self.add_data_tab = QtGui.QWidget()
        self.add_data_tab.setObjectName(_fromUtf8("add_data_tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.add_data_tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.file_path_open = QtGui.QPushButton(self.add_data_tab)
        self.file_path_open.setObjectName(_fromUtf8("file_path_open"))
        self.gridLayout_4.addWidget(self.file_path_open, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.add_data_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.file_path_box = QtGui.QLineEdit(self.add_data_tab)
        self.file_path_box.setObjectName(_fromUtf8("file_path_box"))
        self.gridLayout_4.addWidget(self.file_path_box, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_10 = QtGui.QLabel(self.add_data_tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_6.addWidget(self.label_10, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_9 = QtGui.QLabel(self.add_data_tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.xcolumn_index = QtGui.QSpinBox(self.add_data_tab)
        self.xcolumn_index.setMaximum(999)
        self.xcolumn_index.setObjectName(_fromUtf8("xcolumn_index"))
        self.gridLayout_6.addWidget(self.xcolumn_index, 1, 1, 1, 1)
        self.y_column_index = QtGui.QSpinBox(self.add_data_tab)
        self.y_column_index.setProperty("value", 1)
        self.y_column_index.setObjectName(_fromUtf8("y_column_index"))
        self.gridLayout_6.addWidget(self.y_column_index, 1, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.add_data_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 4)
        self.gridLayout_5.addLayout(self.gridLayout_6, 2, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_13 = QtGui.QLabel(self.add_data_tab)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_7.addWidget(self.label_13, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.bocDiffColor = QtGui.QCheckBox(self.add_data_tab)
        self.bocDiffColor.setTristate(False)
        self.bocDiffColor.setObjectName(_fromUtf8("bocDiffColor"))
        self.gridLayout_7.addWidget(self.bocDiffColor, 3, 2, 1, 2, QtCore.Qt.AlignRight)
        self.comboMarker = QtGui.QComboBox(self.add_data_tab)
        self.comboMarker.setObjectName(_fromUtf8("comboMarker"))
        self.comboMarker.addItem(_fromUtf8(""))
        self.comboMarker.addItem(_fromUtf8(""))
        self.comboMarker.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboMarker, 2, 3, 1, 1)
        self.comboLinestyle = QtGui.QComboBox(self.add_data_tab)
        self.comboLinestyle.setMinimumSize(QtCore.QSize(130, 0))
        self.comboLinestyle.setObjectName(_fromUtf8("comboLinestyle"))
        self.comboLinestyle.addItem(_fromUtf8(""))
        self.comboLinestyle.addItem(_fromUtf8(""))
        self.comboLinestyle.addItem(_fromUtf8(""))
        self.comboLinestyle.addItem(_fromUtf8(""))
        self.comboLinestyle.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboLinestyle, 2, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.add_data_tab)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_7.addWidget(self.label_14, 3, 0, 1, 1)
        self.comboColor = QtGui.QComboBox(self.add_data_tab)
        self.comboColor.setObjectName(_fromUtf8("comboColor"))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.comboColor.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboColor, 3, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.add_data_tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.add_data_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 4)
        self.label_15 = QtGui.QLabel(self.add_data_tab)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_7.addWidget(self.label_15, 4, 0, 1, 1)
        self.comboMarkerColor = QtGui.QComboBox(self.add_data_tab)
        self.comboMarkerColor.setObjectName(_fromUtf8("comboMarkerColor"))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.comboMarkerColor.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboMarkerColor, 4, 1, 1, 1)
        self.plot_but = QtGui.QPushButton(self.add_data_tab)
        self.plot_but.setObjectName(_fromUtf8("plot_but"))
        self.gridLayout_7.addWidget(self.plot_but, 5, 3, 1, 1)
        self.label_16 = QtGui.QLabel(self.add_data_tab)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_7.addWidget(self.label_16, 4, 2, 1, 1)
        self.comboEdgeColor = QtGui.QComboBox(self.add_data_tab)
        self.comboEdgeColor.setObjectName(_fromUtf8("comboEdgeColor"))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.comboEdgeColor.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboEdgeColor, 4, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 3, 0, 1, 1)
        self.frame_7 = QtGui.QFrame(self.add_data_tab)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_13 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_26 = QtGui.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_13.addWidget(self.label_26, 0, 0, 1, 1)
        self.plotlabel_box = QtGui.QLineEdit(self.frame_7)
        self.plotlabel_box.setObjectName(_fromUtf8("plotlabel_box"))
        self.gridLayout_13.addWidget(self.plotlabel_box, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_7, 1, 0, 1, 1)
        self.properties_tab.addTab(self.add_data_tab, _fromUtf8(""))
        self.layout_2.addWidget(self.properties_tab, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.layout_2, 1, 0, 15, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionSet_Template = QtGui.QAction(MainWindow)
        self.actionSet_Template.setObjectName(_fromUtf8("actionSet_Template"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExport)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.properties_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.open, self.save)
        MainWindow.setTabOrder(self.save, self.export_2)
        MainWindow.setTabOrder(self.export_2, self.undo)
        MainWindow.setTabOrder(self.undo, self.redo)
        MainWindow.setTabOrder(self.redo, self.properties_tab)
        MainWindow.setTabOrder(self.properties_tab, self.ncol_template)
        MainWindow.setTabOrder(self.ncol_template, self.nrow_template)
        MainWindow.setTabOrder(self.nrow_template, self.set_template_but)
        MainWindow.setTabOrder(self.set_template_but, self.advanced_template_but)
        MainWindow.setTabOrder(self.advanced_template_but, self.optimize_space_but)
        MainWindow.setTabOrder(self.optimize_space_but, self.joinx_but)
        MainWindow.setTabOrder(self.joinx_but, self.joiny_but)
        MainWindow.setTabOrder(self.joiny_but, self.joinxy_but)
        MainWindow.setTabOrder(self.joinxy_but, self.xmin_val)
        MainWindow.setTabOrder(self.xmin_val, self.xmax_val)
        MainWindow.setTabOrder(self.xmax_val, self.ymin_val)
        MainWindow.setTabOrder(self.ymin_val, self.ymax_val)
        MainWindow.setTabOrder(self.ymax_val, self.decimal_but)
        MainWindow.setTabOrder(self.decimal_but, self.semilogx_but)
        MainWindow.setTabOrder(self.semilogx_but, self.semilogy_but)
        MainWindow.setTabOrder(self.semilogy_but, self.loglog_but)
        MainWindow.setTabOrder(self.loglog_but, self.file_path_box)
        MainWindow.setTabOrder(self.file_path_box, self.file_path_open)
        MainWindow.setTabOrder(self.file_path_open, self.xcolumn_index)
        MainWindow.setTabOrder(self.xcolumn_index, self.y_column_index)
        MainWindow.setTabOrder(self.y_column_index, self.comboLinestyle)
        MainWindow.setTabOrder(self.comboLinestyle, self.comboMarker)
        MainWindow.setTabOrder(self.comboMarker, self.comboColor)
        MainWindow.setTabOrder(self.comboColor, self.bocDiffColor)
        MainWindow.setTabOrder(self.bocDiffColor, self.comboMarkerColor)
        MainWindow.setTabOrder(self.comboMarkerColor, self.comboEdgeColor)
        MainWindow.setTabOrder(self.comboEdgeColor, self.plot_but)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotter", None))
        self.export_2.setText(_translate("MainWindow", "export", None))
        self.undo.setText(_translate("MainWindow", "undo", None))
        self.redo.setText(_translate("MainWindow", "redo", None))
        self.label_17.setText(_translate("MainWindow", "Set the figure template", None))
        self.label_21.setText(_translate("MainWindow", "Advanced template (complex geometry of subplots using a grid):", None))
        self.label_18.setText(_translate("MainWindow", "Simple template (all the subplots are of the same size):", None))
        self.label_19.setText(_translate("MainWindow", "Number of columns:", None))
        self.label_20.setText(_translate("MainWindow", "Number of rows:", None))
        self.set_template_but.setText(_translate("MainWindow", "Set", None))
        self.advanced_template_but.setText(_translate("MainWindow", "Advanced Template", None))
        self.joiny_but.setText(_translate("MainWindow", "Join Y Axes", None))
        self.optimize_space_but.setText(_translate("MainWindow", "Optimize Space", None))
        self.joinx_but.setText(_translate("MainWindow", "Join X Axes", None))
        self.joinxy_but.setText(_translate("MainWindow", "Join XY Axes", None))
        self.label_22.setText(_translate("MainWindow", "Mange space between plots", None))
        self.properties_tab.setTabText(self.properties_tab.indexOf(self.figure_tab), _translate("MainWindow", "Figure", None))
        self.label_6.setText(_translate("MainWindow", "Axis Scale", None))
        self.decimal_but.setText(_translate("MainWindow", "Decimal", None))
        self.semilogx_but.setText(_translate("MainWindow", "Semilog X", None))
        self.semilogy_but.setText(_translate("MainWindow", "Semilog Y", None))
        self.loglog_but.setText(_translate("MainWindow", "Log Log", None))
        self.label.setText(_translate("MainWindow", "Axis Limits", None))
        self.label_3.setText(_translate("MainWindow", "Max", None))
        self.label_4.setText(_translate("MainWindow", "X Axis", None))
        self.label_2.setText(_translate("MainWindow", "Min", None))
        self.label_5.setText(_translate("MainWindow", "Y Axis", None))
        self.label_23.setText(_translate("MainWindow", "Axis Labels", None))
        self.label_25.setText(_translate("MainWindow", "X Axis:", None))
        self.label_24.setText(_translate("MainWindow", "Y Axis", None))
        self.setlabels_but.setText(_translate("MainWindow", "Set", None))
        self.label_27.setText(_translate("MainWindow", "Legend", None))
        self.showlegend.setText(_translate("MainWindow", "Show Legend", None))
        self.properties_tab.setTabText(self.properties_tab.indexOf(self.axis_prop), _translate("MainWindow", "Axis Properties", None))
        self.file_path_open.setText(_translate("MainWindow", "Open", None))
        self.label_7.setText(_translate("MainWindow", "Select the file from which the data wil be read:", None))
        self.label_10.setText(_translate("MainWindow", "Y:", None))
        self.label_9.setText(_translate("MainWindow", "X.", None))
        self.label_8.setText(_translate("MainWindow", "Select the column of the file where\n"
"the x and y data should be read from:", None))
        self.label_13.setText(_translate("MainWindow", "Marker", None))
        self.bocDiffColor.setText(_translate("MainWindow", "Use different \n"
"color for marker", None))
        self.comboMarker.setItemText(0, _translate("MainWindow", "None", None))
        self.comboMarker.setItemText(1, _translate("MainWindow", "Point \".\"", None))
        self.comboMarker.setItemText(2, _translate("MainWindow", "Circle \"o\"", None))
        self.comboLinestyle.setItemText(0, _translate("MainWindow", "Solid: \"-\"", None))
        self.comboLinestyle.setItemText(1, _translate("MainWindow", "Dasded: \"--\"", None))
        self.comboLinestyle.setItemText(2, _translate("MainWindow", "Pointed \"..\"", None))
        self.comboLinestyle.setItemText(3, _translate("MainWindow", "Dash point: \"-.\"", None))
        self.comboLinestyle.setItemText(4, _translate("MainWindow", "None", None))
        self.label_14.setText(_translate("MainWindow", "Color", None))
        self.comboColor.setItemText(0, _translate("MainWindow", "Auto", None))
        self.comboColor.setItemText(1, _translate("MainWindow", "Black", None))
        self.comboColor.setItemText(2, _translate("MainWindow", "Blue", None))
        self.comboColor.setItemText(3, _translate("MainWindow", "Cyan", None))
        self.comboColor.setItemText(4, _translate("MainWindow", "Green", None))
        self.comboColor.setItemText(5, _translate("MainWindow", "Pink", None))
        self.comboColor.setItemText(6, _translate("MainWindow", "Red", None))
        self.comboColor.setItemText(7, _translate("MainWindow", "Yellow", None))
        self.label_12.setText(_translate("MainWindow", "Line Style", None))
        self.label_11.setText(_translate("MainWindow", "Line and marker porperties:", None))
        self.label_15.setText(_translate("MainWindow", "Marker Face\n"
"       Color", None))
        self.comboMarkerColor.setItemText(0, _translate("MainWindow", "Black", None))
        self.comboMarkerColor.setItemText(1, _translate("MainWindow", "Blue", None))
        self.comboMarkerColor.setItemText(2, _translate("MainWindow", "Cyan", None))
        self.comboMarkerColor.setItemText(3, _translate("MainWindow", "Green", None))
        self.comboMarkerColor.setItemText(4, _translate("MainWindow", "Red", None))
        self.comboMarkerColor.setItemText(5, _translate("MainWindow", "Pink", None))
        self.comboMarkerColor.setItemText(6, _translate("MainWindow", "Yellow", None))
        self.plot_but.setText(_translate("MainWindow", "Plot", None))
        self.label_16.setText(_translate("MainWindow", "Marker Edge\n"
"         Color", None))
        self.comboEdgeColor.setItemText(0, _translate("MainWindow", "Black", None))
        self.comboEdgeColor.setItemText(1, _translate("MainWindow", "Blue", None))
        self.comboEdgeColor.setItemText(2, _translate("MainWindow", "Cyan", None))
        self.comboEdgeColor.setItemText(3, _translate("MainWindow", "Green", None))
        self.comboEdgeColor.setItemText(4, _translate("MainWindow", "Pink", None))
        self.comboEdgeColor.setItemText(5, _translate("MainWindow", "Red", None))
        self.comboEdgeColor.setItemText(6, _translate("MainWindow", "Yellow", None))
        self.label_26.setText(_translate("MainWindow", "Set a label for the plot (optional)", None))
        self.properties_tab.setTabText(self.properties_tab.indexOf(self.add_data_tab), _translate("MainWindow", "Add Data From File", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionSet_Template.setText(_translate("MainWindow", "Set Template", None))

import plot_resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

