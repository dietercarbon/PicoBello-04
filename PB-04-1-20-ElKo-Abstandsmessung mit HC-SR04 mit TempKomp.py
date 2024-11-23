#==========================================================================
#
# PB-4-1-20-ElKo-Abstandsmessung mit HC-SR04 mit TempKomp.py
#
# 1 HC-SR501 PIR-Sensor
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, ADC
from utime import sleep, sleep_us, ticks_us

# Initialisierung GPIO-Ausgang für Trigger-Signal
trigger = Pin(16, Pin.OUT)

# Initialisierung GPIO-Eingang für Echo-Signal
echo = Pin(17, Pin.IN)

# Initialisierung des ADC4 (Temperatursensor)
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

# Wiederholung (Endlos-Schleife)
while True:
    # Spannung messen und in Temperatur umrechnen
    read = sensor_temp.read_u16()
    spannung = read * conversion_factor
    temperatur = 27 - (spannung - 0.706) / 0.001721
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
    # Abstand/Entfernung mit Temperatur-Korrektur
    abstand_korr = timepassed * (331.3 + 0.606 * temperatur) / 10000 / 2
    # Ergebnis ausgeben
    print('  Temp.:', str("%.1f" % temperatur), '°C')
    print('    Off:', signaloff)
    print('     On:', signalon)
    print('   Zeit:', timepassed)
    print('Abstand:', str("%.2f" % abstand), 'cm')
    print('  Korr.:', str("%.2f" % abstand_korr), 'cm')
    print()
    # 3 Sekunde warten
    sleep(3)