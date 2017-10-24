# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:06:19 2017

Code adapted from: https://pypi.python.org/pypi/pyrtlsdr

@author: Calil
"""

from pylab import psd, xlabel, ylabel, show
import scipy.signal as sig
from rtlsdr import RtlSdr
import numpy as np
import asyncio as asy
import time
import matplotlib.pyplot as plt

lista = []
t=[0]
flag=[0]
letras=''
class Scanner(object):
    
    def __init__(self,sample_rate,gain):
        self.sdr = RtlSdr()

        # configure device
        self.sdr.sample_rate = sample_rate
        self.sdr.gain = gain
    
    async def monitor_psd(self,fc,samp_scale,count_max,monit):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc
        x=0
        
        global letras
        global lista
        global flag
        global t
        
        async for smpls in self.sdr.stream():
            #print('\n'*100)
            #print(letras)
            
            f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
            
            pow_db = 10*np.log10(pow_sd)
            pow_db = pow_db - np.min(pow_db)
            #self.plot_psd(pow_db)
            #xlabel('Frequency (MHz)')
            #ylabel('Relative power (dB)')
            
            #show()
                
            
            
            if (np.max(pow_db)>20) and (x==0):
                x=1
                t[0]=time.time()
                #print(t)
            elif (np.max(pow_db)<20) and (x==1):
                lista.append(time.time()-t[0])
                t[0]=time.time()
                x=0
                self.sdr.stop()
            elif (time.time()-t[0]>2) and (lista!=[]) and (x==0):
                flag[0]=1
                self.sdr.stop()
            elif (time.time()-t[0]>5) and (x==1):
                letras=''
                lista=[]
                print('\n'*100)
                x=2
                self.sdr.stop()
            elif (np.max(pow_db)<20) and (x==2):
                x=0
                t[0]=time.time()
        self.sdr.close()    

        
    def start_monitor_psd(self,fc,samp_scale = 256,count_max=10,monit = "MAX"):
        #print('antes do return')
        return asy.get_event_loop().run_until_complete(self.monitor_psd(fc,\
                          samp_scale,count_max,monit))
