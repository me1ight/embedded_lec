import RPi.GPIO as GPIO
import time

SW = [5, 6, 13, 19]
cur = [0, 0, 0, 0]
F = [261, 294, 330, 391]
BUZZER = 12

def mel(f, n):
    if(n == 1):
        p.start(50)
        p.ChangeFrequency(f)
    elif(n==0):
        p.stop()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
for i in range(0, 4):
    GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
p = GPIO.PWM(BUZZER, 261)

try:
    while True:
        for i in range(0, 4):
            cur[i] = GPIO.input(SW[i])
            if(cur[i] == 1):
                mel(F[i], 1)
                while(GPIO.input(SW[i]) == 1): continue
            mel(0, 0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

