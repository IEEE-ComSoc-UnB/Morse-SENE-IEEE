# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""

morse={'01': 'a','1000': 'b','1010': 'c','100': 'd','0': 'e','0010': 'f',
       '110': 'g','0000': 'h','00': 'i','0111': 'j','101': 'k','0100': 'l',
       '11': 'm','10': 'n','111': 'o','0110': 'p','1101': 'q','010': 'r',
       '000': 's','1': 't','001': 'u','0001': 'v','011': 'w','1001': 'x',
       '1011': 'y','1100': 'z','01111': '1','00111': '2','00011': '3','00001': '4',
       '00000': '5','10000': '6','11000': '7','11100': '8','11110': '9','11111': '0',}
simbolos=''
def proc_sinais():
    while True:
    
        
        from pygame import mixer
        
        import scanner
        
        #mixer.init()
        #mixer.music.load('F:\car_alarm_short.mp3')
        
        sample_rate = 2.048e6
        gain = 49.6
        
        scn = scanner.Scanner(sample_rate,gain)
        
        center_freq = 433.9e6
        thresh = 10
        scn.start_monitor_psd(center_freq)
        #print('apertado!')
        #for i in scanner.lista:
        #    print('{}\n'.format(i))
        
        if scanner.flag[0]==1:
            for i in range(len(scanner.lista)):
                if i%2==0:
                    if scanner.lista[i]<0.5:
                        simbolos=simbolos+'0'
                    #if (i==0) and (scanner.lista[i]<0.5):
                    #    simbolos=simbolos+'0'
                    #elif (scanner.lista[i-1]>0.05) and (scanner.lista[i]<0.5):
                    #    simbolos=simbolos+'0'
                    else:
                        simbolos=simbolos+'1'
            #print('simbolos é: '+simbolos)
            try:
                x= morse[simbolos]
                #print(morse[simbolos], end='')
            except:
                x= 'erro!'
                #print('erro!')
            #for i in range(int(len(simbolos)/3)):         
            #    if simbolos[3*i:3*i+3]=='000':
            #        print('s')
            #    elif simbolos[3*i:3*i+3] =='111':
            #        print('o')
            #    else:
            #        print('deu merda')
            scanner.lista=[]
            simbolos=''
            scanner.flag[0]=0
            return x
                     
        
    #del scn
    #while True:
    #    x=scn.start_monitor_psd(center_freq,256,10,monit="MEAN")
    #    sleep(0.2)
    #    print('apertado!')
    
    #mixer.music.play()
    