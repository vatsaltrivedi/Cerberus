# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:28:43 2013

@author: Vatsal
"""


class fromfile:
    def __init__(self, fileaddress):
        self.fileaddress = fileaddress
        
        
    ZDisp=[]
    ZLoad=[]
    Time =[]
    ZAmp =[]
    ZPha =[]
    ZExcite=[]
    XDisp =[]
    XLoad =[]
    YDisp =[]
    YLoad =[]
    XAmp=[]
    XPha=[]
    XExc=[]
    YAmp=[]
    YPha=[]
    YExc=[]
    channel = []
    no_of_channels = 0
    def reset(self):
        self.ZDisp=[]
        self.ZLoad=[]
        self.Time =[]
        self.ZAmp =[]
        self.ZPha =[]
        self.ZExcite=[]
        self.XDisp =[]
        self.XLoad =[]
        self.YDisp =[]
        self.YLoad =[]
        self.XAmp=[]
        self.XPha=[]
        self.XExc=[]
        self.YAmp=[]
        self.YPha=[]
        self.YExc=[]
        self.channel = []
        
    def getval(self,line):
        val = []
        char = ''
        for i in range(0, len(line)):
            if line[i] == ',' or line[i] == '\n':
                val.append(char)
                self.no_of_channels +=1
                char=''
            else:
                char += line[i]
        return val
    def getvalfloat(self,line):
        val = []
        char = ''
        for i in range(0, len(line)):
            if line[i] == ',' or line[i] == '\n':
                val.append(float(char))
                char=''
            else:
                char += line[i]
        return val
    def setdata(self,dataset):
        self.ZDisp.append(dataset[0])
        self.ZLoad.append(dataset[1])
        self.Time.append(dataset[2])
        self.ZAmp.append(dataset[3]) 
        self.ZPha.append(dataset[4]) 
        self.ZExcite.append(dataset[5])
        if self.no_of_channels>6:
            self.XDisp.append(dataset[6])
        if self.no_of_channels>7:
            self.XLoad.append(dataset[7]) 
        if self.no_of_channels>8:
            self.YDisp.append(dataset[8]) 
        if self.no_of_channels>9:
            self.YLoad.append(dataset[9])
        if self.no_of_channels>10:
            self.XAmp.append(dataset[10])
        if self.no_of_channels>11:
            self.XPha.append(dataset[11])
        if self.no_of_channels>12:
            self.XExc.append(dataset[12])
        if self.no_of_channels>13:
            self.YAmp.append(dataset[13])
        if self.no_of_channels>14:
            self.YPha.append(dataset[14])
        if self.no_of_channels>15:
            self.YExc.append(dataset[15])
    
    def grabdata(self):
        f = file(self.fileaddress)
        header = f.readline()
      
        self.channel = self.getval(header)

        dataset = []
        while True:
            data = f.readline()
            if len(data) == 0:
                break;
            elif len(data) == 1:
                data = f.readline()
                dataset = self.getvalfloat(data)
                self.setdata(dataset)
            else:
                dataset = self.getvalfloat(data)
                self.setdata(dataset)

    def printdata(self):
        print '****************************************************************Data from channel 1 to 8****************************************************************'
        print '%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t' %(self.channel[0],self.channel[1],self.channel[2],self.channel[3],self.channel[4],self.channel[5],self.channel[6],self.channel[7])
           
        print '______________________________________________________________________________________________'\
              '______________________________________________________________________________________________'

        for i in range(0,15):
            print '%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t' %(self.ZDisp[i],self.ZLoad[i],self.Time[i],self.ZAmp[i],self.ZPha[i],self.ZExcite[i],self.XDisp[i], self.XLoad[i]) 

        print
        print '****************************************************************Data from channel 9 to 16****************************************************************'
        print 
        print '%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t' %(self.channel[8],self.channel[9],self.channel[10],self.channel[11],self.channel[12],self.channel[13],self.channel[14],self.channel[15])
           
        print '______________________________________________________________________________________________'\
              '______________________________________________________________________________________________'

        for i in range(0,15):
            print '%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t%10s\t\t' %(self.YDisp[i],self.YLoad[i],self.XAmp[i],self.XPha[i],self.XExc[i],self.YAmp[i],self.YPha[i],self.YExc[i])
            
    

    

