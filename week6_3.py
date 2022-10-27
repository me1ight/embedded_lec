import RPi.GPIO as GPIO
import time

#속도 입력핀
PWM_ = [18, 23]
#방향 입력핀
IN_ = [22, 27, 25, 24]
#스위치 입력핀
SW = [5, 6, 13, 19]
#스위치 현재 상태
cur = [0, 0, 0, 0]
#입력받은 스위치에 따른 핀 방향 설정
num = {0: [0, 1, 0, 1], 1:[0, 1, 0, 0], 2: [0, 0, 0, 1], 3: [1, 0, 1, 0]}
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in range(0, 4):
    #속도 제어 핀 값 setup
    if i < 2 :
        GPIO.setup(PWM_[i], GPIO.OUT)
        globals()["L_Motor{}".format(i)] = GPIO.PWM(PWM_[i],500)
        globals()["L_Motor{}".format(i)].start(0)
    #방향 제어 핀 값 setup
    GPIO.setup(IN_[i], GPIO.OUT)
    #스위치 핀 값 setup
    GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#방향 및 속도 제어 함수
def G_S(n, N): #(방향, 속도)
    for i in range(0, 4):
        #num 딕셔너리를 활용해 각 핀의 방향 설정
        GPIO.output(IN_[i], n[i])
        if i < 2 :
            if N == 0:
                #50%로 동작
                globals()["L_Motor{}".format(i)].ChangeDutyCycle(50)
            elif N == 1:
                #정지
                globals()["L_Motor{}".format(i)].ChangeDutyCycle(0)

try:
    while True:
        for i in range(0, 4):
            #스위치의 현재 상태 저장
            cur[i] = GPIO.input(SW[i])
            #스위치가 눌린 경우 판별
            if(cur[i] == 1):
                #방향 및 속도 제어 함수 호출
                G_S(num[i], 0)
                #스위치 출력
                print("SW{} click".format(i+1))
                #스위치 눌린 동안 무한 반복
                while(GPIO.input(SW[i]) == 1): continue
            #방향 및 속도 제어 함수 호출
            G_S(num[i], 1)

except KeyboardInterrupt:
    pass

#핀 reset
GPIO.cleanup()