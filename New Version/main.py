# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:38:36 2013

@author: Vatsal
"""
## imports
from __future__ import with_statement
import numpy as np
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from cda_gui import Ui_MainWindow
from mplwidget import Mplwidget
from PyQt4 import QtCore, QtGui
import pickle
import matplotlib.pyplot as plt

## custom modules
 
import data
import calibration_values
import calculator
import os
import datafile
import math
import random

## for translation and encoding
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

## designer main class. The main window for CDA.
class DesignerMainWindow(QMainWindow, Ui_MainWindow):
    ## global variables for Main Window
    ## boolean variables used as indicators    
    file_to_load = ""    
    file_loaded = False
    file_type = ""
    translated_file = ""    
    see_all_channel = False
    
    ## list to store all file objects
    file_objects = []
    color_list = ["b-","g-", "y-", "k-", "c-", "m-", "r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-","r-"]
    cmp_count = 0
    ## used to store data before plotting 

    ## current_project, experiment, and file_objects
    current_project = ''
    current_file = ''
    channellist = ['Time','ZDispTotal' ,'XDisp','YDisp','ZDispZeroed',\
        'XDispZeroed','YDispZeroed','TimeZeroed','ZAmplitude' ,'ZForce' ,'ZLoadV', 'ZLoadZeroed',\
        'ZLoadmN','ZLoadCorrectedforKls' , 'ZStiffness', 'Strain', 'Stress'] 
    
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        ## handlers for different widgets
        
        QObject.connect(self.plotbutton, SIGNAL("clicked()"), self.update_graph)
        QObject.connect(self.pushButton_6, SIGNAL("clicked()"), self.toggle)
        QObject.connect(self.tabarea, SIGNAL("currentChanged(int)"), self.tabchanged)
        QObject.connect(self.actionText, SIGNAL('triggered()'), self.select_textfile)
        QObject.connect(self.actionBinary, SIGNAL('triggered()'), self.select_binfile)
        QObject.connect(self.actionStream, SIGNAL('triggered()'), self.select_stream)
        QObject.connect(self.actionTest_2, SIGNAL('triggered()'), self.opentest)
        QObject.connect(self.actionStream, SIGNAL('triggered()'), self.streamWindow)
        QObject.connect(self.comparebutton, SIGNAL('clicked()'), self.compare_data)
        QObject.connect(self.actionSave, SIGNAL('triggered()'), self.save)
        QObject.connect(self.actionSave_as, SIGNAL('triggered()'), self.saveas)
        QObject.connect(self.actionAbout, SIGNAL('triggered()'), self.about)
        QObject.connect(self.actionContents, SIGNAL('triggered()'), self.contents)
        QObject.connect(self.actionConvert_Binary, SIGNAL('triggered()'), self.convert_binary)
        QObject.connect(self.actionExperiment, SIGNAL('triggered()'), self.new_exp)
        QObject.connect(self.actionProject, SIGNAL('triggered()'), self.new_pro)
        QObject.connect(self.actionQuit, SIGNAL('triggered()'), qApp, SLOT("quit()"))
        QObject.connect(self.commandline, SIGNAL('returnPressed()'), self.execute)
        QObject.connect(self.pushButton_3, SIGNAL('clicked()'), self.remove_cmp)
        QObject.connect(self.stiffnessVload, SIGNAL("triggered()"), self.plot1)
        QObject.connect(self.dispVtime, SIGNAL("triggered()"), self.plot2)
        QObject.connect(self.harAmp, SIGNAL("triggered()"), self.plot3)
        QObject.connect(self.phaseVzdisp, SIGNAL("triggered()"), self.plot4)
        QObject.connect(self.dispAfterContact, SIGNAL("triggered()"), self.plot5)
        QObject.connect(self.crosstalkduringapproach, SIGNAL("triggered()"), self.plot6)
        QObject.connect(self.crosstalkduringloading, SIGNAL("triggered()"), self.plot7)
        QObject.connect(self.loadvdisp, SIGNAL("triggered()"), self.plot8)
        self.view.doubleClicked.connect(self.on_treeView_clicked)
        self.tabarea.tabCloseRequested.connect(self.tab_close)
        self.xaxisbox.currentIndexChanged.connect(self.x_index_changed)
        self.yaxisbox.currentIndexChanged.connect(self.y_index_changed)
        
        for i in self.channellist:
            self.xaxisbox.addItem(i)
            self.yaxisbox.addItem(i)
        self.xaxisbox.setCurrentIndex(4)
        self.yaxisbox.setCurrentIndex(12)
        
    def check(self):
        print "yippee!!"
    def keypressed(self, event):
        print event.key
        
    def x_index_changed(self, index):
        if len(self.file_objects) == 0:
            pass
        else:
            self.file_objects[self.tabarea.currentIndex()].setxchannel(index)

    def y_index_changed(self, index):
        if len(self.file_objects) == 0:
            pass
        else:
            self.file_objects[self.tabarea.currentIndex()].setychannel(index)
    
    def remove_cmp(self):
        pass

    def tab_close(self, index):
        if self.file_objects[index].saved == True:
            self.file_objects.remove(self.file_objects[index])
            self.tabarea.removeTab(index)
        else:
            dialog = QMessageBox(self)
            dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("File not saved.")
            choice = dialog.exec_()
            if choice == QMessageBox.Save:
                self.save()
                self.tabarea.removeTab(index)
                self.file_objects.remove(self.file_objects[index])
            if choice == QMessageBox.Discard:
                self.tabarea.removeTab(index)
                self.file_objects.remove(index)
            if choice == QMessageBox.Cancel:
                pass
            
        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self,index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        filePath = self.model.filePath(indexItem)
        self.file_to_load = filePath
        inputfile = open(filePath, "rb")
        self.file_objects.append(pickle.load(inputfile))
        self.tab = Mplwidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabarea.addTab(self.tab, _fromUtf8("tab")) 
        self.tabarea.setCurrentWidget(self.tab)
        self.tab.canvas.mpl_connect('button_press_event', self.onclick)

        name = self.file_objects[self.tabarea.currentIndex()].filename
        self.update_graph()
        self.tabarea.setTabText(self.tabarea.currentIndex(), _translate("MainWindow", name, None))
        self.tabarea.setTabsClosable(True)
        self.file_loaded = True
        
        
        
    def closeEvent(self,event):
        unsaved_indexes = []
        total_file_objects = self.tabarea.count()        
        for i in range(0,total_file_objects):
            if self.file_objects[i].saved == False:
                unsaved_indexes.append(i)
        count = len(unsaved_indexes)        
        for i in unsaved_indexes:
            self.tabarea.setCurrentIndex(i)
            dialog = QMessageBox(self)
            dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("File not saved.")
            choice = dialog.exec_()
            if choice == QMessageBox.Save:
                self.save()
                count -= 1
            if choice == QMessageBox.Discard:
                count -= 1
            if choice == QMessageBox.Cancel:
                event.ignore()
            if count == 0:
                event.accept()
                
    def new_pro(self):
       ## start a new project
       name,ok = QInputDialog.getText(self, 'New Project', 'Enter Project name' )
       dirlist = os.listdir("projects\\")
       if name in dirlist:
           QMessageBox.information(self, 'Message', ''' Directory exists please enter another name''', QMessageBox.Ok)
           self.new_pro()
       else:
           command = str("mkdir projects\\"+ str(name))
           os.system(command)
           self.view.reset()
           self.view.setModel(self.model)
           self.view.setRootIndex(self.model.index('projects\\'))
           string = str('projects\\' + str(name))
           self.view.expand(self.model.index(string))
           self.current_project = name
           
    def new_exp(self):
        ##start a new experiment
       if self.current_project == '':
                   name,ok = QInputDialog.getText(self, 'Select Project', 'Enter Project name' )
                   if ok == True:
                       dirlist = os.listdir("projects\\")
                       if name not in dirlist:
                           QMessageBox.information(self, 'Message', ''' Project does not exist''', QMessageBox.Ok)
                           self.new_exp()
                       else:
                           self.current_project = name
                           self.new_exp()
                   else:
                       pass
       else:
           exp_name,ok2 = QInputDialog.getText(self, 'New Experiment', 'Enter Experiment name' )
           prodir = str("projects\\" + str(self.current_project))
           dirlist = os.listdir(prodir)
           if exp_name in dirlist:
              QMessageBox.information(self, 'Message', ''' Experiment exists please enter another name''', QMessageBox.Ok)
              self.new_exp()
           else:
               command = str("mkdir projects\\" + str(self.current_project) + "\\" + str(exp_name))
               os.system(command)
               self.view.reset()
               self.view.setModel(self.model)
               self.view.setRootIndex(self.model.index('projects\\'))
               self.current_exp = exp_name
               
    def select_textfile(self):
        self.file_to_load = QFileDialog.getOpenFileName()
        if self.file_to_load:
            self.filename.setText(self.file_to_load)
            self.file_loaded = False
            self.file_type = "txt"
            
        self.statusbar.showMessage('Loaded file : %s '%(self.file_to_load))
        self.update_graph()
    
    def select_binfile(self):
        self.file_to_load = QFileDialog.getOpenFileName()
        if self.file_to_load:
            f = file("file.txt", 'w')
            f2 = file("file2.txt", 'w')
            name = self.file_to_load[-12:-4]
            f.write(self.file_to_load)
            f2.write(name)
            f.close()
            f2.close()
            os.system("check2.bas")
            import time
            time.sleep(2)
            name = self.file_to_load[-12:-4]
            name += ".txt"
            self.file_loaded = False
            self.filename.setText(self.file_to_load)
            self.file_type = "bin"
            self.translated_file = name
        self.statusbar.showMessage('Loaded file : %s '%(self.file_to_load))
        self.update_graph()
    def select_stream(self):
        pass
        
    def opentest(self):
        dialog = QDialog(self)
        label = QLabel("Please select a file")
        label.setGeometry(QtCore.QRect(7,7,400,20))
        layout2 = QVBoxLayout()
        splitter = QtGui.QSplitter()
        model = QtGui.QFileSystemModel(dialog)
        view = QtGui.QTreeView(splitter)
        splitter.setGeometry(QtCore.QRect(0, 0, 400, 200))
        model.setRootPath('projects\\')
        indexRoot = model.index(model.rootPath())
        view.setModel(model)
        view.setRootIndex(indexRoot)
        view.hideColumn(1)
        view.hideColumn(2)
        view.hideColumn(3)
        @QtCore.pyqtSlot(QtCore.QModelIndex)
        def on_treeView_clicked(index):
            indexItem = model.index(index.row(), 0, index.parent())
            filePath = self.model.filePath(indexItem)
            self.file_to_load = filePath
            inputfile = open(filePath, "rb")
            self.file_objects.append(pickle.load(inputfile))
            self.tab = Mplwidget()
            self.tab.setObjectName(_fromUtf8("tab"))
            self.tabarea.addTab(self.tab, _fromUtf8("")) 
            self.tabarea.setCurrentWidget(self.tab)
            name = self.file_objects[self.tabarea.currentIndex()].filename
            self.tab.setObjectName(_fromUtf8(name))
            self.tabarea.setTabText(self.tabarea.indexOf(self.tab), _translate("MainWindow", name, None))
            self.tabarea.setTabsClosable(True)
            self.file_loaded = True
            self.update_graph()
            dialog.close()
        view.doubleClicked.connect(on_treeView_clicked)
        layout2.addWidget(label)
        layout2.addWidget(splitter)
        dialog.setGeometry(QtCore.QRect(300,300,400,300))
        dialog.setWindowTitle("Select")
        dialog.setLayout(layout2)
        dialog.exec_()
    
    def select_project(self):
        
        name,ok = QInputDialog.getText(self, 'Select Project', 'Enter Project name' )
        if ok == True:
            dirlist = os.listdir("projects\\")
            if name not in dirlist:
                       QMessageBox.information(self, 'Message', ''' Project does not exist''', QMessageBox.Ok)
                       self.select_project()
            else:
                       self.current_project = name 
        else:
                       pass
                   
    def select_exp(self):
        name,ok = QInputDialog.getText(self, 'Select Experiment', 'Enter Experiment name' )
        if ok == True:
            dirlist = os.listdir("projects\\" + self.current_project + "\\")
            if name not in dirlist:
                       QMessageBox.information(self, 'Message', ''' Experiment does not exist''', QMessageBox.Ok)
                       self.select_exp()
            else:
                       self.current_exp = name
        else:
                       pass
    
    def save(self):
        file_object = self.file_objects[self.tabarea.currentIndex()]
        if file_object.saved == False:
            if file_object.new == True:
                    self.select_project()
                    self.select_exp()
                    name,ok = QInputDialog.getText(self, 'Save File', 'Enter File name' )                
                    if ok == True:
                        mypath = str("projects/" + self.current_project + "/" + self.current_exp + "/")
                        onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
                        name = str(name) + ".pkl"
                        if name in onlyfiles:
                            QMessageBox.information(self, 'Message', ''' File exists''', QMessageBox.Ok)
                            self.save()
                        else:
                            output = open("projects\\" + self.current_project + "\\" + self.current_exp + "\\"+ name , "wb")
                            file_object.setname(name, self.current_exp, self.current_project)
                            file_object.saved = True
                            file_object.new = False
                            pickle.dump(file_object, output, -1)
                            output.close() 
                            self.tabarea.setTabText(self.tabarea.currentIndex(), _translate("MainWindow", file_object.filename, None))
                            return True
                    else:
                        pass
                        return False
            else:
                output = open("projects\\" + file_object.project + "\\" + file_object.experiment + "\\"+ file_object.filename , "wb")
                file_object.saved = True
                file_object.new = False
                pickle.dump(file_object, output, -1)
                output.close()
                self.tabarea.setTabText(self.tabarea.currentIndex(), _translate("MainWindow", file_object.filename, None))
                return True
        else: 
            return True
                
    def saveas(self):
        pass
    
    def tabchanged(self):
        if self.tabarea.count() > 0:
            self.filename.setText(self.file_objects[self.tabarea.currentIndex()].fileaddress)
            
            if self.file_loaded == False:
                pass
            else:
                self.xaxisbox.setCurrentIndex(self.file_objects[self.tabarea.currentIndex()].xchannel)
                self.yaxisbox.setCurrentIndex(self.file_objects[self.tabarea.currentIndex()].ychannel)
                self.settable()
        
            
    def settable(self):
        rows = len(self.file_objects[self.tabarea.currentIndex()].calc.Time)
        self.datatable.setRowCount(rows)
        
        if self.see_all_channel == False:        
            self.datatable.setColumnCount(2)
            xchannel = self.channellist[self.xaxisbox.currentIndex()]
            ychannel = self.channellist[self.yaxisbox.currentIndex()]
            
            listc = []
            listc.append(xchannel)
            listc.append(ychannel)
            self.datatable.setHorizontalHeaderLabels(listc)
            for j in range(2):
                for i in range(rows):
                    item = self.file_objects[self.tabarea.currentIndex()].dataset[listc[j]][i]
                    self.datatable.setItem(i,j,QTableWidgetItem(QString("%1").arg(item)))
        
        if self.see_all_channel == True:
            self.datatable.setColumnCount(15)
            self.datatable.setHorizontalHeaderLabels(self.channellist)
            for j in range(0,15):
                for i in range(0,rows):
                    item = self.file_objects[self.tabarea.currentIndex()].dataset[self.channellist[j]][i]
                    self.datatable.setItem(i,j,QTableWidgetItem(QString("%1").arg(item)))
    
    def toggle(self):
        if self.see_all_channel == True:
            self.see_all_channel = False
            self.pushButton_6.setText(_translate("MainWindow", "See All", None))
            self.settable()
            
        else:
            self.see_all_channel = True
            self.pushButton_6.setText(_translate("MainWindow", "See Current", None))
            self.settable()
            
    def update_graph(self):
        if self.file_loaded == False:
            try:        
                if self.file_type == "txt":                
                    self.file_objects.append(datafile.Datafile(self.file_to_load,"", self.tabarea.count(), "file", False, "", "",4,12, float(self.thicknessinput.text()), float(self.radiusinput.text()), True)) 
                if self.file_type == "bin":
                    self.file_objects.append(datafile.Datafile(self.translated_file,"",self.tabarea.count(), "file", False, "", "" ,4,12, float(self.thicknessinput.text()), float(self.radiusinput.text()), True))                
                self.tab = Mplwidget()
                self.tab.setObjectName(_fromUtf8("tab"))
                self.tabarea.addTab(self.tab, _fromUtf8("")) 
                count = self.tabarea.count()
                name = "file"  + str(count)
                self.tab.setObjectName(_fromUtf8(name))
                self.tabarea.setTabText(self.tabarea.indexOf(self.tab), _translate("MainWindow", name + " *", None))
                self.tabarea.setTabsClosable(True)
                self.tabarea.setCurrentWidget(self.tab)
                self.file_objects[self.tabarea.currentIndex()].createfile()
                self.file_objects[self.tabarea.currentIndex()].fileaddress = self.file_to_load
                self.tab.canvas.mpl_connect('button_press_event', self.onclick)
                
                self.file_objects[self.tabarea.currentIndex()].setDataset()
                film_thickness = float(self.thicknessinput.text())
                punch_radius = float(self.radiusinput.text())
                self.file_objects[self.tabarea.currentIndex()].setStressAndStrain(film_thickness, punch_radius)
                
                self.current_tab = self.tab
                self.tabarea.setCurrentWidget(self.current_tab)
                self.settable()
                self.file_loaded = True 
            except IOError:
                QMessageBox.information(self, 'Message', ''' Please select a file''', QMessageBox.Ok)
                
        xchannel = self.channellist[self.file_objects[self.tabarea.currentIndex()].xchannel]
        ychannel = self.channellist[self.file_objects[self.tabarea.currentIndex()].ychannel]
        
        self.tabarea.currentWidget().canvas.ax1.clear()
        
            
        self.tabarea.currentWidget().canvas.ax1.plot(self.file_objects[self.tabarea.currentIndex()].dataset[xchannel], self.file_objects[self.tabarea.currentIndex()].dataset[ychannel], 'r-')
        self.tabarea.currentWidget().canvas.ax1.set_xlabel(xchannel)
        self.tabarea.currentWidget().canvas.ax1.set_ylabel(ychannel)
        self.tabarea.currentWidget().canvas.ax1.grid(True)
        self.tabarea.currentWidget().canvas.draw()
        self.drawcomparisions()
        self.settable()
        self.stiffnessVload.setEnabled(True)
        self.dispVtime.setEnabled(True)
        self.harAmp.setEnabled(True)
        self.phaseVzdisp.setEnabled(True)
        self.dispAfterContact.setEnabled(True)
        self.crosstalkduringapproach.setEnabled(True)
        self.crosstalkduringloading.setEnabled(True)
        self.loadvdisp.setEnabled(True)
        
    def drawcomparisions(self):
        cmp_obj = self.file_objects[self.tabarea.currentIndex()].cmp_objects
        count = len(cmp_obj)
        for i in range(count):
            
            self.file_loaded = True  
            xchannel = self.channellist[self.file_objects[self.tabarea.currentIndex()].xchannel]
            ychannel = self.channellist[self.file_objects[self.tabarea.currentIndex()].ychannel]
            
            self.tabarea.currentWidget().canvas.ax1.plot(cmp_obj[i].dataset[xchannel], cmp_obj[i].dataset[ychannel], self.color_list[i])
            self.tabarea.currentWidget().canvas.ax1.grid(True)
            self.tabarea.currentWidget().canvas.draw()
            

    
    def onclick(self, event):
        
        current_file = self.file_objects[self.tabarea.currentIndex()]
        
       
        x_index = current_file.xchannel
        y_index = current_file.ychannel
        x_channel = self.channellist[x_index]
        y_channel = self.channellist[y_index]
        datasize = len(current_file.dataset[x_channel])
        
        row=[]
        for i in range(0,datasize):
            if event.xdata  > (current_file.dataset[x_channel][i]-1) and event.xdata < (current_file.dataset[x_channel][i]+1):
                if event.ydata >( current_file.dataset[y_channel][i]-1) and event.ydata< ( current_file.dataset[y_channel][i]+1):
                        print "check 2"
                        row.append(i)
        for j in row:
            self.datatable.selectRow(j)
            
    def execute(self):
        try:
            text = self.commandline.text()
            exec(text)
        except:
            self.op.append("<font color=red>Error: %s</font>" %text)
    
    def compare_data(self):
        file2 = QFileDialog.getOpenFileName()
        if file2:
            self.file_to_load = file2 
            self.file_objects[self.tabarea.currentIndex()].compare_file(self.file_to_load)
            self.file_objects[self.tabarea.currentIndex()].saved = False
            obj = self.file_objects[self.tabarea.currentIndex()]
            cmp_object = obj.cmp_objects[obj.index]
            cmp_object.createfile()
            ft = float(self.thicknessinput.text())
            pr = float(self.radiusinput.text())
            cmp_object.setStrainAndStress(ft, pr)            
            
            self.file_loaded = True  
            xchannel = self.channellist[self.file_objects[self.tabarea.currentIndex()].xchannel]
            ychannel = self.channellist[self.file_objects[self.tabarea.currentIndex()].ychannel]
            self.tabarea.currentWidget().canvas.ax1.plot(cmp_object.dataset[xchannel], cmp_object.dataset[ychannel], self.color_list[obj.index])
            self.tabarea.currentWidget().canvas.ax1.grid(True)
            self.tabarea.currentWidget().canvas.draw()
            self.tabarea.setTabText(self.tabarea.indexOf(self.tab), _translate("MainWindow", self.file_objects[self.tabarea.currentIndex()].filename + " *", None))
            
#    def calculate(self, caller):
#        film_thickness = float(self.thicknessinput.text())
#        punch_radius = float(self.radiusinput.text())
#        if caller == 1:
#            for i in range(0, len(self.dataset['Time'])):
#                self.dataset['Strain'].append(self.dataset['ZDispZeroed'][i]/film_thickness)
#                self.dataset['Stress'].append((self.dataset['ZLoadCorrectedforKls'][i])/(math.pi * math.pow(punch_radius,2)))
#        if caller == 2:
#            for i in range(0, len(self.dataset2['Time'])):
#                self.dataset2['Strain'].append(self.dataset2['ZDispZeroed'][i]/film_thickness)
#                self.dataset2['Stress'].append((self.dataset2['ZLoadCorrectedforKls'][i])/(math.pi * math.pow(punch_radius,2)))
                
    def is_file_open(self):
        
        if self.tabarea.currentIndex() == -1:
            QMessageBox.information(self, 'Message', ''' Please open a file first !!''', QMessageBox.Ok)
            return False
        else:
            return True
            
    def plot2(self):
        check = self.is_file_open()
        if check == True:
            current = self.file_objects[self.tabarea.currentIndex()]
            self.tabarea.currentWidget().canvas.ax1.clear()
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['Time'], current.dataset['ZDispTotal'], self.color_list[0])
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['Time'], current.dataset['YDisp'], self.color_list[1])
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['Time'], current.dataset['XDisp'], self.color_list[2])
            self.tabarea.currentWidget().canvas.ax1.grid(True)
            self.tabarea.currentWidget().canvas.draw()
                    
                        
    def plot1(self):
        check = self.is_file_open()
        if check == True:
            current = self.file_objects[self.tabarea.currentIndex()]
            self.tabarea.currentWidget().canvas.ax1.clear()
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['ZLoadmN'], current.dataset['ZStiffness'], self.color_list[0])
            self.tabarea.currentWidget().canvas.ax1.grid(True)
            self.tabarea.currentWidget().canvas.draw()
                    
    def plot3(self):
        check = self.is_file_open()
        if check == True:
            current = self.file_objects[self.tabarea.currentIndex()]
            self.tabarea.currentWidget().canvas.ax1.clear()
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['ZDispTotal'], current.dataset['ZAmp'], self.color_list[0])
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['ZDispTotal'], current.dataset['XAmp'], self.color_list[1])
            self.tabarea.currentWidget().canvas.ax1.plot(current.dataset['ZDispTotal'], current.dataset['YDisp'], self.color_list[2])
            self.tabarea.currentWidget().canvas.ax1.grid(True)
            self.tabarea.currentWidget().canvas.draw()          
    def plot4(self):
        pass            
    def plot5(self):
        pass            
    def plot6(self):
        pass            
    def plot7(self):
        pass            
    def plot8(self):
        pass            
        
    def about(self):
        QMessageBox.showMaximized
        
    def contents(self):
        pass        
        ## help contents
    
    def convert_binary(self):
        pass        
        ## conert to binary
    def streamWindow(self):
        
        num,ok = QInputDialog.getText(self, 'Indents', 'Number of indents' )
        for i in range(0,int(num)):
            os.system("stream3.bas")
            self.file_to_load = "Temp.txt"
            if self.file_to_load:
                self.filename.setText(self.file_to_load)
                self.file_loaded = False
                self.file_type = "txt"
            
            self.statusbar.showMessage('Loaded file : %s '%(self.file_to_load))
            self.update_graph()
            self.save()
            os.system("del Temp.txt")
            
                                 
           
app = QApplication(sys.argv)
dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())

