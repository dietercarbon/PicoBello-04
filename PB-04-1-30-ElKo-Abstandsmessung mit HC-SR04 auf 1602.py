#==========================================================================
#
# PB-4-1-30-ElKo-Abstandsmessung mit HC-SR04 auf 1602.py
#
# 1 HC-SR501 PIR-Sensor
# 1 Alphanumerisches LCD 16x2 mit I2C Backpack
#
#==========================================================================
#
# Bibliotheken laden
from time import sleep, sleep_us, ticks_us
from machine import I2C, Pin, Timer
from machine_i2c_lcd import I2cLcd

# Initialisierung GPIO-Ausgang für Trigger-Signal
trigger = Pin(16, Pin.OUT)

# Initialisierung GPIO-Eingang für Echo-Signal
echo = Pin(17, Pin.IN)

# Initialisierung I2C
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)

# Initialisierung LCD über I2C
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Wiederholung (Endlos-Schleife)
while True:
    # Abstand messen
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    # Zeiten messen
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
    # Ergebnis auf Display ausgeben
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('Abstand:' + "\n" + str("%.2f" % abstand) + ' cm')
    # 2 Sekunde warten
    sleep(2)