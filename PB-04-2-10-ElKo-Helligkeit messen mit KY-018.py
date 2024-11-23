#==========================================================================
#
# PB-4-2-10-ElKo-Helligkeit messen mit KY-018.py
#
# 1 KY-018, LDR / Fotowiderstands Modul mit analogem Ausgang
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, ADC
from utime import sleep

# Soll-Wert, ab wann Tag sein soll
soll_wert = 30000

# Initialisierung des ADC0
ldr = ADC(2)

# Initialiseren des GPIO
led = Pin(25, Pin.OUT, value=0)

# Wiederholung
while True:
    # ADC als Dezimalzahl lesen
    read = ldr.read_u16()
    # Ausgabe in der Kommandozeile/Shell
    print("ADC: ", read)
    # EIN und AUS
    if read > soll_wert:
        led.on()
    else:
        led.off()
    # Warten
    sleep(1)