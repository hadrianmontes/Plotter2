from ui.mainwindow import Ui_MainWindow
from options_dialog import PreferencesDialog
from PyQt4 import QtGui, QtCore
from extended_figure import extended_figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from template_gepmetry import TemplateDialog
import os
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class Plotter2(Ui_MainWindow):
    """
    This class defines the behaviour of the ui of the mainwindow
    """
    def __init__(self,*args,**kwargs):
        super(Plotter2,self).__init__(*args,**kwargs)
        self.selected=None
        self.savepath=None
        self.currentpath=os.getcwd()
        return

    def setupUi(self,MainWindow):
        super(Plotter2,self).setupUi(MainWindow)
        ##############################
        # Setup actions of the menus #
        ##############################
        self.actionUndo.triggered.connect(self.undo_function)
        self.actionRedo.triggered.connect(self.redo_function)
        self.actionExport.triggered.connect(self.export_fun)
        self.actionSave.triggered.connect(self.savefun)
        self.actionSave_as.triggered.connect(self.saveasfun)
        self.actionOpen.triggered.connect(self.loadfun)
        self.actionPreferences.triggered.connect(self.change_preferences)
        # self.actionSet_Template.triggered.connect(self.set_template)

        ###################################
        # Setup COnections of the toolbar #
        ###################################

        self.undo.clicked.connect(self.undo_function)
        self.save.clicked.connect(self.savefun)
        self.open.clicked.connect(self.loadfun)
        self.redo.clicked.connect(self.redo_function)
        self.export_2.clicked.connect(self.export_fun)

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

        ################################
        # Setup connections for figure #
        ################################

        self.set_template_but.clicked.connect(self.set_template)
        self.joinx_but.clicked.connect(self.joinx)
        self.joiny_but.clicked.connect(self.joiny)
        self.joinxy_but.clicked.connect(self.joinxy)
        self.optimize_space_but.clicked.connect(self.optimize_space)
        self.advanced_template_but.clicked.connect(self.set_advanced_template)

        ##########################################
        # Setup DoubleSpinbox of the axis limits #
        ##########################################

        self.xmin_val.valueChanged.connect(self.update_min_xlim)
        self.xmax_val.valueChanged.connect(self.update_max_xlim)
        self.ymin_val.valueChanged.connect(self.update_min_ylim)
        self.ymax_val.valueChanged.connect(self.update_max_ylim)
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

        ############################
        # Setup Signals for labels #
        ############################

        self.setlabels_but.clicked.connect(self.set_labels)
        self.showlegend.stateChanged.connect(self.update_legend)

        ###########################################
        # Setup Signals for position/ticks radios #
        ###########################################

        self.top_pos_radio.pressed.connect(self.top_pressed)
        self.bottom_pos_radio.pressed.connect(self.bottom_pressed)
        self.left_pos_radio.pressed.connect(self.left_pressed)
        self.right_pos_radio.pressed.connect(self.right_pressed)

        ##############################
        ##############################
        # Setup Buttons for plotting #

        self.file_path_open.clicked.connect(self.select_path)
        self.bocDiffColor.stateChanged.connect(self.marker_color_policy)
        self.plot_but.clicked.connect(self.plot_file)

        ##########################
        # Disable items on start #
        ##########################

        self.itemStatus(False)

    def undo_function(self):
        self.figure.undo()
        self.canvas.draw()
        self.updateUndoRedoButtons()
        self.update_legend()

    def redo_function(self):
        self.figure.redo()
        self.canvas.draw()
        self.update_legend()
        self.updateUndoRedoButtons()

    def set_template(self):
        self.selected=None
        self.clear_figure()
        ncol=self.ncol_template.value()
        nrow=self.nrow_template.value()
        self.figure.define_template(size=(nrow,ncol))
        self.canvas.draw()
        self.select_ax_manual(1)

    def change_preferences(self):
        dialog=QtGui.QDialog()
        dialog.ui=PreferencesDialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def set_advanced_template(self):
        dialog=QtGui.QDialog()
        dialog.ui=TemplateDialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        if dialog.exec_():
            self.selected=None
            # Only executed the code if the Dialog exits with
            # the accept buttons
            self.clear_figure()
            minimum=dialog.ui.matrix[0][0]
            for row in dialog.ui.matrix:
                for element in row:
                    minimum=min(minimum,element)
            self.figure.define_template(matrix=dialog.ui.matrix)
            self.disable_join_buttons()
            self.select_ax_manual(minimum)
            self.canvas.draw()

    ####################
    # Figure Functions #
    ####################

    def joinx(self):
        self.figure.join_x()
        self.canvas.draw()

    def joiny(self):
        self.figure.join_y()
        self.canvas.draw()

    def joinxy(self):
        self.figure.join_xy()
        self.canvas.draw()

    def optimize_space(self):
        self.figure.reset_ticks()
        self.figure.tight_layout()
        self.canvas.draw()

    def clear_figure(self):
        self.figure.clear()

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

    def select_ax_manual(self,index):
        if self.selected and self.selected!=index:
            self.unremark_axis(self.selected)
        self.selected=index
        if index:
            self.remark_axis(index)
        self.itemStatus(bool(self.selected))
        self.canvas.draw()

    def remark_axis(self,index):
        ax=self.figure.axes_dict[index]
        ax.spines["bottom"].set_color("red")
        ax.spines["top"].set_color("red")
        ax.spines["right"].set_color("red")
        ax.spines["left"].set_color("red")
        self.update_limits_indicators(index)
        self.update_legend_info(index)
        self.update_labels_box()

    def unremark_axis(self,index):
        ax=self.figure.axes_dict[index]
        ax.spines["bottom"].set_color("black")
        ax.spines["top"].set_color("black")
        ax.spines["right"].set_color("black")
        ax.spines["left"].set_color("black")

    ################################
    # Porperties of Axes Functions #
    ################################

    def update_labels_box(self):
        plot=self.figure.axes_dict[self.selected]
        xlabel=plot.get_xlabel()
        ylabel=plot.get_ylabel()
        self.xlabel_box.setText(xlabel)
        self.ylabel_box.setText(ylabel)

    def set_labels(self):
        plot=self.figure.axes_dict[self.selected]
        xlabel=str(self.xlabel_box.text())
        ylabel=str(self.ylabel_box.text())
        plot.set_xlabel(xlabel)
        plot.set_ylabel(ylabel)
        self.canvas.draw()

    def update_limits_indicators(self,index):
        plot=self.figure.axes_dict[index]
        xmin,xmax=plot.get_xlim()
        ymin,ymax=plot.get_ylim()
        self.xmin_val.setValue(xmin)
        self.xmax_val.setValue(xmax)
        self.ymin_val.setValue(ymin)
        self.ymax_val.setValue(ymax)

    def update_limits(self):
        # Deprecated function, it have some bugs
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

    def update_min_xlim(self):
        if not self.selected:
            return
        plot=self.figure.axes_dict[self.selected]
        xmin=self.xmin_val.value()
        xmin2=plot.get_xlim()[0]
        if xmin!=xmin2:
            xmax=self.xmax_val.value()
            plot.set_xlim((xmin,xmax))
            self.canvas.draw()
        else:
            return

    def update_max_xlim(self):
        if not self.selected:
            return
        plot=self.figure.axes_dict[self.selected]
        xmax=self.xmax_val.value()
        xmax2=plot.get_xlim()[1]
        if xmax!=xmax2:
            xmin=self.xmin_val.value()
            plot.set_xlim((xmin,xmax))
            self.canvas.draw()
        else:
            return

    def update_min_ylim(self):
        if not self.selected:
            return
        plot=self.figure.axes_dict[self.selected]
        ymin=self.ymin_val.value()
        ymin2=plot.get_ylim()[0]
        if ymin!=ymin2:
            ymax=self.ymax_val.value()
            plot.set_ylim((ymin,ymax))
            self.canvas.draw()
        else:
            return

    def update_max_ylim(self):
        if not self.selected:
            return
        plot=self.figure.axes_dict[self.selected]
        ymax=self.ymax_val.value()
        ymax2=plot.get_ylim()[1]
        if ymax!=ymax2:
            ymin=self.ymin_val.value()
            plot.set_ylim((ymin,ymax))
            self.canvas.draw()
        else:
            return

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

    def update_legend(self):
        plot=self.figure.axes_dict[self.selected]
        legend=plot.legend()
        state=self.showlegend.isChecked()
        self.figure.legend_status[self.selected]=state
        if legend is None:
            return
        legend.set_visible(state)
        self.canvas.draw()
        return

    def update_legend_info(self,index):
        state=self.figure.legend_status[index]
        self.showlegend.setChecked(state)

    def error_dialog_axis(self,axis="x"):
        error_message=QtGui.QMessageBox()
        error_message.setIcon(QtGui.QMessageBox.Warning)
        error_message.setText("A value of 0 or negative was found when "+
                              "calculating logarithm in the "+axis+" axis.\n"+
                              "Please check plot boundaries and try again")
        error_message.exec_()

    def top_pressed(self):
        plot=self.figure.axes_dict[self.selected]
        plot.xaxis.tick_top()
        plot.xaxis.set_ticks_position("both")
        plot.xaxis.set_label_position("top")
        self.optimize_space()
        self.canvas.draw()

    def bottom_pressed(self):
        plot=self.figure.axes_dict[self.selected]
        plot.xaxis.tick_bottom()
        plot.xaxis.set_ticks_position("both")
        plot.xaxis.set_label_position("bottom")
        self.optimize_space()
        self.canvas.draw()

    def right_pressed(self):
        plot=self.figure.axes_dict[self.selected]
        plot.yaxis.tick_right()
        plot.yaxis.set_ticks_position("both")
        plot.yaxis.set_label_position("right")
        self.optimize_space()
        self.canvas.draw()

    def left_pressed(self):
        plot=self.figure.axes_dict[self.selected]
        plot.yaxis.tick_left()
        plot.yaxis.set_ticks_position("both")
        plot.yaxis.set_label_position("left")
        self.optimize_space()
        self.canvas.draw()

    ###########################
    # Plotting File Functions #
    ###########################

    def select_path(self):

        text=str(QtGui.QFileDialog.getOpenFileName(directory=self.currentpath))
        if text:
            self.currentpath=os.path.dirname(text)
        self.file_path_box.setText(text)

    def plot_file(self):
        plot_parameters=self.export_properties()
        xcolumn=self.xcolumn_index.value()
        ycolumn=self.y_column_index.value()
        path=str(self.file_path_box.text())
        index=self.selected
        self.figure.plot_file(path,index,xcol=xcolumn,ycol=ycolumn,**plot_parameters)
        self.update_legend()
        self.canvas.draw()
        self.update_limits_indicators(self.selected)
        self.update_labels_box()
        self.updateUndoRedoButtons()

    def export_properties(self):
        """Search for the properties set in the window and
        export them for their use in kwargs"""

        properties=dict()

        # Search for label

        label=str(self.plotlabel_box.text())
        properties["label"]=label

        # Search for the linestyle
        # Linestyle in the combo is set as:
        # explicative text "linestyle"
        # doinf split('"')[-2] will return the linestyle
        linestyle=str(self.comboLinestyle.currentText())
        if linestyle!="None":
            linestyle=linestyle.split('"')[-2]
        properties["linestyle"]=linestyle

        # Search for the marker
        marker_raw=str(self.comboMarker.currentText())
        if marker_raw!="None":
            # If it is not None the formating is the same as in linestyle
            marker_raw=marker_raw.split('"')[-2]
        properties["marker"]=marker_raw

        # Search for the color

        color=str(self.comboColor.currentText()).lower()
        if color!="auto":
            properties["color"]=color

        # If a different color is selected for the marker export it

        if self.bocDiffColor.isChecked():
            color=str(self.comboMarkerColor.currentText()).lower()
            properties["markerfacecolor"]=color
            properties["markeredgecolor"] =str(self.comboEdgeColor.currentText()).lower()

        return properties

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

        #######################
        # Disable axes labels #
        #######################

        self.xlabel_box.setEnabled(state)
        self.ylabel_box.setEnabled(state)
        self.setlabels_but.setEnabled(state)

        ###################################
        # Disable the radio for positions #
        ###################################
        self.left_pos_radio.setEnabled(state)
        self.right_pos_radio.setEnabled(state)
        self.top_pos_radio.setEnabled(state)
        self.bottom_pos_radio.setEnabled(state)

        #########################
        # Disable legend things #
        #########################

        self.showlegend.setEnabled(state)

        #####################
        # Disable path file #
        #####################

        self.file_path_box.setEnabled(state)
        self.file_path_open.setEnabled(state)

        ######################
        # Disable plot label #
        ######################

        self.plotlabel_box.setEnabled(state)

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
        self.comboEdgeColor.setEnabled(state)
        self.bocDiffColor.setEnabled(state)

        #######################
        # Disable button plot #
        #######################

        self.plot_but.setEnabled(state)

        ####################################
        # Set the state of the markercolor #
        ####################################
        if state:
            self.marker_color_policy()

        ###################################################
        # Check the correct state for the redoing buttons #
        ###################################################

        self.updateUndoRedoButtons()

    def disable_join_buttons(self):
        status_y=self.figure.template.yjoinable
        status_x=self.figure.template.xjoinable
        status_xy=(status_x and status_y)
        self.joinx_but.setEnabled(status_x)
        self.joiny_but.setEnabled(status_y)
        self.joinxy_but.setEnabled(status_xy)

    def updateUndoRedoButtons(self):
        state_undo=self.figure.canUndo()
        self.actionUndo.setEnabled(state_undo)
        self.undo.setEnabled(state_undo)
        state_redo=self.figure.canRedo()
        self.actionRedo.setEnabled(state_redo)
        self.redo.setEnabled(state_redo)

    def marker_color_policy(self):

        state=self.bocDiffColor.isChecked()
        self.comboMarkerColor.setEnabled(state)
        self.comboEdgeColor.setEnabled(state)

    ###########################
    # Import/Export functions #
    ###########################

    def export_fun(self):
        text=str(QtGui.QFileDialog.getSaveFileName(filter="Portable Document File (*.pdf)"+
                                                   ";;Portable Network Graphics (*.png)"+
                                                   ";;Encapsulated Postscript (*.eps)"+
                                                   ";;All Files (*)",
                                                   directory=self.currentpath,
                                                   options=QtGui.QFileDialog.DontUseNativeDialog))
        if text=="":
            return

        self.currentpath=os.path.dirname(text)
        
        if self.selected:
            self.unremark_axis(self.selected)
        self.figure.savefig(text)
        if self.selected:
            self.remark_axis(self.selected)
            self.canvas.draw()

    def savefun(self):
        # Check if there is an existing save path or not
        # if not it creates a dialog to select it
        if self.savepath is None:
            self.saveasfun()
        else:
            self.saveinfile()

    def saveinfile(self):
        self.figure.save(self.savepath)

    def saveasfun(self):
        text=str(QtGui.QFileDialog.getSaveFileName(filter="Plotter2 savefiles (*.plt2);;All Files (*)",
                                                   directory=self.currentpath,
                                                   options=QtGui.QFileDialog.DontUseNativeDialog))
        if text=="":
            return
        else:
            self.savepath=text
            self.currentpath=os.path.dirname(text)
            self.saveinfile()

    def loadfun(self):
        text=str(QtGui.QFileDialog.getOpenFileName(filter="Plotter2 savefiles (*.plt2);;All Files (*)",
                                                   directory=self.currentpath,
                                                   options=QtGui.QFileDialog.DontUseNativeDialog))
        if text=="":
            return
        else:
            self.figure.load(text)
            self.currentpath=os.path.dirname(text)
            self.savepath=text
        for row in self.figure.template.matrix:
            for item in row:
                self.selected=item
                self.update_limits_indicators(item)
                self.update_legend()
                self.canvas.draw()

        self.update_labels_box()
        self.updateUndoRedoButtons()
        self.optimize_space()

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Plotter2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
