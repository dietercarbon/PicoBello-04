#==========================================================================
#
# PB-4-2-40-ElKo-Helligkeit einer LED mit Fotowiderstand regeln.py
#
# 1 KY-018, LDR / Fotowiderstands Modul mit analogem Ausgang
# interne LED
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, PWM, ADC
from utime import sleep

# Korrekturwert
korrektur = 4

# Initialisierung des ADC0
ldr = ADC(2)

# Initialisierung von GPIO25 als PWM-Ausgang
led = PWM(Pin(25))

# PWM-Einstellung: Frequenz in Hertz (Hz)
led.freq(1000)

# Wiederholung
while True:
    # ADC als Dezimalzahl lesen
    read = ldr.read_u16()
    print()
    print('ADC-Wert :', read)
    # Korrektur
    value = int(read / korrektur)
    print('Korrektur:', value)
    # LED-Helligkeit regeln
    led.duty_u16(value)
    # Warten
    sleep(0.1)