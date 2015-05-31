# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:08:09 2013

@author: Vatsal
"""

from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg \
import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg \
import NavigationToolbar2QTAgg as NavigationToolbar

from matplotlib.figure import Figure
class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure() 
        self.ax1 = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,
        QtGui.QSizePolicy.Expanding,
        QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
class Mplwidget(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.ntb = NavigationToolbar(self.canvas, MplCanvas())
        self.vbl.addWidget(self.ntb)
        self.setLayout(self.vbl)