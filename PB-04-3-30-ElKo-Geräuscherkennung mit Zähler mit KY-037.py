#==========================================================================
#
# PB-4-3-30-ElKo-Geräuscherkennung mit Zähler mit KY-037.py
#
# 1 KY-037 Hochempfindliches Mikrofon
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, Timer
from time import sleep

# Initialisierung von GPIO22 als Eingang
sensor = Pin(5, Pin.IN)

# Zähler
count = 0

# Start
print('Bereit')
print()

# Funktion: Zähler
def release(Pin):
    #print('Ausgelöst')
    #print()
    if sensor.value() == 1:
        global count
        count = count + 1
        print('Zähler:', count)
        print()
    sleep(0.2)

# Interrupt für die Geräuscherkennung
sensor.irq(trigger=Pin.IRQ_RISING, handler=release)