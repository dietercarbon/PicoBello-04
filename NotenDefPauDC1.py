from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(1))
buzzer.duty_u16(0)
duty=5000
Tonumfang=2
EndePause=0.05

def P(Dauer,Pause):
    buzzer.duty_u16(0)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)

def C5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(532)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def CS5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(554)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def D5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(587)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def DS5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(622)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def E5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(659)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def F5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(698)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def FS5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(740)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def G5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(784)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def GS5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(831)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def A5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(880)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def AS5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(932)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def B5(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(988)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def C6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1047)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def CS6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1109)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def D6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1175)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def DS6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1245)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def E6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1319)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def F6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1397)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def FS6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1480)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
def G6(Dauer,Pause):
    buzzer.duty_u16(duty)
    buzzer.freq(1568)
    sleep(Tonumfang/Dauer)
    buzzer.duty_u16(0)
    if Pause > 0:
        buzzer.duty_u16(0)
        sleep(EndePause)
    
