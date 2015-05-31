# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:13:29 2013

@author: Vatsal
"""

import data
import calibration_values
import calculator
import math
class Cmp_files:
    def __init__(self, fileaddress, calc):
        self.fileaddress = fileaddress
        self.calc = calc
        self.dataset = {}
        
        
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
    
    def setStrainAndStress(self, ft, pr):
        for i in range(0, len(self.dataset['Time'])):
            self.dataset['Strain'].append(self.dataset['ZDispZeroed'][i]/ft)
            self.dataset['Stress'].append((self.dataset['ZLoadCorrectedforKls'][i])/(math.pi * math.pow(pr,2)))
            
        