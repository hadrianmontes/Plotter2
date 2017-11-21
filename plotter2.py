from interface import Plotter2
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Plotter2()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
