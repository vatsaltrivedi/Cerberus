# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:38:36 2013

@author: Vatsal
"""
from __future__ import with_statement
import numpy as np
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from cda_gui import Ui_MainWindow
import data
import calibration_values
import calculator
import os
from mplwidget import Mplwidget
from PyQt4 import QtCore, QtGui
import datafile
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

class DesignerMainWindow(QMainWindow, Ui_MainWindow):
    load = False
    saved = True
    files = []
    file_count = 0
    cmpfiles_count = 0
    cmpfiles = []
    dataset = {}
    dataset2 = {}
    current_project = ''
    current_exp = ''
    current_file = ''
    current_tab = ''
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        QObject.connect(self.plotbutton, SIGNAL("clicked()"), self.update_graph)

        QObject.connect(self.actionText, SIGNAL('triggered()'), self.select_textfile)
        QObject.connect(self.actionBinary, SIGNAL('triggered()'), self.select_binfile)
        QObject.connect(self.actionStream, SIGNAL('triggered()'), self.select_stream)
        QObject.connect(self.actionTest_2, SIGNAL('triggered()'), self.opentest)
        QObject.connect(self.actionExperiment_2, SIGNAL('triggered()'), self.openexp)        
        QObject.connect(self.actionProject_2, SIGNAL('triggered()'), self.openpro)
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
       #QObject.connect(self.file_selected, 'doubleclicked()', )
        self.channellist = ['Time','ZDispTotal' ,'XDisp','YDisp','ZDispZeroed',\
        'XDispZeroed','YDispZeroed','TimeZeroed','ZAmplitude' ,'ZForce' ,'ZLoadV', 'ZLoadZeroed',\
        'ZLoadmN','ZLoadCorrectedforKls' , 'ZStiffness']        
        for i in self.channellist:
            self.xaxisbox.addItem(i)
            self.yaxisbox.addItem(i)
        self.xaxisbox.setCurrentIndex(1)
        self.yaxisbox.setCurrentIndex(12)
        
    def select_textfile(self):
        file1 = QFileDialog.getOpenFileName()
        if file1:
            self.filename.setText(file1)
            self.load = False
            self.saved = False
        self.statusbar.showMessage('Loaded file : %s '%(file1))
        
        
    def select_binfile(self):
        file1 = QFileDialog.getOpenFileName()
        if file1:
            f = file("file.txt", 'w')
            f2 = file("file2.txt", 'w')
            name = file1[-12:-4]
            f.write(file1)
            f2.write(name)
            f.close()
            f2.close()
            
            os.system("check2.bas")
            import time
            time.sleep(2)
            name = file1[-12:-4]
            name += ".txt"
            self.load = False
            self.saved = False
            self.filename.setText(name)
        self.statusbar.showMessage('Loaded file : %s '%(file1))
    def closeEvent(self,event):
        if self.saved == True:
            event.accept()
        else:
            dialog = QMessageBox(self)
            dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("File not saved.")
            choice = dialog.exec_()
            if choice == QMessageBox.Save:
                self.save()
            if choice == QMessageBox.Discard:
                event.accept()
            if choice == QMessageBox.Cancel:
                event.ignore()
                
    def opentest(self):
        pass
    def openexp(self):
        pass
    def openpro(self):
        pass
    
    def update_graph(self):
        if self.load == False:
            try:        
                
                data1 = data.fromfile(self.filename.text())
                data1.reset()
                data1.grabdata()
                calbval = calibration_values.calbvalue(data1)
                calbval.reset()
                calbval.setcalbval()
                calc = calculator.calculator(data1, calbval)
                calc.reset()
                calc.calculate()
                
                self.dataset.clear()
                self.dataset = {}
                self.dataset['Time'] = calc.Time
                self.dataset['ZDispTotal']=calc.ZDispTotal
                self.dataset['XDisp']= calc.XDisp
                self.dataset['YDisp'] = calc.YDisp
                self.dataset['ZDispZeroed'] = calc.ZDispZeroed
                self.dataset['XDispZeroed'] = calc.XDispZeroed
                self.dataset['YDispZeroed']= calc.YDispZeroed
                self.dataset['TimeZeroed'] = calc.TimeZeroed
                self.dataset['ZAmplitude'] = calc.ZAmplitude
                self.dataset['ZForce'] = calc.ZForce
                self.dataset['ZLoadV'] = calc.ZLoadV
                self.dataset['ZLoadZeroed'] = calc.ZLoadZeroed
                self.dataset['ZLoadmN'] = calc.ZLoadmN
                self.dataset['ZLoadCorrectedforKls'] = calc.ZLoadCorrectedforKls
                self.dataset['ZStiffness'] = calc.ZLoadCorrectedforKls
                
                self.load = True                
                self.tab = Mplwidget()
                self.tab.setObjectName(_fromUtf8("tab"))
                self.tabarea.addTab(self.tab, _fromUtf8("")) 
                self.current_tab =self.tab
                self.tabarea.setTabText(self.tabarea.indexOf(self.tab), _translate("MainWindow", "Untitled *", None))
                del(calc, data1, calbval)
                
            except IOError,e:
                QMessageBox.information(self, 'Message', ''' Please select a file''', QMessageBox.Ok)
                print '--------' 
        
        xchannel = self.channellist[self.xaxisbox.currentIndex()]
        ychannel = self.channellist[self.yaxisbox.currentIndex()]
        
        print len(self.dataset[xchannel])
        print len(self.dataset[ychannel])
             
        self.current_tab.canvas.ax1.clear()
        self.current_tab.canvas.ax1.plot(self.dataset[xchannel], self.dataset[ychannel], 'r-')
        self.current_tab.canvas.ax1.set_xlabel(xchannel)
        self.current_tab.canvas.ax1.set_ylabel(ychannel)
        self.current_tab.canvas.ax1.grid(True)
        self.current_tab.canvas.draw()
        
    def execute(self):
        try:
            text = self.commandline.text()
            exec(text)
        except:
            self.op.append(
                    "<font color=red>Error: %s</font>" %text)
    
    def select_stream(self):
        pass
        ## to get data from stream
        
    def compare_data(self):
        file2 = QFileDialog.getOpenFileName()
        if file2:
            data1 = data.fromfile(file2)
            data1.reset()
            data1.grabdata()
            calbval = calibration_values.calbvalue(data1)
            calbval.reset()
            calbval.setcalbval()
            calc = calculator.calculator(data1, calbval)
            calc.reset()
            calc.calculate()
            
            self.dataset2.clear()
            self.dataset2= {}
            self.dataset2['Time'] = calc.Time
            self.dataset2['ZDispTotal']=calc.ZDispTotal
            self.dataset2['XDisp']= calc.XDisp
            self.dataset2['YDisp'] = calc.YDisp
            self.dataset2['ZDispZeroed'] = calc.ZDispZeroed
            self.dataset2['XDispZeroed'] = calc.XDispZeroed
            self.dataset2['YDispZeroed']= calc.YDispZeroed
            self.dataset2['TimeZeroed'] = calc.TimeZeroed
            self.dataset2['ZAmplitude'] = calc.ZAmplitude
            self.dataset2['ZForce'] = calc.ZForce
            self.dataset2['ZLoadV'] = calc.ZLoadV
            self.dataset2['ZLoadZeroed'] = calc.ZLoadZeroed
            self.dataset2['ZLoadmN'] = calc.ZLoadmN
            self.dataset2['ZLoadCorrectedforKls'] = calc.ZLoadCorrectedforKls
            self.dataset2['ZStiffness'] = calc.ZLoadCorrectedforKls
            self.load = True  
            xchannel = self.channellist[self.xaxisbox.currentIndex()]
            ychannel = self.channellist[self.yaxisbox.currentIndex()]
            
            print len(self.dataset[xchannel])
            print len(self.dataset[ychannel])
                 
            
            self.plotwidget.canvas.ax1.plot(self.dataset2[xchannel], self.dataset2[ychannel], 'b-')
            self.plotwidget.canvas.ax1.set_xlabel(xchannel)
            self.plotwidget.canvas.ax1.set_ylabel(ychannel)
            self.plotwidget.canvas.ax1.grid(True)
            self.plotwidget.canvas.draw()
        
        
    def save(self):
        if self.saved == False:
            if self.current_project == '':
                self.select_project()
            if self.current_exp == '':
                self.select_exp()
            if self.current_file == '':
                name,ok = QInputDialog.getText(self, 'Save File', 'Enter File name' )                
                if ok == True:
                    dirlist = os.listdir("projects\\" + self.current_project + "\\" + self.current_exp + "\\")
                    if name in dirlist:
                       QMessageBox.information(self, 'Message', ''' File exists''', QMessageBox.Ok)
                       self.save()
                    else:
                        
                        
                        source = self.filename.text()
                        print source
                        print name
                        command = str("Copy " + str(source) + " " + str(name) + ".TXT")              
                        os.system(command)
                                                
                        
                else:
                       pass                
                self.saved = True
                
        else: 
            pass
        
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
        
    def saveas(self):
        self.saved = True
        ## save as desired filename
        
    def about(self):
        dialog = QDialogButtonBox(self)
        label = QLabel("check")
        lineedit = QLineEdit()
        dialog.set
        dialog.setStandardButtons()
        
    def contents(self):
        pass        
        ## help contents
    
    def convert_binary(self):
        pass        
        ## conert to binary
    
    def new_exp(self):
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
               self.view.setRootIndex(self.model.index('e:\\final\\v6\\projects'))
               self.current_exp = exp_name
        ##start a new experiment
    
    def new_pro(self):
              
        ## start a new project
       name,ok = QInputDialog.getText(self, 'New Project', 'Enter Project name' )
       import os
       dirlist = os.listdir("projects\\")
       if name in dirlist:
           QMessageBox.information(self, 'Message', ''' Directory exists please enter another name''', QMessageBox.Ok)
           self.new_pro()
       else:
           command = str("mkdir projects\\"+ str(name))
           
           os.system(command)
           self.view.reset()
           self.view.setModel(self.model)
           self.view.setRootIndex(self.model.index('e:\\final\\v6\\projects'))
           string = str('e:\\final\\v6\\projects' + str(name))
           self.view.expand(self.model.index(string))
           self.current_project = name
           
           
app = QApplication(sys.argv)
dmw = DesignerMainWindow()
dmw.show()

sys.exit(app.exec_())
