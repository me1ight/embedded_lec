import threading
import serial
import RPi.GPIO as GPIO
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

PWM_ = [18, 23]
IN_ = [22, 27, 25, 24]
num = {0: [0, 1, 0, 1], 1:[0, 1, 0, 0], 2: [0, 0, 0, 1], 3: [1, 0, 1, 0], 4: [0, 0, 0, 0]}

gData = ""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in range(0, 4):
    if i < 2 :
        GPIO.setup(PWM_[i], GPIO.OUT)
        globals()["L_Motor{}".format(i)] = GPIO.PWM(PWM_[i],500)
        globals()["L_Motor{}".format(i)].start(0)
    GPIO.setup(IN_[i], GPIO.OUT)


def G_S(n):
    if n==[0,0,0,0]:
        for i in range(0, 2):
            globals()["L_Motor{}".format(i)].ChangeDutyCycle(0)
    else:
        for i in range(0, 4):
            GPIO.output(IN_[i], n[i])
            if i < 2:
                globals()["L_Motor{}".format(i)].ChangeDutyCycle(50)

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def main():
    global gData
    try:
        while True:
            if gData.find("go") >= 0:
                gData = ""
                G_S(num[0])
                print("ok go")
            elif gData.find("back") >= 0:
                gData = ""
                G_S(num[3])
                print("ok back")
            elif gData.find("left") >= 0:
                gData = ""
                G_S(num[2])
                print("ok left")
            elif gData.find("right") >= 0:
                gData = ""
                G_S(num[1])
                print("ok right")
            elif gData.find("stop") >= 0:
                gData = ""
                G_S(num[4])
                print("ok stop")

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()