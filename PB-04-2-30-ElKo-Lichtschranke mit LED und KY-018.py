#==========================================================================
#
# PB-4-2-30-ElKo-Lichtschranke mit LED und KY-018.py
#
# 1 KY-018, LDR / Fotowiderstands Modul mit analogem Ausgang
# 1 LED mit Vorwiderstand
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, ADC
from utime import sleep

# Initialisierung von GPIO25 als Ausgang
led_onboard = Pin(25, Pin.OUT, value=0)

# Initialisierung des ADC0
ldr = ADC(2)

# Schwellwert bei Unterbrechung
threshold = 15000 # weiße LED
#threshold = 10000 # rote LED

# Funktion zur Alarmkontakt-Auswertung
print('Ich bin scharfgeschaltet!')
while True:
    # ADC als Dezimalzahl lesen
    value = ldr.read_u16()
    # ADC-Wert ausgeben
    print('ADC:', value)
    # ADC-Wert auswerten
    if value > threshold:
        break
    # Warten
    sleep(0.1)

# Alarm auslösen
led_onboard.on()
print('Alarm')
print('ADC:', value)