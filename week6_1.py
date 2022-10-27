import RPi.GPIO as GPIO
import time

#스위치 핀 값 저장
SW = [5, 6, 13, 19]
#각 스위치별 상태 및 횟수 저장
last = [0, 0, 0, 0]
cur = [0, 0, 0, 0]
cnt = [0, 0, 0, 0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#핀 값을 받아와 setup 시킴
for i in range(0, 4):
    GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(0, 4):
            #스위치의 현재 상태 저장
            cur[i] = GPIO.input(SW[i])
            #스위치가 눌린 경우 판별
            if(cur[i] == 0 and last[i] == 1):
                #스위치 눌린 횟수 저장
                cnt[i] += 1
                #스위치 및 횟수 출력
                print("('SW{} click', {})".format(i+1, cnt[i]))
            #현재 상태를 이전 상태에 저장
            last[i] = cur[i]

except KeyboardInterrupt:
    pass

#핀 reset
GPIO.cleanup()

