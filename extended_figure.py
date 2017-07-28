import matplotlib.pyplot as plt
from axes_template import axes_template
from plot_manager import Plot_Manager

def extended_figure(*args,**kwargs):
    kwargs["FigureClass"]=Extended_Figure
    return plt.figure(*args,**kwargs)

class Extended_Figure(plt.Figure):
    '''
    Creates a figure to plot data in multiple axes
    comming from files or from objects with the correct format
    '''
    def __init__(self,*args,**kwargs):
        super(Extended_Figure,self).__init__(*args,**kwargs)
        self.ncol=1
        self.nrow=1
        self.manager=Plot_Manager(self)

    def blank_figure(self):
        """
        Creates a blank figure
        """
        self.define_template(matrix=[[1]])
        ax=self.axes_dict[1]
        ax.set_xticks([])
        ax.set_yticks([])
        self.tight_layout()

    def define_template(self,**kwargs):
        '''
        Defines the number of rows and colums
        for the subplots. It is possible also to define a custom grid
        that will include the columspans.
        '''
        self.template=axes_template(**kwargs)
        self.ncol=self.template.ncol
        self.nrow=self.template.nrow
        self.axes_dict=self.template.apply_template(self)
        self.manager=Plot_Manager(self)
        self.index_dict=dict()
        self.legend_status=dict()
        for index in self.axes_dict:
            self.index_dict[self.axes_dict[index]]=index
            self.legend_status[index]=True

    def view_template(self):
        """
        It generates a figure with the template and numbers
        that identify each axis
        """
        self.template.generate_preview()

    def plot(self,index,*args,**kwargs):
        """
        PLots the data in a given subplot.

        Parameters
        ----------
        index: int
            Index of the subplot where the data will be plotted
        *args: Any argument for matplotlib.axis.plot
        **kwargs: Any keywordargument for matplotlib.axis.plot.
            Moreover, the arguents xcol and ycol are accepted to set
            in the plot manager from wich column was the x and y data
            read.
        """
        xcol=None
        ycol=None
        string=None
        if "xcol" in kwargs:
            xcol=kwargs.pop("xcol")
        if "ycol" in kwargs:
            ycol=kwargs.pop("ycol")
        if "string" in kwargs:
            string=kwargs.pop("string")
        plot_label=""
        if "plot_label" in kwargs:
            plot_label=kwargs.pop("plot_label")
        if index in self.axes_dict:
            plot=self.axes_dict[index].plot(*args,**kwargs)[0]
            self.manager.add_plot(index, plot, kwargs, path=plot_label,
                                  xcol=xcol, ycol=ycol, string=string)
        else:
            raise KeyError("This value for the axis is not defined")
            return


    def errorbar(self,index,*args,**kwargs):
        """
        PLots the data in a given subplot.

        Parameters
        ----------
        index: int
            Index of the subplot where the data will be plotted
        *args: Any argument for matplotlib.axis.plot
        **kwargs: Any keywordargument for matplotlib.axis.plot.
            Moreover, the arguents xcol and ycol are accepted to set
            in the plot manager from wich column was the x and y data
            read.
        """
        xcol=None
        ycol=None
        yerrcol=None
        string=None
        if "xcol" in kwargs:
            xcol=kwargs.pop("xcol")
        if "ycol" in kwargs:
            ycol=kwargs.pop("ycol")
        if "yerrcol" in kwargs:
            yerrcol=kwargs.pop("yerrcol")
        if "string" in kwargs:
            string=kwargs.pop("string")
        plot_label=""
        if "plot_label" in kwargs:
            plot_label=kwargs.pop("plot_label")
        if index in self.axes_dict:
            plot=self.axes_dict[index].errorbar(*args,**kwargs)[0]
            self.manager.add_plot(index, plot, kwargs, path=plot_label,
                                  xcol=xcol, ycol=ycol, yerrcol=yerrcol,
                                  string=string, errorbar=True)
        else:
            raise KeyError("This value for the axis is not defined")
            return


    def hist(self,index,*args,**kwargs):
        """
        Histograms the data in a given subplot.

        Parameters
        ----------
        index: int
            Index of the subplot where the data will be plotted
        *args: Any argument for matplotlib.axis.hist
        **kwargs: Any keywordargument for matplotlib.axis.hist.
            Moreover, the arguents xcol and ycol are accepted to set
            in the plot manager from wich column was the x and y data
            read.
        """

        xcol=None
        ycol=None
        if "xcol" in kwargs:
            xcol=kwargs.pop("xcol")
        if "ycol" in kwargs:
            ycol=kwargs.pop("ycol")
        if "plot_label" in kwargs:
            plot_label=kwargs.pop("plot_label")
        if index in self.axes_dict:
            if "width" in kwargs:
                if kwargs["width"]=="auto":
                    lens=[args[0][i]-args[0][i-1] for i in range(1,len(args[0]))]
                    kwargs["width"]=0.8*min(lens)
            self.axes_dict[index].bar(*args,**kwargs)
        else:
            raise KeyError("This value for the axis is not defined")
            return

    def hist_file(self,filename,index,xcol=0,ycol=1,**kwargs):
        if "plot_label" not in kwargs:
            kwargs["plot_label"]=filename
        kwargs["xcol"]=xcol
        kwargs["ycol"]=ycol
        x,y=read_file(filename,xcol,ycol)
        self.hist(index,x,y,**kwargs)

    def errorbar_file(self, filename, index, xcol=0,
                      ycol=1, yerrcol=2, **kwargs):

        if "plot_label" not in kwargs:
            kwargs["plot_label"]=filename
        kwargs["xcol"]=int(xcol)
        kwargs["ycol"]=int(ycol)
        kwargs["yerrcol"]=int(yerrcol)
        x,y, yerr=read_file_errorbar(filename,int(xcol),int(ycol), int(yerrcol))
        # Make a copy to avoid nasty changes in plots
        self.errorbar(index,x,y,yerr=yerr,**kwargs)
        return

    def plot_file(self,filename,index,xcol=0,ycol=1,**kwargs):
        if "plot_label" not in kwargs:
            kwargs["plot_label"]=filename
        kwargs["xcol"]=int(xcol)
        kwargs["ycol"]=int(ycol)
        x,y=read_file(filename,int(xcol),int(ycol))
        # Make a copy to avoid nasty changes in plots
        self.plot(index,x,y,**kwargs)
        return

    def plot_class(self,objeto,index,**kwargs):
        x=objeto.data[0]
        y=objeto.data[1]
        self.plot(index,x,y,**kwargs)

    def update_legend(self,index,state):
        legend=self.axes_dict[index]
        legend.set_visible(state)

    def join_xy(self):
        if not (self.template.xjoinable and self.template.yjoinable):
            print("The tempalte does not allow this kind of joining"+
                  " try with only one kind of axis")
            return
        else:
            self.join_x()
            self.join_y()

    def join_x(self):
        """
        Joins and share the x axis of the subplots 
        of each column
        """
        if not self.template.xjoinable:
            print("This configuration does not support x axis joinability")
            return
        matrix=self.template.matrix

        # Join all the axis in each column
        joined_index=[]
        maximuns = []
        minimuns = []
        for column in range(self.ncol):
            joined_index.append(matrix[-1][column])
            ref_axis=self.axes_dict[matrix[-1][column]]
            maximuns.append(ref_axis.get_xlim()[1])
            minimuns.append(ref_axis.get_xlim()[0])
            for row in range(self.nrow):
                index=matrix[row][column]
                if index not in joined_index:
                    joined_index.append(index)
                    ref_axis.get_shared_x_axes().join(self.axes_dict[index],ref_axis)
                mini,maxi=self.axes_dict[matrix[row][column]].get_xlim()
                maximuns[-1] = max(maximuns[-1],maxi)
                minimuns[-1] = min(minimuns[-1],mini)

        # Change the range of all the subplots
        for column in range(self.ncol):
            self.axes_dict[matrix[-1][column]].set_xlim((minimuns[column],maximuns[column]))
        self.fix_x_ticks()

    def fix_x_ticks(self):
        # Elimnate the xticks of all the subplots that are not
        # at the bottom. It also pops the top element of each
        # set of ticks if they are not in the top subplot
        matrix=self.template.matrix
        adjusted_ticks=[]

        for column in range(self.ncol):
            bottom_index=matrix[-1][column]
            top_index=matrix[-1][column]
            removed_ticks=[]
            for row in range(self.nrow):
                if matrix[row][column]!=bottom_index and matrix[row][column] not in removed_ticks:
                    for tick in self.axes_dict[matrix[row][column]].xaxis.get_major_ticks():
                        tick.label1.set_visible(False)
                    removed_ticks.append(matrix[row][column])
                if matrix[row][column]!=top_index and matrix[row][column] not in adjusted_ticks:
                    ticks=self.axes_dict[matrix[row][column]].yaxis.get_major_ticks()
                    ticks[0].set_visible(False)
                    adjusted_ticks.append(matrix[row][column])
        self.subplots_adjust(hspace=0)

    def join_y(self):
        """
        Joins and share the y axis of the subplots
        of each column
        """
        if not self.template.yjoinable:
            print("This configuration does not support y axis joinability")
            return
        matrix=self.template.matrix

        # Join all the axis in each row
        joined_index=[]
        maximuns = []
        minimuns = []
        for row in range(self.nrow):
            joined_index.append(matrix[row][0])
            ref_axis=self.axes_dict[matrix[row][0]]
            maximuns.append(ref_axis.get_ylim()[1])
            minimuns.append(ref_axis.get_ylim()[0])
            for column in range(self.ncol):
                index=matrix[row][column]
                if index not in joined_index:
                    joined_index.append(index)
                    ref_axis.get_shared_y_axes().join(self.axes_dict[index],ref_axis)
                mini,maxi=self.axes_dict[matrix[row][column]].get_ylim()
                maximuns[-1] = max(maximuns[-1],maxi)
                minimuns[-1] = min(minimuns[-1],mini)

        # Change the range of all the subplots
        for column in range(self.nrow):
            self.axes_dict[matrix[column][-1]].set_ylim((minimuns[column],maximuns[column]))
        self.fix_y_ticks()

    def fix_y_ticks(self):
        # Elimnate the xticks of all the subplots that are not
        # at the bottom. It also pops the top element of each
        # set of ticks if they are not in the top subplot
        adjusted_ticks=[]
        matrix=self.template.matrix

        for row in range(self.nrow):
            bottom_index=matrix[row][0]
            top_index=matrix[row][-1]
            removed_ticks=[]
            for column in range(self.ncol):
                if matrix[row][column]!=bottom_index and matrix[row][column] not in removed_ticks:
                    for tick in self.axes_dict[matrix[row][column]].yaxis.get_major_ticks():
                        tick.label1.set_visible(False)
                    removed_ticks.append(matrix[row][column])
                if matrix[row][column]!=top_index and matrix[row][column] not in adjusted_ticks:
                    ticks=self.axes_dict[matrix[row][column]].xaxis.get_major_ticks()
                    ticks[-1].set_visible(False)
                    adjusted_ticks.append(matrix[row][column])
        self.subplots_adjust(wspace=0)

    def undo(self):
        self.manager.undo()

    def redo(self):
        self.manager.redo()

    def canUndo(self):
        return self.manager.canUndo()

    def canRedo(self):
        return self.manager.canRedo()

    def reset_ticks(self):
        """
        Makes visisible all the ticks, this can be used if there are
        hidden ticks that should ve visible
        """
        matrix = self.template.matrix
        for column in range(self.ncol):
            for row in range(self.nrow):
                axes = self.axes_dict[matrix[row][column]]
                x_ticks = axes.xaxis.get_major_ticks()
                for tick in x_ticks:
                    tick.set_visible(True)
                    tick.label1.set_visible(True)
                y_ticks = axes.yaxis.get_major_ticks()
                for tick in y_ticks:
                    tick.set_visible(True)
                    tick.label1.set_visible(True)

    ###########################
    # Lading saving functions #
    ###########################

    def save(self,path):
        self.manager.save(path)

    def load(self,path):
        return self.manager.load(path)

def read_file(filename,xcol=0,ycol=1):
    f=open(filename,"Ur")
    x=[]
    y=[]
    for l in f:
        if l.startswith("#"):
            pass
        elif l.startswith(r"@"):
            pass
        else:
            try:
                xval=float(l.split()[xcol])
                yval=float(l.split()[ycol])
                x.append(xval)
                y.append(yval)
            except:
                pass
    return x,y

def read_file_errorbar(filename, xcol=0, ycol=1, yerrcol=2):
    f=open(filename,"Ur")
    x=[]
    y=[]
    yerr=[]
    for l in f:
        if l.startswith("#"):
            pass
        elif l.startswith(r"@"):
            pass
        else:
            try:
                xval=float(l.split()[xcol])
                yval=float(l.split()[ycol])
                yerrval=float(l.split()[yerrcol])
                x.append(xval)
                y.append(yval)
                yerr.append(yerrval)
            except:
                pass
    return x,y, yerr
