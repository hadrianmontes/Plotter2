from matplotlib import use
use("Qt4Agg")
import matplotlib.pyplot as plt
from extended_figure import extended_figure

class test_class():
    def __init__(self):
        self.data=[[],[]]
        self.data[0]=[1,2,3,4,5]
        self.data[1]=[i**2 for i in self.data[0]]

if __name__=="__main__":
    b=extended_figure(figsize=(15,8))
    """
    b.define_template(matrix=[[1,2,2,3,4],
                              [1,2,2,5,4],
                              [6,6,6,6,4]])
    """
    b.define_template(matrix=[[1,2,2,8,3],
                              [4,7,7,5,6],
                              [4,7,7,5,6]])
    # b.define_template(size=[3,3])
    b.plot(6,[0,1],[1,2])
    b.plot(2,[0,5],[2,1])
    b.plot(4,[1,2],[1,2])
    b.plot_file("serie_1.dat",5,linestyle="",marker=".")
    b.hist_file("serie_3.dat",1,xcol=0,ycol=1,width="auto")
    b.plot_class(test_class(),3)
    b.tight_layout()

    # b.join_x()
    # b.join_y()
    b.join_xy()
    # b.reset_ticks()


    # b.view_template()


    plt.show()
