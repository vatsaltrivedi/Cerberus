# -*- coding: utf-8 -*-
"""
Created on Wed Oct 09 17:17:48 2013

@author: Vatsal
"""
from pyqt4 import QtGui, QtCore

class StreamWindow(QtGui.QDialog):
    
    buttonBox = QtGui.QDialogButtonBox()
    buttonBox.setOrientation(QtCore.Qt.Horizontal)
    buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

    textBrowser = QtGui.QTextBrowser()
    textBrowser.append("This is a QTextBrowser!")

    verticalLayout = QtGui.QVBoxLayout()
    verticalLayout.addWidget(textBrowser)
    verticalLayout.addWidget(buttonBox)
        
    
