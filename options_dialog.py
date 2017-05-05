from ui.preferences_dialog import Ui_Options
import matplotlib
from os import path
import json
from PyQt4 import QtGui

class PreferencesDialog(Ui_Options):
    def __init__(self,*args,**kwargs):
        super(PreferencesDialog,self).__init__(*args,**kwargs)
        self.mode, self.options = load_options()

    def setupUi(self,MainWindow):
        self.parent=MainWindow
        super(PreferencesDialog,self).setupUi(MainWindow)
        self.set_mode()

        self.tickmat1.clicked.connect(self.set_mode1)
        self.tickmat2.clicked.connect(self.set_mode2)
        self.tickcust.clicked.connect(self.set_modecust)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.cancel)

    def accept(self):
        self.recopilate_options()
        options_to_rcparams(self.options)
        save_options(self.mode, self.options)
        self.parent.accept()

    def cancel(self):
        self.parent.close()

    def set_mode1(self):
        self.mode = "1"
        self.set_mode()

    def set_mode2(self):
        self.mode = "2"
        self.set_mode()

    def set_modecust(self):
        self.mode = "custom"
        self.set_mode()

    def set_mode(self):
        if self.mode == "1":
            self.options = get_options_matplotlib1()
            self.tickmat1.setChecked(True)
            self.tickmat2.setChecked(False)
            self.tickcust.setChecked(False)
            self.disable_custom()
        elif self.mode == "2":
            self.options = get_options_matplotlib2()
            self.tickmat1.setChecked(False)
            self.tickmat2.setChecked(True)
            self.tickcust.setChecked(False)
            self.disable_custom()
        elif self.mode == "custom":
            self.tickmat1.setChecked(False)
            self.tickmat2.setChecked(False)
            self.tickcust.setChecked(True)
            self.enable_custom()
        self.update_options()

    def update_options(self):
        self.xtickcombo.setCurrentIndex(self.options["xtick.direction"] == "out")
        self.ytickcombo.setCurrentIndex(self.options["ytick.direction"] == "out")
        self.topcheck.setChecked(self.options["xtick.top"])
        self.leftcheck.setChecked(self.options["ytick.right"])
        self.scaledash.setChecked(self.options["lines.scale_dashes"])
        self.newcycle.setChecked(self.options["new_cycle"])
        self.newlegend.setChecked(self.options["new_legend"])
        self.linewidth.setValue(self.options["lines.linewidth"])
        self.markersize.setValue(self.options["lines.markersize"])
        self.fontsize.setValue(self.options["font.size"])
        values = ("large", "medium", "small")
        index = values.index(self.options["legend.fontsize"])
        self.legendsize.setCurrentIndex(index)
        return

    def recopilate_options(self):
        if (self.mode == "1") or (self.mode == "2"):
            return
        self.options["xtick.direction"] = str(self.xtickcombo.currentText())
        self.options["ytick.direction"] = str(self.ytickcombo.currentText())
        self.options["xtick.top"] = self.topcheck.isChecked()
        self.options["ytick.right"] = self.leftcheck.isChecked()
        self.options["lines.scale_dashes"] = self.scaledash.isChecked()
        self.options["new_cycle"] = self.newcycle.isChecked()
        self.options["new_legend"] = self.newlegend.isChecked()
        self.options["lines.linewidth"] = self.linewidth.value()
        self.options["lines.markersize"] = self.markersize.value()
        self.options["font.size"] = self.fontsize.value()
        self.options["legend.fontsize"] = str(self.legendsize.currentText())

    def disable_custom(self):
        self.xtickcombo.setEnabled(False)
        self.ytickcombo.setEnabled(False)
        self.leftcheck.setEnabled(False)
        self.topcheck.setEnabled(False)
        self.scaledash.setEnabled(False)
        self.newcycle.setEnabled(False)
        self.newlegend.setEnabled(False)
        self.linewidth.setEnabled(False)
        self.markersize.setEnabled(False)
        self.fontsize.setEnabled(False)
        self.legendsize.setEnabled(False)
        return

    def enable_custom(self):
        self.xtickcombo.setEnabled(True)
        self.ytickcombo.setEnabled(True)
        self.leftcheck.setEnabled(True)
        self.topcheck.setEnabled(True)
        self.scaledash.setEnabled(True)
        self.newcycle.setEnabled(True)
        self.newlegend.setEnabled(True)
        self.linewidth.setEnabled(True)
        self.markersize.setEnabled(True)
        self.fontsize.setEnabled(True)
        self.legendsize.setEnabled(True)
        return


