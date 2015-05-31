# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:40:09 2013

@author: Vatsal
"""
class calbvalue:
    def __init__(self, data):
            self.data = data
    
    import math
    import calibration_constant as calbcons
    disprng = []
    dispoff = []
    dcdispcalb = []
    acdispcalb  = []        
    loadrng = []
    dcloadcalb = []
    acloadcalb = []
    modfact = []
    
    calb = calbcons.calbcons()
    def reset(self):
        self.disprng = []
        self.dispoff = []
        self.dcdispcalb = []
        self.acdispcalb  = []        
        self.loadrng = []
        self.dcloadcalb = []
        self.acloadcalb = []
        self.modfact = []
    def setcalbval(self):    
        self.disprng.append(round(((self.data.ZDisp[0])/10000)-1))
        self.disprng.append(round(((self.data.XDisp[0])/10000)-1))
        self.disprng.append(round(((self.data.YDisp[0])/10000)-1))
        
        self.dispoff.append( round( (  (self.data.ZDisp[0]-( ( self.disprng[0]+1 )*10000 ) )-5)/10 ) ) 
        self.dispoff.append( round( (  (self.data.XDisp[0]-( ( self.disprng[1]+1 )*10000 ) )-5)/10 ) )
        self.dispoff.append( round( (  (self.data.YDisp[0]-( ( self.disprng[2]+1 )*10000 ) )-5)/10 ) )
        
        
        
        self.dcdispcalb.append(self.calb.dccalibrations['dispconstterm'][0] + self.calb.dccalibrations['displinterm'][0]*(self.dispoff[0]-128) + \
                           self. calb.dccalibrations['dispsqrterm'][0]*(self.math.pow((self.dispoff[0]-128),2)))
        self.dcdispcalb.append(self.calb.dccalibrations['dispconstterm'][1] + self.calb.dccalibrations['displinterm'][1]*(self.dispoff[1]-128) + \
                            self.calb.dccalibrations['dispsqrterm'][1]*(self.math.pow((self.dispoff[1]-128),2)))
        self.dcdispcalb.append(self.calb.dccalibrations['dispconstterm'][2] + self.calb.dccalibrations['displinterm'][2]*(self.dispoff[2]-128) + \
                            self.calb.dccalibrations['dispsqrterm'][2]*(self.math.pow((self.dispoff[2]-128),2)))
        
        
        self.acdispcalb.append(self.calb.accalibrations['dispconstterm'][0] + self.calb.accalibrations['displinterm'][0]*(self.dispoff[0]-128) + \
                            self.calb.accalibrations['dispsqrterm'][0]*(self.math.pow((self.dispoff[0]-128),2)))
        self.acdispcalb.append(self.calb.accalibrations['dispconstterm'][1] + self.calb.accalibrations['displinterm'][1]*(self.dispoff[1]-128) + \
                            self.calb.dccalibrations['dispsqrterm'][1]*(self.math.pow((self.dispoff[1]-128),2)))
        self. acdispcalb.append(self.calb.accalibrations['dispconstterm'][2] + self.calb.accalibrations['displinterm'][2]*(self.dispoff[2]-128) + \
                            self.calb.accalibrations['dispsqrterm'][2]*(self.math.pow((self.dispoff[2]-128),2)))
        
        self.loadrng.append(round((self.data.ZLoad[0]/10)-1))        
        self.loadrng.append(round((self.data.XLoad[0]/10)-1))        
        self.loadrng.append(round((self.data.YLoad[0]/10)-1))
        
        self.dcloadcalb.append(self.calb.dccalibrations['loadconstterm'][0] + self.calb.dccalibrations['loadlinterm'][0]*(self.dispoff[0]-128) + \
                            self.calb.dccalibrations['loadsqrterm'][0]*self.math.pow((self.dispoff[0]-128),2))
        self.dcloadcalb.append(self.calb.dccalibrations['loadconstterm'][1] + self.calb.dccalibrations['loadlinterm'][1]*(self.dispoff[1]-128) + \
                            self.calb.dccalibrations['loadsqrterm'][1]*self.math.pow((self.dispoff[1]-128),2))
        self.dcloadcalb.append(self.calb.dccalibrations['loadconstterm'][2] + self.calb.dccalibrations['loadlinterm'][2]*(self.dispoff[2]-128) + \
                            self.calb.dccalibrations['loadsqrterm'][2]*self.math.pow((self.dispoff[2]-128),2))
                            
        self.acloadcalb.append(self.calb.accalibrations['loadconstterm'][0] + self.calb.accalibrations['loadlinterm'][0]*(self.dispoff[0]-128) + \
                            self.calb.accalibrations['loadsqrterm'][0]*self.math.pow((self.dispoff[0]-128),2))
        self.acloadcalb.append(self.calb.accalibrations['loadconstterm'][1] + self.calb.accalibrations['loadlinterm'][1]*(self.dispoff[1]-128) + \
                            self.calb.accalibrations['loadsqrterm'][1]*self.math.pow((self.dispoff[1]-128),2))
        self.acloadcalb.append(self.calb.accalibrations['loadconstterm'][2] + self.calb.accalibrations['loadlinterm'][2]*(self.dispoff[2]-128) + \
                            self.calb.accalibrations['loadsqrterm'][2]*self.math.pow((self.dispoff[2]-128),2))
        
        self.modfact.append(self.calb.accalibrations['modcalfactor'][0])
        self.modfact.append(self.calb.accalibrations['modcalfactor'][1])
        self.modfact.append(self.calb.accalibrations['modcalfactor'][2])
#        print self.disprng
#        print self.dispoff
#        print self.dcdispcalb
#        print self.acdispcalb
#        print self.loadrng
#        print self.dcloadcalb
#        print self.acloadcalb
#        print self.modfact
    
    
    