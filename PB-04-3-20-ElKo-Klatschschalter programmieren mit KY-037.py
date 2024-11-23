#==========================================================================
#
# PB-4-3-20-ElKo-Klatschschalter programmieren mit KY-037.py
#
# 1 KY-037 Hochempfindliches Mikrofon
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin
from time import sleep

# Initialisierung der Onboard-LED
device = Pin(25, Pin.OUT, value=0)

# Initialisierung von GPIO22 als Eingang
sensor = Pin(5, Pin.IN)

# Wiederholung (Endlos-Schleife)
while True:
    if sensor.value() == 1:
        device.toggle()
        sleep(0.5)
    sleep(0.1)