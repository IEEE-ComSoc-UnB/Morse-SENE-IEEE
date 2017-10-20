# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""

simbolos=''
while True:

    
    from pygame import mixer
    
    import scanner
    
    mixer.init()
    mixer.music.load('F:\car_alarm_short.mp3')
    
    sample_rate = 2.048e6
    gain = 49.6
    
    scn = scanner.Scanner(sample_rate,gain)
    
    center_freq = 433.9e6
    thresh = 10
    scn.start_monitor_psd(center_freq)
    print('apertado!')
    for i in scanner.lista:
        print('{}\n'.format(i))
    
    if scanner.flag[0]==1:
        for i in range(len(scanner.lista)-1):
            if i%2==0:
                if scanner.lista[i]<1.5:
                    simbolos=simbolos+'0'
                else:
                    simbolos=simbolos+'1'
        if simbolos=='000':
            print('s')
        elif simbolos =='111':
            print('o')
        else:
            print('deu merda')
        scanner.lista=[0]
        simbolos=''
                 
    
    #del scn
    #while True:
    #    x=scn.start_monitor_psd(center_freq,256,10,monit="MEAN")
    #    sleep(0.2)
    #    print('apertado!')
    
    #mixer.music.play()
    