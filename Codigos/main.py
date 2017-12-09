# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Bruno
"""

import scanner

morse={'01': 'a','1000': 'b','1010': 'c','100': 'd','0': 'e','0010': 'f',
       '110': 'g','0000': 'h','00': 'i','0111': 'j','101': 'k','0100': 'l',
       '11': 'm','10': 'n','111': 'o','0110': 'p','1101': 'q','010': 'r',
       '000': 's','1': 't','001': 'u','0001': 'v','011': 'w','1001': 'x',
       '1011': 'y','1100': 'z','01111': '1','00111': '2','00011': '3','00001': '4',
       '00000': '5','10000': '6','11000': '7','11100': '8','11110': '9','11111': '0',}

#simbolos é a string de traços e pontos
simbolos=''

def proc_sinais():

    #x é a letra em questão
    x=''
    global simbolos
    import scanner
       
    #inicialização
    sample_rate = 2.048e6
    gain = 49.6
    
    scn = scanner.Scanner(sample_rate,gain)
    
    center_freq = 433.9e6
    
    scn.start_monitor_psd(center_freq)
    
    if scanner.flag[0]==1:
        for i in range(len(scanner.lista)):
            if scanner.lista[i]<0.6:
                simbolos=simbolos+'0'
            else:
                simbolos=simbolos+'1'
        try:
            x=morse[simbolos]
        except:
            x='erro!'
        scanner.lista=[]
        simbolos=''
        scanner.flag[0]=0
        
        scanner.letras=scanner.letras+x
        print(x, end='')
        
    return x    

                 
while True:
   proc_sinais()       
    