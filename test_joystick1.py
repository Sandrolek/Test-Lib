import RTCjoystick
import time

J = RTCjoystick.Joystick()
J.connect("/dev/input/js0")
J.info()
J.start()

LastX = 0

while True:
#тестируем стики
    J.Axis.get('z')
    x = J.Axis.get('x')
    if LastX == x:
        pass
    else:
        print(x)
    LastX = x

#тестируем кнопки
#    btn = J.Buttons.get('b')
#    print(btn)

    time.sleep(0.1)

J.exit()
