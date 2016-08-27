from ui.template_dialog import Ui_Dialog
from PyQt4 import QtGui
import matplotlib.pyplot as plt
from axes_template import axes_template
from time import sleep

class TemplateDialog(Ui_Dialog):
    def __init__(self,*args,**kwargs):
        self.selectedIndex=False
        super(TemplateDialog,self).__init__(*args,**kwargs)

    def setupUi(self,MainWindow):
        self.parent=MainWindow
        super(TemplateDialog,self).setupUi(MainWindow)
        self.set_but.clicked.connect(self.setColRow)
        self.table_template.itemSelectionChanged.connect(self.increase_selection)
        self.table_template.cellPressed.connect(self.selected_item)
        self.preview_but.clicked.connect(self.preview)
        self.dialog_buttons.accepted.connect(self.accept)
        self.dialog_buttons.rejected.connect(self.reject)
        self.setColRow()

    def setColRow(self):
        ncol=self.ncol.value()
        self.table_template.setColumnCount(ncol)
        nrow=self.nrow.value()
        self.table_template.setRowCount(nrow)
        index=0
        self.matrix=[]
        for i in range(nrow):
            self.matrix.append([])
            for j in range(ncol):
                index+=1
                self.matrix[-1].append(index)
                item=QtGui.QTableWidgetItem(str(index))
                self.table_template.setItem(i,j,item)

        self.prematrix=[]
        for i in range(len(self.matrix)):
            self.prematrix.append([])
            for j in range(len(self.matrix[0])):
                self.prematrix[-1].append(self.matrix[i][j])

    def selected_item(self):
        # print(self.table_template.selectedIndexes())
        index=self.table_template.currentIndex()
        self.selectedIndex=self.prematrix[index.row()][index.column()]
        self.prematrix=[]
        for i in range(len(self.matrix)):
            self.prematrix.append([])
            for j in range(len(self.matrix[0])):
                self.prematrix[-1].append(self.matrix[i][j])

        self.startingIn=(index.row(),index.column())
        # print(index.row(),index.column(),self.selectedIndex)

    def increase_selection(self):
        if not self.selectedIndex:
            return
        indexes=self.table_template.selectedIndexes()
        for index in indexes:
            row=index.row()
            column=index.column()
            self.matrix[row][column]=self.selectedIndex
            item=QtGui.QTableWidgetItem(str(self.selectedIndex))
            self.table_template.setItem(row,column,item)

    def preview(self):
        template=axes_template(matrix=self.matrix)
        fig=template.generate_preview()
        fig.show()
        sleep(5)
        plt.close(fig)

    def accept(self):
        self.parent.accept()

    def reject(self):
        self.parent.close()
