#==========================================================================
#
# PB-4-3-40-ElKo-Lärmampel mit KY-037.py
#
# 1 KY-037 Hochempfindliches Mikrofon
# 1 rote LED mit Vorwiderstand
# 1 gelbe LED mit Vorwiderstand
# 1 grüne LED mit Vorwiderstand
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, ADC
from time import sleep

# Lautstärke-Werte (0 - 65535)
value_ok = 34000
value_nok = 36000

# Initialiserung der GPIOs für die Ampel
red = Pin(13, Pin.OUT, value=0)
yellow = Pin(14, Pin.OUT, value=0)
green = Pin(15, Pin.OUT, value=0)

# Initialiserung der GPIOs für den Summer
buz = Pin(8, Pin.OUT, value=0)

# Initialisierung des ADC0 (GPIO26)
sensor = ADC(0)

# Funktion, wenn Lautstärke OK
def sound_ok():
    red.off()
    yellow.off()
    green.on()

# Funktion, wenn Lautstärke nicht OK
def sound_nok():
    red.off()
    yellow.on()
    green.off()

# Funktion, wenn Lautstärke zu laut
def sound_alarm():
    red.on()
    yellow.off()
    green.off()
    buz.on()
    sleep(1)
    buz.off()

# Wiederholung (Endlos-Schleife)
while True:
    value = sensor.read_u16()
    print(value)
    if (value < value_ok):
        sound_ok()
    elif (value < value_nok):
        sound_nok()
    else:
        sound_alarm()
    sleep(1)