def get_options_matplotlib2():
    """
    Return the deafult options to be used with matplotlib 2
    """
    options = {"legend.fontsize": u"medium",
               "font.size": 10,
               "lines.markersize": 6,
               "lines.linewidth": 1.5,
               "lines.scale_dashes": True,
               "new_legend": True,
               "new_cycle": True,
               "xtick.direction": u"out",
               "ytick.direction": u"out",
               "xtick.top": False,
               "ytick.right": False}
    return options

def get_options_matplotlib1():
    """
    Return the deafult options to be used with matplotlib 1
    """
    options = {"legend.fontsize": u"large",
               "font.size": 12,
               "lines.markersize": 20**0.5,
               "lines.linewidth": 1.,
               "lines.scale_dashes": False,
               "new_legend": False,
               "new_cycle": False,
               "xtick.direction": u"in",
               "ytick.direction": u"in",
               "xtick.top": True,
               "ytick.right": True}
    return options

def options_to_rcparams(options):
    """
    Transfer the options inside the rcParams
    """
    special_words = ("new_legend", "new_cycle")
    # New style of legend
    if options["new_legend"]:
        matplotlib.rcParams["legend.fancybox"] = True
        matplotlib.rcParams["legend.numpoints"] = 1
        matplotlib.rcParams["legend.framealpha"] = 0.8
        matplotlib.rcParams["legend.scatterpoints"] = 1
        matplotlib.rcParams["legend.edgecolor"] = u'0.8'
    else:
        matplotlib.rcParams["legend.fancybox"] = False
        matplotlib.rcParams["legend.numpoints"] = 2
        matplotlib.rcParams["legend.framealpha"] = None
        matplotlib.rcParams["legend.scatterpoints"] = 3
        matplotlib.rcParams["legend.edgecolor"] = u'inherit'
    # New color cycle
    if options["new_cycle"]:
        cycler = matplotlib.cycler(color=[u'#1f77b4', u'#ff7f0e',
                                          u'#2ca02c', u'#d62728',
                                          u'#9467bd', u'#8c564b',
                                          u'#e377c2', u'#7f7f7f',
                                          u'#bcbd22', u'#17becf'])
        matplotlib.rcParams["axes.prop_cycle"] = cycler
    else:
        cycler = matplotlib.cycler(color='bgrcmyk')
        matplotlib.rcParams["axes.prop_cycle"] = cycler
    # Transfer all the options except the special ones
    for option in options:
        if option in special_words:
            continue
        matplotlib.rcParams[option] = options[option]

def save_options(mode, options):
    """
    Exports the options and mode to a file to be read later.
    mode: string - 1, 2 or custom
    options: dict with the options to be saved
    """
    cwd = path.dirname(path.abspath(__file__))
    options_file_path = cwd + "/preferences"
    options_file = open(options_file_path, "w")
    # Write the mode at the beggining of the file
    options_file.write(mode+"\n")
    if mode == "custom":
        json.dump(options, options_file)
    options_file.close()

def load_options():
    """
    Retruns the mode and options saved on the preferences file
    """
    cwd = path.dirname(path.abspath(__file__))
    options_file_path = cwd + "/preferences"

    if not path.isfile(options_file_path):
        return default_options()

    options_file = open(options_file_path)
    mode = next(options_file).strip()
    if mode == "1":
        return mode, get_options_matplotlib1()
    elif mode == "2":
        return mode, get_options_matplotlib2()
    elif mode == "custom":
        try:
            return mode, json.loads(next(options_file))
        except ValueError:
            return default_options()
    else:
        raise(KeyError("Unknow mode {}".format(mode)))

def default_options():
    mode = matplotlib.__version__[0]
    if mode == "1":
        options = get_options_matplotlib1()
    elif mode == "2":
        options = get_options_matplotlib2()
    return mode, options
