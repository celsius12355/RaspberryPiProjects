'''
A simple Raspberry Pi buzzer project
implemented in Python in order to 
familiarize myself with the GPIO 
library and note frequencies.
May 15th 2020.
Jazmin Idhali Paz
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #using Broadcom GPIO numbers setup
GPIO.setwarnings(False)
BUZZER = 17 #buzzer connected to GPIO17, (PIN 11)
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       time.sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       time.sleep(halveWaveTime)

def play():
    t=0
    notes=[196,233,311,233,196,233,196,233,311,233,196,233,
208,262,349,262,208,262,208,262,349,262,208,262,
208,262,393,262,208,262,208,262,393,262,208,262,
233,294,392,294,233,294,233,294,392,294,233,294,
262,311,415,311,262,311,262,311,415,311,262,311,
262,349,415,349,262,349,262,349,415,349,262,349,
294,349,466,349,294,349,294,349,466,349,294,349,
294,349,466,349,294,349,294,349,466,349,294,349
]

    duration=[0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25,
0.5,0.25,0.5,0.25,0.5,0.25
]
    for n in notes:
        buzz(n, duration[t]/1.75) #sounds good at duration / 1.75
        time.sleep(duration[t] *0.1)
        t+=1


play()
