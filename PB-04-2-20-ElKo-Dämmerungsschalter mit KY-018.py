#==========================================================================
#
# PB-4-2-20-ElKo-Dämmerungsschalter mit KY-018.py
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
    print()
    print("ADC: ", read)
    # EIN und AUS
    if read > soll_wert:
        led.on()
        print("größer ",soll_wert,", also Nacht")
    else:
        led.off()
        print("kleiner ",soll_wert,", also Tag")
    # Warten
    sleep(1)