from ui.preferences_dialog import Ui_Options
from PyQt4 import QtGui

class PreferencesDialog(Ui_Options):
    def __init__(self,*args,**kwargs):
        super(PreferencesDialog,self).__init__(*args,**kwargs)

    def setupUi(self,MainWindow):
        self.parent=MainWindow
        super(PreferencesDialog,self).setupUi(MainWindow)
