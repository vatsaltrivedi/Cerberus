# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:21:38 2013

@author: Vatsal
"""
import calibration_constant as calbcons
class calculator:
    def __init__(self,data,calbvalue):
        self.data = data
        self.calbvalue = calbvalue

    Time = []
    ZDispR3 = []
    ZDispR3Zeroed = []
    ZDispTotal = []
    XDispR3=[]
    XDispR3Zeroed=[]
    XDisp=[]
    YDispR3=[]
    YDispR3Zeroed=[]
    YDisp=[]
    ZDispZeroed=[]
    XDispZeroed =  []
    YDispZeroed = []
    TimeZeroed = []
    ZAmplitude = []
    ZForce = []
    ZLoadV  = []
    ZLoadZeroed = []
    ZLoadmN = []
    ZLoadCorrectedforKls = []
    RawZPhase = []
    CorrectedZPhase  = []
    COSZPhase = []
    FXCosPHI = []
    FXCosPHIkmw2 = []
    ZStiffness = []
    ZPS2  = []
    XAmplitude = []
    YAmplitude  = []
    XForce  = []
    YForce  = []
    ZFX = []
    XFX = []
    YFX = []
    XHarmonic_F_for_Const_XQuasistatic_ZForce = []
    YHarmonic_F_for_Const_XQuasi_static_ZForce = []
    Raw_X_Phase = []
    Corrected_X_Phase = []
    COS_X_Phase=[]
    Raw_Y_Phase = []
    Corrected_Y_Phase =[]
    COS_Y_Phase = []
    XFX_CosPHI=[]
    XFX_CosPHIkmw2 = []
    XStiffness = []
    YFx_CosPHI = []
    YFx_CosPHIkmw2 = []
    YStiffness =  []
    XPS2 = []
    YPS2 =  []
    X_SinPHI = []
    XFX_SinPHI = []
    XFX_SinPHIciw = []
    CwS_XAxis = []
    Y_SinPHI=[]
    YFX_SinPHI = []
    YFX_SinPHI_ciw=[]
    CwS_YAxis = []
    
    
    zero_disp_z = 0
    zero_disp_x = 0
    zero_disp_y = 0
    zero_time = 0
    zero_load = 0    
    load_for_kls = []
    disp_for_kls = []
    
    def reset(self):
        self.Time = []
        self.ZDispR3 = []
        self.ZDispR3Zeroed = []
        self.ZDispTotal = []
        self.XDispR3=[]
        self.XDispR3Zeroed=[]
        self.XDisp=[]
        self.YDispR3=[]
        self.YDispR3Zeroed=[]
        self.YDisp=[]
        self.ZDispZeroed=[]
        self.XDispZeroed =  []
        self.YDispZeroed = []
        self.TimeZeroed = []
        self.ZAmplitude = []
        self.ZForce = []
        self.ZLoadV  = []
        self.ZLoadZeroed = []
        self.ZLoadmN = []
        self.ZLoadCorrectedforKls = []
        self.RawZPhase = []
        self.CorrectedZPhase  = []
        self.COSZPhase = []
        self.FXCosPHI = []
        self.FXCosPHIkmw2 = []
        self.ZStiffness = []
        self.ZPS2  = []
        self.XAmplitude = []
        self.YAmplitude  = []
        self.XForce  = []
        self.YForce  = []
        self.ZFX = []
        self.XFX = []
        self.YFX = []
        self.XHarmonic_F_for_Const_XQuasistatic_ZForce = []
        self.YHarmonic_F_for_Const_XQuasi_static_ZForce = []
        self.Raw_X_Phase = []
        self.Corrected_X_Phase = []
        self.COS_X_Phase=[]
        self.Raw_Y_Phase = []
        self.Corrected_Y_Phase =[]
        self.COS_Y_Phase = []
        self.XFX_CosPHI=[]
        self.XFX_CosPHIkmw2 = []
        self.XStiffness = []
        self.YFx_CosPHI = []
        self.YFx_CosPHIkmw2 = []
        self.YStiffness =  []
        self.XPS2 = []
        self.YPS2 =  []
        self.X_SinPHI = []
        self.XFX_SinPHI = []
        self.XFX_SinPHIciw = []
        self.CwS_XAxis = []
        self.Y_SinPHI=[]
        self.YFX_SinPHI = []
        self.YFX_SinPHI_ciw=[]
        self.CwS_YAxis = []        
    
    def avg(self,dataset):
        total = 0
        for i in range(0,len(dataset)):
            total = total + dataset[i]
        avg = total/len(dataset)
        return avg
    def slope(self,x,y):
        meanX = self.avg(x)
        meanY = self.avg(y)
        num = 0
        den = 0
        for i in range(1,len(x)):
            num = num + (x[i]-meanX)*(y[i]-meanY)
            den = den + (x[i]-meanX)**2
        
        return num/den
        
    def calculate(self):
        
        import math
        from scipy import stats
        calb = calbcons.calbcons()
        self.Time.append(0)
        
        maxlen = len(self.data.Time)
        for i in range(1, maxlen):
            self.Time.append(self.data.Time[i]-self.data.Time[1])
            
        maxlen = len(self.data.ZDisp)
        for i in range(0, maxlen):
            self.ZDispR3.append(self.data.ZDisp[i]-5- self.calbvalue.dispoff[0]*10 -(self.calbvalue.disprng[0]+1)*10000)
        
        maxlen = len(self.ZDispR3)
        for i in range(0, maxlen):
            self.ZDispR3Zeroed.append(self.ZDispR3[i]-self.ZDispR3[0])
        
        maxlen = len(self.ZDispR3Zeroed)
        for i in range(0, maxlen):
            self.ZDispTotal.append(self.ZDispR3Zeroed[i]*self.calbvalue.dcdispcalb[0]/math.pow(2,self.calbvalue.disprng[0]))
            
        maxlen = len(self.data.XDisp)
        for i in range(0, maxlen):
            self.XDispR3.append(self.data.XDisp[i]- 5- self.calbvalue.dispoff[1]*10 -(self.calbvalue.disprng[1]+1)*10000)
        
        maxlen = len(self.XDispR3)
        for i in range(0, maxlen):
            self.XDispR3Zeroed.append(self.XDispR3[i]-self.XDispR3[0])
        
        maxlen = len(self.XDispR3Zeroed)
        for i in range(0, maxlen):
            self.XDisp.append(self.XDispR3Zeroed[i]*self.calbvalue.dcdispcalb[1]/math.pow(2,self.calbvalue.disprng[1]))
        
        maxlen = len(self.data.YDisp)
        for i in range(0, maxlen):
            self.YDispR3.append(self.data.YDisp[i]-5- self.calbvalue.dispoff[2]*10 -(self.calbvalue.disprng[2]+1)*10000)
        
        maxlen = len(self.YDispR3)
        for i in range(0, maxlen):
            self.YDispR3Zeroed.append(self.YDispR3[i]-self.YDispR3[0])
        
            
        maxlen = len(self.YDispR3Zeroed)
        for i in range(0, maxlen):
            self.YDisp.append(self.YDispR3Zeroed[i]*self.calbvalue.dcdispcalb[2]/math.pow(2,self.calbvalue.disprng[2]))
        
            
        zero = int(round(len(self.ZDispR3)/2))
        
        self.zero_disp_z = self.ZDispTotal[zero]
        self.zero_disp_x = self.XDisp[zero]
        self.zero_disp_y = self.YDisp[zero]
        self.zero_time = self.Time[zero]
        
#        print self.zero_disp_z 
#        print self.zero_disp_x 
#        print self.zero_disp_y 
#        print self.zero_time 
        maxlen = len(self.ZDispTotal)
        for i in range(0, maxlen):
            self.ZDispZeroed.append(self.ZDispTotal[i] - self.zero_disp_z)
        
        maxlen = len(self.XDisp)
        for i in range(0, maxlen):
            self.XDispZeroed.append(self.XDisp[i] - self.zero_disp_x)
        
        maxlen = len(self.YDisp)
        for i in range(0, maxlen):
            self.YDispZeroed.append(self.YDisp[i] - self.zero_disp_y)
        
        maxlen = len(self.Time)
        for i in range(0,maxlen):    
            self.TimeZeroed.append(self.Time[i]-self.zero_time)
        
        maxlen = len(self.data.ZAmp)
        for i in range(0, maxlen):
            self.ZAmplitude.append(self.data.ZAmp[i]*self.calbvalue.acdispcalb[0]/math.pow(2,self.calbvalue.disprng[0]))
        
        self.ZForce.append(self.data.ZExcite[0]*calb.accalibrations['loadconstterm'][0]*calb.accalibrations['modcalfactor'][0])  
        
        maxlen = len(self.data.ZExcite)
        for i in range(1, maxlen):
            self.ZForce.append(self.data.ZExcite[i] * self.calbvalue.modfact[0]* self.calbvalue.acloadcalb[0])
       
        maxlen = len(self.data.ZLoad)
        for i in range(0, maxlen):
            self.ZLoadV.append(self.data.ZLoad[i] - (self.calbvalue.loadrng[0]+1)*10 - 5)
        
        self.zero_load = self.ZLoadV[zero]        
        maxlen = len(self.ZLoadV)
        for i in range(0, maxlen):
            self.ZLoadZeroed.append(-(self.ZLoadV[i]-self.zero_load))
    
        maxlen = len(self.ZLoadZeroed)
        for i in range(0, maxlen):
            self.ZLoadmN.append(self.ZLoadZeroed[i]*self.calbvalue.dcloadcalb[0]/1000)

        self.load_for_kls = self.ZLoadmN[1:86]
        self.disp_for_kls = self.ZDispZeroed[1:86]
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.disp_for_kls,self.load_for_kls)
        
        maxlen = len(self.ZLoadmN)
        for i in range(0, maxlen):
            self.ZLoadCorrectedforKls.append(self.ZLoadmN[i] - slope *self.ZDispZeroed[i])
        
        maxlen = len(self.data.ZPha)
        for i in range(0, maxlen):
            self.RawZPhase.append(self.data.ZPha[i])
        
        maxlen = len(self.RawZPhase)
        for i in range(0, maxlen):
            self.CorrectedZPhase.append(self.RawZPhase[i] - (-0.0844*125-0.0596))
        
        maxlen = len(self.CorrectedZPhase)
        for i in range(0, maxlen):
            self.COSZPhase.append(math.cos(self.CorrectedZPhase[i]*math.pi/180))
        
        maxlen = len(self.ZForce)
        for i in range(0, maxlen):
            self.FXCosPHI.append(self.ZForce[i]/self.ZAmplitude[i] * math.cos(self.CorrectedZPhase[i]*math.pi/180)*1000)
        
        maxlen = len(self.FXCosPHI)
        for i in range(0, maxlen):
            self.FXCosPHIkmw2.append(self.FXCosPHI[i] - calb.dccalibrations['springconstterm'][0]-calb.accalibrations['massofindenter'][0]*2*math.pi*125)
       
        
        
        maxlen = len(self.FXCosPHIkmw2)
        for i in range(0,maxlen):
            self.ZStiffness.append(self.FXCosPHIkmw2[i]-1/calb.accalibrations['loadframestiff'][0])
            
#        maxlen = len(self.ZStiffness)
#        for i in range(0, maxlen):
#            self.ZPS2.append(self.ZLoadCorrectedforKls[i]/ self.ZStiffness[i]/self.ZStiffness/1000)
#        
#        maxlen = len(self.data.XAmp)
#        for i in range(0, maxlen):
#            self.XAmplitude.append(self.data.XAmp[i]*self.calbvalue.acdispcalb[1]/math.pow(2,self.disprng[1]))
#        
#        maxlen = len(self.data.YAmp)
#        for i in range(0,maxlen):
#            self.YAmplitude.append(self.data.YAmp[i]* self.calbvalue.acdidpcalb[2]/math.pow(2, self.disprng[2]))
#            
#        maxlen = len(self.data.XExc)
#        for i in range(0,maxlen):
#            self.XForce.append(self.data.XExc[i] * self.calbcons.accalibrations['loadconstterm'][1] * self.calbcons.accalibrations['modcalfactor'][1])
#            
#        
#        maxlen = len(self.data.YExc)
#        for i in range(0,maxlen):
#            self.YForce.append(self.data.YExc[i] * self.calbcons.accalibrations['loadconstterm'][2] * self.calbcons.accalibrations['modcalfactor'][2])
#        maxlen = len(self.ZForce)
#        for i in range(0,maxlen):
#            self.ZFX = []
        self.XFX = []
        self.YFX = []
        self.XHarmonic_F_for_Const_XQuasistatic_ZForce = []
        self.YHarmonic_F_for_Const_XQuasi_static_ZForce = []
        self.Raw_X_Phase = []
        self.Corrected_X_Phase = []
        self.COS_X_Phase=[]
        self.Raw_Y_Phase = []
        self.Corrected_Y_Phase =[]
        self.COS_Y_Phase = []
        self.XFX_CosPHI=[]
        self.XFX_CosPHIkmw2 = []
        self.XStiffness = []
        self.YFx_CosPHI = []
        self.YFx_CosPHIkmw2 = []
        self.YStiffness =  []
        self.XPS2 = []
        self.YPS2 =  []
        self.X_SinPHI = []
        self.XFX_SinPHI = []
        self.XFX_SinPHIciw = []
        self.CwS_XAxis = []
        self.Y_SinPHI=[]
        self.YFX_SinPHI = []
        self.YFX_SinPHI_ciw=[]
        self.CwS_YAxis = []  
        
    def printdata(self):
        maxlen = len(self.ZDispR3)
        for i in range(0,maxlen):
            #print '%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\t%4f\n'%(self.ZDispR3[i], \
            #    self.ZDispR3Zeroed[i], self.ZDispTotal[i], self.XDispR3[i],self.XDispR3Zeroed[i], self.XDisp[i], self.YDispR3[i], \
            #    self.YDispR3Zeroed[i], self.YDisp[i], self.ZDispZeroed[i], self.XDispZeroed[i], self.YDispZeroed[i] , self.TimeZeroed[i] , \
            #    self.ZAmplitude[i], self.ZForce[i], self.ZLoadV[i], self.ZLoadZeroed[i], self.ZLoadmN[i], self.ZLoadCorrectedforKls[i])
            print '%4f\t%4f\t%4f\t%4f\t%4f\t%4f'%(self.RawZPhase[i], self.CorrectedZPhase[i], self.COSZPhase[i], self.FXCosPHI[i], \
                    self.FXCosPHIkmw2[i], self.ZStiffness[i])
            
        
        
            
    
        
    
