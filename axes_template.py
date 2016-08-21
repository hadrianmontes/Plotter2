import matplotlib.pyplot as plt
class axes_template():
    """This object defines the template that will be used for plotting"""

    def __init__(self,size=None,matrix=None):
            if matrix:
                # Check if the formating is correct
                self.nrow=len(matrix)
                self.ncol=len(matrix[0])
                for col in matrix:
                    if len(col)!=self.ncol:
                        print("The number of colums per row is not consistent")
                        break
                self.matrix=matrix
                if size is not None:
                    if self.ncol!=size[0] or self.nrow!=size[1]:
                        print("There is a mismatch betwteen the columns/row arguments"+
                              "ant the matrix, the latter will be used")
            elif size is not None:

                self.ncol=size[0]
                self.nrow=size[1]
                self.reset_matrix()

            self.check_matrix()

    def reset_matrix(self):
        self.matrix=[]
        index=1
        for _ in range(self.nrow):
            self.matrix.append([])
            for _ in range(self.ncol):
                self.matrix[-1].append(index)
                index+=1

    def check_matrix(self):
        """
        This function checks if the template matrix is correct
        and it calculates the values for the culumn/rowspan. It
        returns True if everything is correct and False if there
        was any error
        """
        status=True
        list_index=[]
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.matrix[i][j] not in list_index:
                    list_index.append(self.matrix[i][j])
        # make a copy of the matrix for editing
        matrix_copy=[]
        for i in range(self.nrow):
            matrix_copy.append([])
            for j in range(self.ncol):
                matrix_copy[-1].append(self.matrix[i][j])

        self.span=dict()
        for i in list_index:
            self.span[i]=self.check_axes(i,matrix_copy)
            if self.span[i]==[-1,-1,-1,-1]:
                status=False

        # Check if all the elements of the matrix are 0
        for columna in matrix_copy:
            for element in columna:
                if element:
                    print("Error, incorrect format of matrix")
                    return False
        self.chek_joinable()
        return status
                
    def check_axes(self,index,matrix_copy):
        """ This functionwill check that the axes are set
        in a "rectangular" way"""

        # Search for the first ourrence of the index
        breakable=False
        for i in range(self.nrow):
            for j in range(self.ncol):
                if matrix_copy[i][j]==index:
                    breakable=True
                    break
            if breakable:
                break

        # Now check for the boundaries supossing all is correct
        # The column span
        columnspan=0
        for column in range(j,self.ncol):
            if matrix_copy[i][column]==index:
                columnspan+=1
                # make 0 the readed values
                matrix_copy[i][column]=0
        # The row span
        rowspan=1
        for row in range(i,self.nrow):
            if matrix_copy[row][j]==index:
                rowspan+=1
                # make 0 the readed values
                matrix_copy[row][j]=0

        # Check the values inside the boundaries of the row/colspan
        for row in range(i+1,i+rowspan):
            for column in range(j+1,j+columnspan):
                if matrix_copy[row][column]==index:
                    matrix_copy[row][column]=0
                else:
                    print("Incorrect format")
                    return [-1,-1,-1,-1]
        return [i,j,rowspan,columnspan]

    def apply_template(self,figure):
        """
        This function set the template of axes to the figure
        """
        if not self.span:
            print("Template must be set with"+
                  " check_matrix before calling this function")
            return

        # Set the current figure
        plt.figure(figure.number)
        for ax in figure.axes:
            ax.remove()

        self.axes=dict()

        for i in self.span:
            row=self.span[i][0]
            column=self.span[i][1]
            rowspan=self.span[i][2]
            columnspan=self.span[i][3]
            self.axes[i]=plt.subplot2grid((self.nrow,self.ncol),(row,column),
                                          rowspan=rowspan,colspan=columnspan)
        figure.tight_layout()
        return self.axes

    def generate_preview(self):
        fig=plt.figure()
        axis=self.apply_template(fig)
        for axnum in axis:
            ax=axis[axnum]
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_ylim([0,0.2])
            ax.text(0.45,0.09,str(axnum),fontsize=32)

    def chek_joinable(self):
        self.xjoinable=True
        self.yjoinable=True
        # Check first for joinability by columns
        for i in range(self.nrow):
            ref_rowspan=self.span[self.matrix[i][0]][2]
            for j in range(self.ncol):
                if self.span[self.matrix[i][j]][2]!=ref_rowspan:
                    self.yjoinable=False

        # Now by rows
        for j in range(self.ncol):
            ref_colspan=self.span[self.matrix[0][j]][3]
            for i in range(self.nrow):
                if self.span[self.matrix[i][j]][3]!=ref_colspan:
                    self.xjoinable=False

if __name__=="__main__":
    a=axes_template([2,2],matrix=[[1,1],[1,1]])
