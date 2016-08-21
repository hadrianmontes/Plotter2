from PyQt4 import QtGui
from ui.mainwindow import Ui_MainWindow
from extended_figure import extended_figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class Plotter2(Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super(Plotter2,self).__init__(*args,**kwargs)
        self.selected=None
        return

    def setupUi(self,MainWindow):
        super(Plotter2,self).setupUi(MainWindow)    
        ##############################
        # Setup actions of the menus #
        ##############################
        self.actionUndo.triggered.connect(self.undo_function)
        self.actionSet_Template.triggered.connect(self.set_template)

        ###################################
        # Setup COnections of the toolbar #
        ###################################

        self.undo.clicked.connect(self.undo_function)

        # #######################
        # # Setup the tree view #
        # #######################

        # # model=QtGui.QDirModel()
        # model=QtGui.QFileSystemModel()
        # model.setRootPath("/homde/hadrian")
        # self.treedir.setModel(model)
        # self.treedir.setRootIndex(model.index("/hadrian/home/Documentos"))
        # self.treedir.expand(model.index("/hadrian/home/Documentos"))

        ################
        # Setup Figure #
        ################
        color=self.centralwidget.palette().color(QtGui.QPalette.Background)
        color=str(color.name())
        figure=extended_figure(facecolor=color)
        self.figure=figure
        figure.blank_figure()
        self.canvas=FigureCanvas(figure)
        self.layout_3.addWidget(self.canvas,0,0)
        figure.canvas.callbacks.connect("button_press_event", self.select_ax)

        ##########################################
        # Setup DoubleSpinbox of the axis limits #
        ##########################################

        self.xmin_val.valueChanged.connect(self.update_limits)
        self.xmax_val.valueChanged.connect(self.update_limits)
        self.ymin_val.valueChanged.connect(self.update_limits)
        self.ymax_val.valueChanged.connect(self.update_limits)
        self.xmin_val.setValue(0)
        self.xmax_val.setValue(1)
        self.ymin_val.setValue(0)
        self.ymax_val.setValue(1)

        ############################
        # Setup Buttons for scales #
        ############################

        self.decimal_but.clicked.connect(self.decimal_scale)
        self.semilogx_but.clicked.connect(self.semilogx_scale)
        self.semilogy_but.clicked.connect(self.semilogy_scale)
        self.loglog_but.clicked.connect(self.loglog_scale)

        ##########################
        # Disable items on start #
        ##########################

        self.itemStatus(False)

        self.bocDiffColor.stateChanged.connect(self.marker_color_policy)

    def undo_function(self):
        self.error_dialog_axis()
        print("Hola")

    def set_template(self):
        # This function should invoke a new dialog to
        # define the template, now it just set the
        # same template
        self.figure.define_template(matrix=[[1,1,3],[2,2,3]])
        self.canvas.draw()

    #######################
    # Selection Functions #
    #######################

    def select_ax(self,event):
        if event.inaxes is not None:
            index=self.figure.index_dict[event.inaxes]
            if self.selected and self.selected!=index:
                self.unremark_axis(self.selected)
            self.selected=index
            self.remark_axis(index)
        else:
            if self.selected:
                self.unremark_axis(self.selected)
            self.selected=None
        self.itemStatus(bool(self.selected))
        self.canvas.draw()

    def remark_axis(self,index):
        ax=self.figure.axes_dict[index]
        ax.spines["bottom"].set_color("red")
        ax.spines["top"].set_color("red")
        ax.spines["right"].set_color("red")
        ax.spines["left"].set_color("red")
        self.update_limits_indicators(index)

    def unremark_axis(self,index):
        ax=self.figure.axes_dict[index]
        ax.spines["bottom"].set_color("black")
        ax.spines["top"].set_color("black")
        ax.spines["right"].set_color("black")
        ax.spines["left"].set_color("black")

    ################################
    # Porperties of Axes Functions #
    ################################

    def update_limits_indicators(self,index):
        plot=self.figure.axes_dict[index]
        xmin,xmax=plot.get_xlim()
        ymin,ymax=plot.get_ylim()
        self.xmin_val.setValue(xmin)
        self.xmax_val.setValue(xmax)
        self.ymin_val.setValue(ymin)
        self.ymax_val.setValue(ymax)

    def update_limits(self):
        if not self.selected:
            return
        plot=self.figure.axes_dict[self.selected]
        xmax=self.xmax_val.value()
        xmin=self.xmin_val.value()
        ymax=self.ymax_val.value()
        ymin=self.ymin_val.value()
        plot.set_xlim((xmin,xmax))
        plot.set_ylim((ymin,ymax))
        self.canvas.draw()

    def decimal_scale(self):
        plot=self.figure.axes_dict[self.selected]
        plot.set_xscale("linear")
        plot.set_yscale("linear")
        self.canvas.draw()

    def semilogx_scale(self):
        plot=self.figure.axes_dict[self.selected]
        xmin,xmax=plot.get_xlim()
        if min(xmin,xmax)<=0:
            self.error_dialog_axis("x")
        else:
            plot.set_xscale("log")
            plot.set_yscale("linear")
            self.canvas.draw()

    def semilogy_scale(self):
        plot=self.figure.axes_dict[self.selected]
        xmin,xmax=plot.get_ylim()
        if min(xmin,xmax)<=0:
            self.error_dialog_axis("y")
        else:
            plot.set_yscale("log")
            plot.set_xscale("linear")
            self.canvas.draw()

    def loglog_scale(self):
        plot=self.figure.axes_dict[self.selected]
        xmin,xmax=plot.get_xlim()
        ymin,ymax=plot.get_ylim()
        if min(xmin,xmax)<=0:
            self.error_dialog_axis("x")

        elif min(ymin,ymax)<=0:
            self.error_dialog_axis("y")

        else:
            plot.set_yscale("log")
            plot.set_xscale("log")
            self.canvas.draw()

    def error_dialog_axis(self,axis="x"):
        error_message=QtGui.QMessageBox()
        error_message.setIcon(QtGui.QMessageBox.Warning)
        error_message.setText("A value of 0 or negative was found when "+
                              "calculating logarithm in the "+axis+" axis.\n"+
                              "Please check plot boundaries and try again")
        error_message.exec_()

    #############################################
    # Methods to activate and desactivate items #
    #############################################

    def itemStatus(self,state):

        ##########################
        # Disable the axe limits #
        ##########################

        self.xmax_val.setEnabled(state)
        self.xmin_val.setEnabled(state)
        self.ymax_val.setEnabled(state)
        self.ymin_val.setEnabled(state)

        #####################
        # Disable Axe scale #
        #####################

        self.decimal_but.setEnabled(state)
        self.semilogx_but.setEnabled(state)
        self.semilogy_but.setEnabled(state)
        self.loglog_but.setEnabled(state)

        #####################
        # Disable path file #
        #####################

        self.file_path_box.setEnabled(state)
        self.file_path_open.setEnabled(state)

        #######################
        # Disable file column #
        #######################

        self.xcolumn_index.setEnabled(state)
        self.y_column_index.setEnabled(state)

        ######################
        # Disable properties #
        ######################

        self.comboColor.setEnabled(state)
        self.comboLinestyle.setEnabled(state)
        self.comboMarker.setEnabled(state)
        self.comboMarkerColor.setEnabled(state)
        self.bocDiffColor.setEnabled(state)

        ####################################
        # Set the state of the markercolor #
        ####################################
        if state:
            self.marker_color_policy()

    def marker_color_policy(self):

        state=self.bocDiffColor.isChecked()
        self.comboMarkerColor.setEnabled(state)

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Plotter2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
