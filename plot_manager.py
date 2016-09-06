class Plot_Manager():
    """This class implements a manager to manage existing
    plots with operations such as removing plots, editing existing
    or reverting last change"""

    def __init__(self,parent):
        self.parent=parent
        self.uid=0
        self.plot_by_uid=dict()
        self.uid_by_name=dict()
        self.changes=[]
        self.unchanges=[]
        self.indexes=[]

    def add_plot(self,index,plot,properties,string=None,path=None,xcol=None,ycol=None):
        if string is None:
            string="Unnamed plot "+str(self.uid)
        elif string in self.uid_by_name:
            copy=2
            while string+"("+str(copy)+")" in self.uid_by_name:
                copy+=1
            else:
                string=string+"("+str(copy)+")"

        # save the color in the porperties
        # wether it was lready saved or not
        properties["color"]=plot.get_color()

        self.plot_by_uid[self.uid]={"string":string,"plot":plot,"deleted":False,"index":index,"properties":properties}

        # Save info about columns if existing
        if xcol is not None and ycol is not None:
            self.plot_by_uid[self.uid]["xcol"]=xcol
            self.plot_by_uid[self.uid]["ycol"]=ycol

        if index not in self.indexes:
            self.indexes.append(index)

        if path:
            self.plot_by_uid[self.uid]["path"]=path
        self.uid_by_name[string]=self.uid
        self.changes.append(Change(1,plot))
        self.unchanges=[]
        self.uid+=1

    def delete_plot(self,name):
        plot=self[name]
        plot.set_visible("False")
        self.changes.append(Change(-1,plot))
        self.unchanges=[]

    def edit_plot(self,name,list_changes):
        for change in list_changes:
            key_val="set_"+change[0]
            eval("plot."+key_val+"("+change[2]+")")
        self.unchanges=[]
        return

    def undo(self):
        if len(self.changes)==0:
            return
        last_change=self.changes.pop()
        last_change.undo()
        self.unchanges.append(last_change)
        return

    def canUndo(self):
        return bool(len(self.changes))

    def canRedo(self):
        return bool(len(self.unchanges))

    def redo(self):
        if len(self.unchanges)==0:
            return
        unchange=self.unchanges.pop()
        unchange.redo()
        self.changes.append(unchange)

    def __getitem__(self,name):
        uid=self.uid_by_name[name]
        plot=self.plot_by_uid[uid]["plot"]
        return plot

    ################################
    # Loading and saving functions #
    ################################

    def save(self,filename):
        f=open(filename,"w")
        # First get the current template
        f.write("Template:\n")
        template=self.parent.template.matrix
        for row in template:
            for item in row:
                f.write("\t")
                f.write(str(item))
            f.write("\n")
        f.write("End Template\n")

        # Start writting the info of the plots
        for index in self.indexes:
            f.write("Index: ")
            f.write(str(index))
            f.write("\n")
            self.write_axis_info(index,f)
            for uid in self.plot_by_uid:
                plot=self.plot_by_uid[uid]
                if plot["index"]==index:
                    self.write_info(uid,plot,f)

        f.close()
        return

    def write_axis_info(self,index,filebuffer):
        axis=self.parent.axes_dict[index]
        filebuffer.write("xlimit ")
        xmin,xmax=axis.get_xlim()
        filebuffer.write(str(xmin)+" "+str(xmax)+"\n")

        filebuffer.write("ylimit ")
        ymin,ymax=axis.get_ylim()
        filebuffer.write(str(ymin)+" "+str(ymax)+"\n")

        xlabel=axis.get_xlabel()
        filebuffer.write("xlabel "+xlabel+"\n")

        ylabel=axis.get_ylabel()
        filebuffer.write("ylabel "+ylabel+"\n")

        label_visible=self.parent.legend_status[index]
        filebuffer.write("label_visible "+str(label_visible)+"\n")

        filebuffer.write("End Axis\n")

    def write_info(self,uid,plot,filebuffer):
        if "path" not in plot:
            print("Found a non savable plot")
            return
        if not plot["plot"].get_visible():
            return
        filebuffer.write("\tPlot: "+str(uid)+"\n")

        # Write the path
        path=str(plot["path"])
        filebuffer.write("\t\tPath "+path+"\n")

        # Write its string
        string=str(plot["string"])
        filebuffer.write("\t\tstring "+string+"\n")

        # Write the columns
        if "xcol" in plot:
            filebuffer.write("\t\txcol "+str(plot["xcol"])+"\n")
            filebuffer.write("\t\tycol "+str(plot["ycol"])+"\n")


        # Write their properties

        for option in plot["properties"]:
            formated=plot["properties"][option]
            filebuffer.write("\t\t"+option+" "+formated+"\n")

        filebuffer.write("End Plot\n")
        return

    def load(self,filename):
        template_loaded=False
        f=open(filename,"r")
        index=None
        for l in f:
            l=l.strip()
            # Start different functions depending on keywords
            if l=="Template:":
                template_loaded=self.load_template(f)
            if l.startswith("Index:"):
                if not template_loaded:
                    print ("Template must be defined at the begining")
                    return
                index=int(l.split()[1])
                self.load_axis(f,index)
            if l.startswith("Plot"):
                self.load_plot(index,f)
        return index

    def load_plot(self, index, filebuffer):
        path=""
        string=None
        options=dict()
        for l in filebuffer:
            l=l.strip()
            if l=="":
                continue
            elif l=="End Plot":
                break
            option=l.split()[0].lower()
            if option!="path":
                value=l[len(option)+1:]
                options[option]=value
            else:
                path=l[len(option)+1:]
        self.parent.plot_file(path,index,**options)

    def load_axis(self,filebuffer,index):
        xlabel=""
        ylabel=""
        xlimit=[0,1]
        ylimit=[0,1]
        visible=True
        for l in filebuffer:
            l=l.strip()
            if l==("End Axis"):
                break
            elif l.startswith("xlimit"):
                xlimit=[float(i) for i in l.split()[1:]]
            elif l.startswith("ylimit"):
                ylimit=[float(i) for i in l.split()[1:]]
            elif l.startswith("xlabel"):
                if len(l)!=len("xlabel"):
                    xlabel=l[len("xlabel"+1):]
            elif l.startswith("ylabel"):
                if len(l)!=len("ylabel"):
                    ylabel=l[len("xlabel"+1):]
            elif l.startswith("label_visible"):
                if l.split()[1].lower()=="false":
                    visible=False
            
        axis=self.parent.axes_dict[index]
        axis.set_xlim(xlimit)
        axis.set_ylim(ylimit)
        axis.set_xlabel(xlabel)
        axis.set_ylabel(ylabel)
        self.parent.legend_status[index]=visible
        return

    def load_template(self, filebuffer):
        template=[]
        # Reads until end is reached
        for l in filebuffer:
            l=l.strip()
            if l=="End Template":
                break
            elif l=="":
                pass
            else:
                newline=[int(i) for i in l.split()]
                template.append(newline)

        if template!=[]:
            self.parent.define_template(matrix=template)
            return True
        else:
            return False
    


            
            

