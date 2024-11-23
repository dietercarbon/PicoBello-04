#==========================================================================
#
# PB-4-1-40-ElKo-Anwesenheitserkennung mit HC-SR04 auf 1602.py
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

# Display-Zeilen ausgeben
lcd.putstr('Hello World')

# Funktion: Anwesenheit erkennen
def distance_measure():
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    while echo.value() == 0:
       signaloff = ticks_us()
    while echo.value() == 1:         
       signalon = ticks_us()
    timepassed = signalon - signaloff
    abstand = timepassed * 0.03432 / 2
    if abstand > 100:
        return 0
    else:
        return 1

# Funktion: Display-Steuerung
def display(timer):
    if distance_measure() == 0:
        lcd.backlight_off()
    else:
        lcd.backlight_on()

# Timer für die Display-Steuerung
tim = Timer(freq=0.5, mode=Timer.PERIODIC, callback=display)