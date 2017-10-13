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

class Scanner(object):
    
    def __init__(self,sample_rate,gain):
        self.sdr = RtlSdr()

        # configure device
        self.sdr.sample_rate = sample_rate
        self.sdr.gain = gain
    
    def plot_psd(self,fc,samp_scale=256):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc

        samples = self.sdr.read_samples(samp_scale*1024)

        # use matplotlib to estimate and plot the PSD
        psd(samples, NFFT=1024, Fs=self.sdr.sample_rate/1e6, \
            Fc=self.sdr.center_freq/1e6)
        xlabel('Frequency (MHz)')
        ylabel('Relative power (dB)')

        show()
        
    def calc_psd(self,fc,samp_scale=256):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc

        smpls = self.sdr.read_samples(samp_scale*1024)

        # use matplotlib to estimate and plot the PSD
        f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
        
        f = f + fc
        
        pow_db = 10*np.log10(pow_sd)
        pow_db = pow_db - np.min(pow_db)
        
        return f, pow_db
    
    
    async def monitor_psd(self,fc,samp_scale,count_max,monit):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc
        count = 0
        print(1)
        
        async for smpls in self.sdr.stream():
            count = count + 1
            
            f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
            
            pow_db = 10*np.log10(pow_sd)
            pow_db = pow_db - np.min(pow_db)
            
            #if monit == "MAX":
            #    print(np.max(pow_db))
            #elif monit == "MEAN":
            #print(np.max(pow_db))
            if np.max(pow_db)>10:
                return 1
            
            #if count > count_max:
            #    self.sdr.stop()   
        #print('done!')        
        #self.sdr.close()
        
    async def monitor_psd_until(self,fc,thresh,samp_scale,monit):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc
        
        async for smpls in self.sdr.stream():
            f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
            
            pow_db = 10*np.log10(pow_sd)
            pow_db = pow_db - np.min(pow_db)
            
            if monit == "MAX":
                val = np.max(pow_db)
            elif monit == "MEAN":
                val = np.mean(pow_db)
                
            #print(val)
                
            if val > thresh:
                self.sdr.stop()
                
        self.sdr.close()
        #print("Threshold reached!")
        
    def start_monitor_psd(self,fc,samp_scale = 256,count_max=10,monit = "MAX"):
        asy.get_event_loop().run_until_complete(self.monitor_psd(fc,\
                          samp_scale,count_max,monit))
        
    def start_monitor_psd_until(self,fc,thresh,samp_scale = 256,monit = "MAX"):
       return  asy.get_event_loop().run_until_complete(self.monitor_psd_until(fc,\
                          thresh,samp_scale,monit))