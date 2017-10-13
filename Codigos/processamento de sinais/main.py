# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""
while True:

    
    from pygame import mixer
    from time import sleep
    
    from scanner import Scanner
    
    mixer.init()
    mixer.music.load('F:\car_alarm_short.mp3')
    
    sample_rate = 2.048e6
    gain = 49.6
    
    scn = Scanner(sample_rate,gain)
    
    center_freq = 433.9e6
    thresh = 10
    scn.start_monitor_psd_until(center_freq,thresh,monit="MAX")
    print('apertado!')
    #while True:
    #    x=scn.start_monitor_psd(center_freq,256,10,monit="MEAN")
    #    sleep(0.2)
    #    print('apertado!')
    
    #mixer.music.play()
    