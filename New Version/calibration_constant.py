# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:33:02 2013

@author: Vatsal
"""
class calbcons:
    dccalibrations = {};
    accalibrations = {};
    
    
    ## DC Calibrations    
    
    dccalibrations['dispconstterm']=[9944.3,18506,11091]                        ##DC displacement constant term Z,X amd Y
     
    dccalibrations['displinterm']=[2.0903,4.8506,1.6121]                        ##DC displacement linear term Z,X amd Y
     
    dccalibrations['dispsqrterm']=[-0.3789,-0.5316,-0.26013]                    ##DC displacement square term Z,X amd Y
     
    dccalibrations['loadconstterm']=[47624,43313,58032]                         ##DC Load Constant Term Z,X amd Y
     
    dccalibrations['loadlinterm']=[8.0558,21.588,3.5987]                        ##DC Load Linear Term Z,X amd Y
     
    dccalibrations['loadsqrterm']=[0.003,0.0067645,0.00064854]                  ##DC Load Squared Term Z,X amd Y
         
    dccalibrations['springconstterm']=[230,207,204]                             ##DC Spring Constant term Z,X amd Y
     
    dccalibrations['springlinterm']=[0.0055042];                                ##DC Sprning Linear Term  Z
                                
    dccalibrations['springsqtermr']=[-0.010195];                                ##DC Sprning Square Term Z
                                
    dccalibrations['springcubterm']=[0.0000177];                                ##DC Sprning Cube Term Z
     
     
    dccalibrations['rng0']=[1,1,1]                        
    dccalibrations['rng1']=[2,2,2]                         
    dccalibrations['rng2']=[4,4,4]                         
    dccalibrations['rng3']=[8,8,8]                                              ## DC Gains Z,X amd Y
    dccalibrations['rng4']=[16,16,16]                       
    dccalibrations['rng5']=[32,32,32]                        
    dccalibrations['rng6']=[64,64,64]                       
    dccalibrations['rng7']=[128,128,128]                      
     
    dccalibrations['dclf']=[220000,220000,220000]                               ##DC Load Frame Stiffness Z,X amd Y//
    
    ## AC Calibrations    
    
    accalibrations['dispconstterm']=[9935.9,18509,11088]                        ##AC displacement constant term Z,X amd Y
     
    accalibrations['displinterm']=[2.0639,4.8118,1.6513]                        ##AC displacement linear term Z,X amd Y
     
    accalibrations['dispsqrterm']=[-0.37801,-0.53142,-0.26013]                  ##AC displacement square term Z,X amd Y
     
    accalibrations['loadconstterm']=[14023.5,12767,17098]                       ##AC Load Constant Term Z,X amd Y
     
    accalibrations['loadlinterm']=[2.36,6.4062,1.1621]                          ##AC Load Linear Term Z,X amd Y
     
    accalibrations['loadsqrterm']=[-0.0002,0.0019054,-0.0013593]                ##AC Load Squared Term Z,X amd Y
     
    accalibrations['modcalfactor']=[0.0000000115050282231,0.0000000115050282231\
                                    ,0.0000000115050282231]                     ##AC modcal factor Z,X amd Y
     
    accalibrations['massofindenter']=[0.000165,0.000145,0.00014];               ##mass of indenter  Z,X amd Y
                                
    accalibrations['dcconstterm']=[0.019, 0.0066396, 0.017396];                 ##AC Damping coeffecient constant term Z,X amd Y
                                
    accalibrations['dclinterm']=[0.0000026058, 0, 0.0000026058];                ##AC Damping coeffecient linear term Z,X amd Y
     
    accalibrations['dcsqrterm']=[0.0000079439, 0,0.0000079439];                 ##AC Damping coeffecient squared term Z,X amd Y
    
    accalibrations['dccubeterm']=[-0.0000000034583, 0, -0.0000000034583];       ##AC Damping coeffecient cube term Z,X amd Y
    
    accalibrations['dcquadterm']=[0.0000000030961, 0, 0.0000000030961];         ##AC Damping coeffecient quad term Z,X amd Y
    
    accalibrations['loadframestiff'] = [130000,21200,25800]
    
      
