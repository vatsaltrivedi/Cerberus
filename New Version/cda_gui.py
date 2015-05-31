# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cda_gui.ui'
#
# Created: Tue Aug 27 12:13:37 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pickle
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1166, 890)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtGui.QScrollArea(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(500)
        sizePolicy.setVerticalStretch(500)
        self.centralwidget.setSizePolicy(sizePolicy)
        
        self.topwidget = QtGui.QWidget(self.centralwidget)
        self.topwidget.setGeometry(QtCore.QRect(10, 10, 1145, 641))
        sizePolicy.setHeightForWidth(self.topwidget.sizePolicy().hasHeightForWidth())
        self.topwidget.setSizePolicy(sizePolicy)
        self.topwidget.setObjectName(_fromUtf8("topwidget"))
        
        self.proexpwidget = QtGui.QWidget(self.topwidget)
        self.proexpwidget.setGeometry(QtCore.QRect(10, 10, 181, 621))
        self.proexpwidget.setSizePolicy(sizePolicy)
        self.proexpwidget.setObjectName(_fromUtf8("proexpwidget"))
        
        self.widget_4 = QtGui.QWidget(self.topwidget)
        self.widget_4.setGeometry(QtCore.QRect(200, 10, 711, 621))
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        
        self.inputwidget = QtGui.QWidget(self.widget_4)
        self.inputwidget.setGeometry(QtCore.QRect(10, 10, 691, 90))
        self.inputwidget.setObjectName(_fromUtf8("inputwidget"))
        self.inputwidget.setSizePolicy(sizePolicy)
        
        self.filename = QtGui.QLineEdit(self.inputwidget)
        self.filename.setGeometry(QtCore.QRect(60, 10, 321, 20))
        self.filename.setObjectName(_fromUtf8("filename"))
        
        self.label = QtGui.QLabel(self.inputwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.thicknessLabel = QtGui.QLabel(self.inputwidget)
        self.thicknessLabel.setGeometry(QtCore.QRect(20,35,70,15))
        
        self.thicknessinput = QtGui.QLineEdit(self.inputwidget)
        self.thicknessinput.setGeometry(QtCore.QRect(95,35,70,15))
        self.thicknessinput.setText("1.0")
        
        self.radiuslabel = QtGui.QLabel(self.inputwidget)
        self.radiuslabel.setGeometry(QtCore.QRect(170,35,70,15))
        
        self.radiusinput = QtGui.QLineEdit(self.inputwidget)
        self.radiusinput.setGeometry(QtCore.QRect(240,35,70,15))
        self.radiusinput.setText("1.0")
        
        self.xaxisbox = QtGui.QComboBox(self.inputwidget)
        self.xaxisbox.setGeometry(QtCore.QRect(60, 60, 131, 22))
        self.xaxisbox.setObjectName(_fromUtf8("xaxisbox"))
        
        self.yaxisbox = QtGui.QComboBox(self.inputwidget)
        self.yaxisbox.setGeometry(QtCore.QRect(250, 60, 131, 22))
        self.yaxisbox.setObjectName(_fromUtf8("yaxisbox"))
        
        self.label_2 = QtGui.QLabel(self.inputwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.label_3 = QtGui.QLabel(self.inputwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.comparebutton = QtGui.QPushButton(self.inputwidget)
        self.comparebutton.setGeometry(QtCore.QRect(520, 10, 75, 23))
        self.comparebutton.setObjectName(_fromUtf8("comparebutton"))
        
        self.markpointbutton = QtGui.QPushButton(self.inputwidget)
        self.markpointbutton.setGeometry(QtCore.QRect(600, 10, 75, 23))
        self.markpointbutton.setObjectName(_fromUtf8("markpointbutton"))
        
        self.pushButton_3 = QtGui.QPushButton(self.inputwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 40, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        self.pushButton_4 = QtGui.QPushButton(self.inputwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 40, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        
        self.plotbutton = QtGui.QPushButton(self.inputwidget)
        self.plotbutton.setGeometry(QtCore.QRect(440, 10, 75, 23))
        self.plotbutton.setObjectName(_fromUtf8("plotbutton"))
        
        self.pushButton_6 = QtGui.QPushButton(self.inputwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        
        self.widget_7 = QtGui.QWidget(self.widget_4)
        self.widget_7.setGeometry(QtCore.QRect(10, 100, 691, 511))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        
        self.tabarea = QtGui.QTabWidget(self.widget_7)
        self.tabarea.setGeometry(QtCore.QRect(16, 9, 661, 491))
        self.tabarea.setMouseTracking(True)
        self.tabarea.setObjectName(_fromUtf8("tabarea"))
    
        self.dataarea = QtGui.QScrollArea(self.topwidget)
        self.dataarea.setGeometry(QtCore.QRect(920, 10, 221, 621))
        self.dataarea.setWidgetResizable(True)
        self.dataarea.setObjectName(_fromUtf8("dataarea"))
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 619))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        
        self.datatable = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.datatable.setGeometry(QtCore.QRect(10, 10, 201, 601))
        self.datatable.setObjectName(_fromUtf8("datatable"))
        
        self.dataarea.setWidget(self.scrollAreaWidgetContents)
        
        self.cmdwidget = Cmdwidget(self.centralwidget)
        self.cmdwidget.setGeometry(QtCore.QRect(9, 658, 1145, 181))
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdwidget.sizePolicy().hasHeightForWidth())
        
        self.cmdwidget.setSizePolicy(sizePolicy)
        self.cmdwidget.setObjectName(_fromUtf8("cmdwidget"))
        
        self.outputarea = QtGui.QTextBrowser(self.cmdwidget)
        self.outputarea.setGeometry(QtCore.QRect(10, 10, 1121, 131))
        self.outputarea.setObjectName(_fromUtf8("outputarea"))
        
        self.commandline = QtGui.QLineEdit(self.cmdwidget)
        self.commandline.setGeometry(QtCore.QRect(10, 150, 1121, 21))
        self.commandline.setObjectName(_fromUtf8("commandline"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1166, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuNew = QtGui.QMenu(self.menuFile)
        self.menuNew.setObjectName(_fromUtf8("menuNew"))
        
        self.menuTest = QtGui.QMenu(self.menuNew)
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        
        self.menuOpen = QtGui.QMenu(self.menuFile)
        self.menuOpen.setObjectName(_fromUtf8("menuOpen"))
        
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionBinary = QtGui.QAction(MainWindow)
        self.actionBinary.setObjectName(_fromUtf8("actionBinary"))
        
        self.actionText = QtGui.QAction(MainWindow)
        self.actionText.setObjectName(_fromUtf8("actionText"))
        
        self.actionStream = QtGui.QAction(MainWindow)
        self.actionStream.setObjectName(_fromUtf8("actionStream"))
        
        self.actionExperiment = QtGui.QAction(MainWindow)
        self.actionExperiment.setObjectName(_fromUtf8("actionExperiment"))
        
        self.actionProject = QtGui.QAction(MainWindow)
        self.actionProject.setObjectName(_fromUtf8("actionProject"))
        
        self.actionTest_2 = QtGui.QAction(MainWindow)
        self.actionTest_2.setObjectName(_fromUtf8("actionTest_2"))
        
        self.actionProject_2 = QtGui.QAction(MainWindow)
        self.actionProject_2.setObjectName(_fromUtf8("actionProject_2"))
        
        self.actionExperiment_2 = QtGui.QAction(MainWindow)
        self.actionExperiment_2.setObjectName(_fromUtf8("actionExperiment_2"))
        
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        
        
        
        self.actionConvert_Binary = QtGui.QAction(MainWindow)
        self.actionConvert_Binary.setObjectName(_fromUtf8("actionConvert_Binary"))
        
        self.stiffnessVload = QtGui.QAction(MainWindow)
        self.stiffnessVload.setObjectName(_fromUtf8("stiffnessVload"))
        
        self.dispVtime = QtGui.QAction(MainWindow)
        self.dispVtime.setObjectName(_fromUtf8("dispVtime"))
        
        self.harAmp = QtGui.QAction(MainWindow)
        self.harAmp.setObjectName(_fromUtf8("harAmp"))
        
        self.phaseVzdisp = QtGui.QAction(MainWindow)
        self.phaseVzdisp.setObjectName(_fromUtf8("phaseVzdisp"))
        
        self.dispAfterContact = QtGui.QAction(MainWindow)
        self.dispAfterContact.setObjectName(_fromUtf8("dispAfterContact"))
        
        self.crosstalkduringapproach = QtGui.QAction(MainWindow)
        self.crosstalkduringapproach.setObjectName(_fromUtf8("crosstalkduringapproach"))
        
        self.crosstalkduringloading = QtGui.QAction(MainWindow)
        self.crosstalkduringloading.setObjectName(_fromUtf8("crosstalkduringloading"))
        
        self.loadvdisp = QtGui.QAction(MainWindow)
        self.loadvdisp.setObjectName(_fromUtf8("loadvdisp"))
        
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        
        self.actionContents = QtGui.QAction(MainWindow)
        self.actionContents.setObjectName(_fromUtf8("actionContents"))
        
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        
        
        
        self.menuTest.addAction(self.actionBinary)
        self.menuTest.addAction(self.actionText)
        self.menuTest.addAction(self.actionStream)
        
        self.menuView.addAction(self.stiffnessVload)
        self.menuView.addAction(self.dispVtime)
        self.menuView.addAction(self.harAmp)
        self.menuView.addAction(self.phaseVzdisp)
        
        self.menuView.addAction(self.crosstalkduringapproach)
        self.menuView.addAction(self.crosstalkduringloading)
        self.menuView.addAction(self.loadvdisp)
        self.menuNew.addAction(self.menuTest.menuAction())
        
        
        self.menuNew.addAction(self.actionExperiment)
        self.menuNew.addAction(self.actionProject)
        self.menuOpen.addAction(self.actionTest_2)
        self.menuOpen.addAction(self.actionProject_2)
        self.menuOpen.addAction(self.actionExperiment_2)
        
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        
        self.menuTools.addAction(self.actionConvert_Binary)
        self.menuTools.addAction(self.actionDelete)
        
        

        
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionAbout)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.splitter = QtGui.QSplitter(self.proexpwidget)
        self.model = QtGui.QFileSystemModel(self.proexpwidget)
        self.view = QtGui.QTreeView(self.splitter)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 181, 621))
        self.retranslateUi(MainWindow)
        
        self.tabarea.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(_translate("MainWindow", "Cerberus Data Analyzer", None))
        self.label.setText(_translate("MainWindow", "File", None))
        self.label_2.setText(_translate("MainWindow", "X-Axis", None))
        self.label_3.setText(_translate("MainWindow", "Y-Axis", None))
        self.thicknessLabel.setText(_translate("MainWindow", "Film Thickness", None))
        self.radiuslabel.setText(_translate("MainWindow", "Punch Radius", None))
        self.comparebutton.setText(_translate("MainWindow", "Compare", None))
        self.markpointbutton.setText(_translate("MainWindow", "Mark Points", None))
        self.pushButton_3.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_4.setText(_translate("MainWindow", "Copy", None))
        self.plotbutton.setText(_translate("MainWindow", "Plot", None))
        self.pushButton_6.setText(_translate("MainWindow", "See All", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuNew.setTitle(_translate("MainWindow", "New", None))
        self.menuTest.setTitle(_translate("MainWindow", "Test", None))
        self.menuOpen.setTitle(_translate("MainWindow", "Open", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
            
        self.actionBinary.setText(_translate("MainWindow", "Binary", None))
        self.actionText.setText(_translate("MainWindow", "Text", None))
        self.actionStream.setText(_translate("MainWindow", "Stream", None))
        self.actionExperiment.setText(_translate("MainWindow", "Experiment", None))
        self.actionProject.setText(_translate("MainWindow", "Project", None))
        self.actionTest_2.setText(_translate("MainWindow", "Test", None))
        self.actionProject_2.setText(_translate("MainWindow", "Project", None))
        self.actionExperiment_2.setText(_translate("MainWindow", "Experiment", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionPrint.setText(_translate("MainWindow", "Print", None))
        self.actionConvert_Binary.setText(_translate("MainWindow", "Convert Binary", None))
        self.stiffnessVload.setText(_translate("MainWindow", "Stiffness_v_Load", None))
        self.dispVtime.setText(_translate("MainWindow", "Displacement_v_Time", None))
        self.harAmp.setText(_translate("MainWindow", "Harmonic Amplitude", None))
        self.phaseVzdisp.setText(_translate("MainWindow", "Phase Angle _v_ Vertical Displacement", None))
        self.dispAfterContact.setText(_translate("MainWindow", "Displacement after Contact", None))
        self.crosstalkduringapproach.setText(_translate("MainWindow", "Cross Talk During Approach", None))            
        self.crosstalkduringloading.setText(_translate("MainWindow", "Cross talk during Load", None))
        self.loadvdisp.setText(_translate("MainWindow", "Load_v_Displacement", None)) 
        
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionContents.setText(_translate("MainWindow", "Contents", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.model.setRootPath('projects\\')
        self.indexRoot = self.model.index(self.model.rootPath())
        self.view.setRootIndex(self.indexRoot)
        self.view.setModel(self.model)
        self.view.setRootIndex(self.model.index('projects\\'))
        self.view.hideColumn(1)
        self.view.hideColumn(2)
        self.view.hideColumn(3)
        self.stiffnessVload.setEnabled(False)
        self.dispVtime.setEnabled(False)
        self.harAmp.setEnabled(False)
        self.phaseVzdisp.setEnabled(False)
        self.dispAfterContact.setEnabled(False)
        self.crosstalkduringapproach.setEnabled(False)
        self.crosstalkduringloading.setEnabled(False)
        self.loadvdisp.setEnabled(False)
        
        self.outputarea.append('<font color = red> Loaded the CDA program</font>')
        self.commandline.setText("Type your command here")
        self.commandline.selectAll()
        self.commandline.setFocus()
        
from mplwidget import Mplwidget
from cmdwidget import Cmdwidget
