#==========================================================================
#
# PB-4-2-32-ElKo-Lichtschranke mit LED und KY-018 Kali.py
#
# 1 KY-018, LDR / Fotowiderstands Modul mit analogem Ausgang
# 1 LED mit Vorwiderstand
#
#==========================================================================
#
# Bibliotheken laden
from machine import ADC, Pin
from utime import sleep

# Initialisierung des ADC0
ldr = ADC(2)

# Initialiserung GPIO16 für LED
led = Pin(16, Pin.OUT, value=0)

# Kalibrierung des Schwellwerts
print('Kalibrierung')

# Messung: Helligkeit, wenn LED aus (Unterbrechung)
valueOff = ldr.read_u16()
print('Schaltschwelle bei Unterbrechung:', valueOff)

# LED einschalten
led.on()
sleep(1)

# Messung: Helligkeit, wenn LED an (Normal)
valueOn = ldr.read_u16()
print('Schaltschwelle wenn LED an:', valueOn)

# Berechnung: Schwellwert
threshold = int(valueOff + (valueOn - valueOff) / 2)
print('Berechneter Schwellwert:', threshold)
print('Kalibrierung beendet')

# Unterbrechung (0/1)
interrupt = 0

# Dauer der Unterbrechung
count = 0

# Wiederholung (Endlos-Schleife)
while True:
    # ADC als Dezimalzahl lesen
    value = ldr.read_u16()
    # ADC-Wert ausgeben
    #print('ADC:', value)
    # ADC-Wert auswerten
    if value > threshold:
        interrupt = 1
        count = count + 1
    else:
        interrupt = 0
        count = 0
    # Erste Unterbrechung erkannt
    if count == 1:
        print('Unterbrechung')
    # Zähler ausgeben
    if count > 0:
        print('Zähler:', count)
    # Warten
    sleep(0.1)