class Change():
    def __init__(self,kind,plot,list_changes=None):
        # each element of list_changes must have the next formating
        # [keyword,previous_value,new_value]
        self.undo_functions=[self.undo_edit,self.undo_add,self.undo_delete]
        self.redo_functions=[self.redo_edit,self.redo_add,self.redo_delete]
        self.add_functions=[self.edit,self.add,self.delete]
        # Kind -1 means plot deleted
        # 0 means plot edited
        # 1 means new plot
        self.kind=kind
        self.plot=plot
        self.add_functions[kind](list_changes)

    def add(self,list_changes):
        current_label=self.plot.get_label()
        self.list_changes=[["label","",current_label]]

    def delete(self,list_changes):
        current_label=self.plot.get_label()
        self.list_changes=[["label",current_label,""]]

    def edit(self,list_changes):
        self.list_changes=list_changes

    def undo(self):
        self.undo_functions[self.kind]()

    def redo(self):
        self.redo_functions[self.kind]()

    def undo_add(self):
        self.plot.set_visible(False)
        self.undo_edit()
        return

    def redo_add(self):
        self.plot.set_visible(True)
        self.redo_edit()
        return

    def undo_delete(self):
        self.plot.set_visible(True)
        self.undo_edit()
        return

    def redo_delete(self):
        self.plot.set_visible(False)
        self.redo_edit()

    def undo_edit(self):
        for change in self.list_changes:
            key_val="set_"+change[0]
            function=eval("self.plot."+key_val)
            function(change[1])
        return

    def redo_edit(self):
        for change in self.list_changes:
            key_val="set_"+change[0]
            function=eval("self.plot."+key_val)
            function(change[2])
        return
