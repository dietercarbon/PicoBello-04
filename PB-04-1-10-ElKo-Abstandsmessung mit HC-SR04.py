#==========================================================================
#
# PB-4-1-10-ElKo-Abstandsmessung mit HC-SR04.py
#
# 1 HC-SR501 PIR-Sensor
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin
from utime import sleep, sleep_us, ticks_us

# Initialisierung GPIO-Ausgang für Trigger-Signal
trigger = Pin(16, Pin.OUT)

# Initialisierung GPIO-Eingang für Echo-Signal
echo = Pin(17, Pin.IN)

# Wiederholung (Endlos-Schleife)
while True:
    # Abstand messen
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    # Zeitmessungen
    while echo.value() == 0:
       signaloff = ticks_us()
    while echo.value() == 1:         
       signalon = ticks_us()
    # Vergangene Zeit ermitteln
    timepassed = signalon - signaloff
    # Abstand/Entfernung ermitteln
    # Entfernung über die Schallgeschwindigkeit (34320 cm/s bei 20 °C) berechnen
    # Durch 2 teilen, wegen Hin- und Rückweg
    abstand = timepassed * 0.03432 / 2
    # Ergebnis ausgeben
    print('    Off:', signaloff)
    print('     On:', signalon)
    print('   Zeit:', timepassed)
    print('Abstand:', str("%.2f" % abstand), 'cm')
    print()
    # 3 Sekunde warten
    sleep(3)