import RPi.GPIO as GP
import time

# led 핀 값을 리스트에 저장
pin=[26, 16, 21, 20]

GP.setmode(GP.BCM)
# 핀 값을 받아와 setup 시킴
map(lambda x: GP.setup(x, GP.OUT), pin)

# led를 켰다 끄는 함수 정의
def pinOut(pin):
    GP.output(pin,GP.HIGH)
    time.sleep(1.0)
    GP.output(pin,GP.LOW)
    time.sleep(1.0)

# while문을 이용해 함수 무한 반복
while True:
    # 핀 값을 받아와 pinOut함수 호출
    map(lambda x: pinOut(x), pin)