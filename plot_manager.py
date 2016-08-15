class Plot_Manager():
    """This class implements a manager to manage existing
    plots with operations such as removing plots, editing existing
    or reverting last change"""

    def __init__(self):
        self.uid=0
        self.plot_by_uid=dict()
        self.uid_by_name=dict()
        self.changes=[]
        self.unchanges=[]

    def add_plot(self,index,plot,string=None,path=None):
        if string is None:
            string="Unnamed plot "+str(self.uid)
        elif string in self.uid_by_name:
            copy=2
            while string+"("+str(copy)+")" in self.uid_by_name:
                copy+=1
            else:
                string=string+"("+str(copy)+")"
        
        self.plot_by_uid[self.uid]={"string":string,"plot":plot,"deleted":False}
        if path: self.plot_by_uid[self.uid]["path"]=path
        self.uid_by_name[string]=self.uid
        self.changes.append(Change(1,plot))
        self.unchanges=[]

    def delete_plot(self,name):
        plot=self[name]
        plot.set_visible("False")
        self.plot_by_uid[uid]["deleted"]=True
        self.changes.append(Change(-1,plot))
        self.unchanges=[]

    def edit_plot(self,name,list_changes):
        plot=self[name]
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


class Change():
    def __init__(self,kind,plot,list_changes=None):
        # each element of list_changes must have the next formating
        # [keyword,previous_value,new_value]
        self.undo_functions=[self.undo_edit,self.undo_add,self.undo_delete]
        self.redo_functions=[self.redo_edit,self.redo_add,self.redo_delete]
        # Kind -1 means plot deleted
        # 0 means plot edited
        # 1 means new plot
        self.kind=kind
        self.plot=plot
        self.list_changes=list_changes

    def undo(self):
       self.undo_functions[self.kind]()

    def redo(self):
        self.redo_functions[self.kind]()

    def undo_add(self):
        self.plot.set_visible(False)
        return

    def redo_add(self):
        self.plot.set_visible(True)
        return

    def undo_delete(self):
        self.plot.set_visible(True)
        return

    def redo_delete(self):
        self.plot.set_visible(False)

    def undo_edit(self):
        for change in list_changes:
            key_val="set_"+change[0]
            eval("self.plot."+key_val+"("+change[2]+")")
        return

    def redo_edit(self):
        for change in list_changes:
            key_val="set_"+change[0]
            eval("self.plot."+key_val+"("+change[1]+")")
        return
        
        


