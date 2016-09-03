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

    def add_plot(self,index,plot,properties,string=None,path=None):
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

        # Start writting the info of the plots
        for index in self.indexes:
            f.write("Index: ")
            f.write(str(index))
            f.write("\n")
            for uid in self.plot_by_uid:
                plot=self.plot_by_uid[uid]
                if plot["index"]==index:
                    self.write_info(uid,plot,f)

        f.close()
        return

    def write_info(self,uid,plot,filebuffer):
        if "path" not in plot:
            print("Found a non savable plot")
            return
        filebuffer.write("\tPlot: "+str(uid)+"\n")

        # Write the path
        path=str(plot["path"])
        filebuffer.write("\t\tPath "+path+"\n")

        # Write its string
        string=str(plot["string"])
        filebuffer.write("\t\tstring "+string+"\n")

        # Write their properties

        for option in plot["properties"]:
            formated=plot["properties"][option]
            filebuffer.write("\t\t"+option+" "+formated+"\n")
        filebuffer.flush()

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
