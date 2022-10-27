import RPi.GPIO as GP
import time
import random

try:
    # led 핀 값을 리스트에 저장
    pin=[26, 16, 21, 20]
    GP.setmode(GP.BCM)
    # 핀 값을 받아와 setup 시킴
    map(lambda x: GP.setup(x, GP.OUT), pin)

    # led를 켰다 끄는 함수 정의
    def pinOut(pin):
        GP.output(pin,GP.HIGH)
        time.sleep(0.5)
        GP.output(pin,GP.LOW)
        time.sleep(0.5)
    
    # pin 리스트 섞기
    random.shuffle(pin)

    # pin 리스트 순서에 따라 핀 값을 받아와 pinOut함수 호출(10번)
    for i in range(0,10):
        pinOut(pin[i%4])
    
    # 핀 reset
    GP.cleanup()

except:
    # 핀 값을 받아와 모든 led 소등
    map(lambda x: GP.output(x,GP.LOW), pin)
    # 핀 reset
    GP.cleanup()