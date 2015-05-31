# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:00:30 2013

@author: Vatsal
"""

import data
import calibration_values
import calculator
import math
import cmp_files
class Datafile:
    cmp_objects = []
    index = -1
    def __init__(self, fileaddress,project, indexposition, filename, saved, experiment, calc, xchannel, ychannel, film_thickness, punch_radius, new):
        self.fileaddress = fileaddress
        self.indexposition = indexposition
        self.project = project
        self.filename = filename
        self.saved = saved
        self.experiment = experiment
        self.calc = calc
        self.xchannel = xchannel
        self.ychannel = ychannel
        self.film_thickness = film_thickness
        self.punch_radius = punch_radius
        self.new = new
        self.dataset = {}
        
        
    def setnew(self, new):
        self.new = new
        
    def setxchannel(self, x):
        self.xchannel = x
    
    def setychannel(self, y):
        self.ychannel = y
        
    def setname(self,file_name, exp, pro ):
        self.filename = file_name
        self.project = pro
        self.experiment = exp
    
    def setparamaters(self,filmthickness, radius):
        self.film_thickness = filmthickness
        self.punch_radius = radius

    def createfile(self):
        filedata = data.fromfile(self.fileaddress)
        filedata.reset()
        filedata.grabdata()
        calbval = calibration_values.calbvalue(filedata)
        calbval.reset()
        calbval.setcalbval()
        self.calc = calculator.calculator(filedata, calbval)
        self.calc.reset()
        self.calc.calculate()
        
    def compare_file(self, address):
        self.cmp_objects.append(cmp_files.Cmp_files(address, ""))
        self.index = len(self.cmp_objects) - 1
        self.cmp_objects[self.index].createfile()
        
    def display(self):
        print self.fileaddress
        print self.saved
        print self.project
        print self.experiment
        print self.calc
    
    def setDataset(self):
        self.dataset.clear()
        self.dataset = {}
        self.dataset['Time'] = self.calc.Time
        self.dataset['ZDispTotal']=self.calc.ZDispTotal
        self.dataset['XDisp']= self.calc.XDisp
        self.dataset['YDisp'] = self.calc.YDisp
        self.dataset['ZDispZeroed'] = self.calc.ZDispZeroed
        self.dataset['XDispZeroed'] = self.calc.XDispZeroed
        self.dataset['YDispZeroed']= self.calc.YDispZeroed
        self.dataset['TimeZeroed'] = self.calc.TimeZeroed
        self.dataset['ZAmplitude'] = self.calc.ZAmplitude
        self.dataset['ZForce'] = self.calc.ZForce
        self.dataset['ZLoadV'] = self.calc.ZLoadV
        self.dataset['ZLoadZeroed'] = self.calc.ZLoadZeroed
        self.dataset['ZLoadmN'] = self.calc.ZLoadmN
        self.dataset['ZLoadCorrectedforKls'] = self.calc.ZLoadCorrectedforKls
        self.dataset['ZStiffness'] = self.calc.ZLoadCorrectedforKls
        self.dataset['Strain'] = []
        self.dataset['Stress'] = []
    
    def setStressAndStrain(self, ft, pr):
        for i in range(0, len(self.dataset['Time'])):
            self.dataset['Strain'].append(self.dataset['ZDispZeroed'][i]/ft)
            self.dataset['Stress'].append((self.dataset['ZLoadCorrectedforKls'][i])/(math.pi * math.pow(pr,2)))