#Plotter2

Plotter 2 is a remodeled version of the program plotter. It is intended to manage plots 
hat can be confiusing to do in a script in an easy way. It features plotting differnt subplots
in the a single frame. It allows to crate complex geomtries with different sized subpltos and
it is capable of sharing the axes between the subplots (if the geometry is compatible). The input
data must be in raw text (.dat, .xvg,...) and organized by columns (it is possible to have many
columns in a single file). It is possible to export the plots in all the formats allowed by matplotlib
(.pdf,.eps,.png,...). It is also possible to save the work in a text file that can be loaded later
in order to continue or edit the work.

## Installation

The ways to install right now the program is:

  1) Downloading the source code and running
  
     python interface.py
  inside the main folder.
  
  2) Downloading and installing the .deb package (compatible with all the debian based linux releases as ubuntu
  kubuntu,...)
  
The dependecies necesary are: python2.7, matplotlib and pyqt4. There are some distributions of python (as anaconda or pythonXY) that bundle together all this dependencies. If you are installing the deb package using a package manager it is possible that the dependencies are automatically resolved. It is also possible to install it from the terminal as:

    sudo dpkg -i plotter2-version.deb
    sudo apt-get -f install
With this 2 commands all the dependencies will be solved.

Both the source code and the deb package are avaliable in the releases section (https://github.com/hadrianmontes/Plotter2/releases)
