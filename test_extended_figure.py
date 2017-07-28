import unittest
from extended_figure import extended_figure

class Test_extended_figure(unittest.TestCase):

    def setUp(self):
        self.fig = extended_figure()
        self.fig.define_template(size=(2,2))

    def test_plot_file(self):
        self.fig.plot_file("test_files/test_1.dat", 1, xcol=0, ycol=1)

    def test_error_index_plot_file(self):
        self.assertRaises(KeyError, self.call_plot_error)

    def call_plot_error(self):
        self.fig.plot_file("test_files/test_1.dat", 0, xcol=0, ycol=1)

    def test_errorbar(self):
        self.fig.errorbar_file("test_files/test_1.dat", 1,
                               xcol=0, ycol=1, yerrcol=1)


    def test_show(self):
        self.fig.show()

if __name__ == "__main__":
    Test_extended_figure.main()
