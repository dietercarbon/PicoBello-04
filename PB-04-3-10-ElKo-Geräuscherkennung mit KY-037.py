#==========================================================================
#
# PB-4-3-10-ElKo-Geräuscherkennung mit KY-037.py
#
# 1 KY-037 Hochempfindliches Mikrofon
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, ADC
from time import sleep

# Initialisierung des ADC0 (GPIO26)
sensor_a = ADC(1)

# Initialisierung von GPIO22 als Eingang
sensor_d = Pin(5, Pin.IN)

# Wiederholung (Endlos-Schleife)
while True:
    value_a = sensor_a.read_u16()
    print('ADC:', value_a)
    value_d = sensor_d.value()
    print('IO:', value_d)
    print()
    sleep(0.1)