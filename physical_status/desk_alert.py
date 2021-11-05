from gpiozero import MotionSensor

#PIR data pin to BCM#21, +5v for power
pir = MotionSensor(21, sample_rate=1) 
#Best to turn PIR's SENSITIVITY DOWN and the DELAY UP

def flag1():
    flag = open('/path/to/your/flag', 'w')
    flag.write('1\n')
    flag.close()

def flag0():
    flag = open('/path/to/your/flag', 'w')
    flag.write('0\n')
    flag.close

while True:
    pir.wait_for_motion()
    flag1()
    pir.wait_for_no_motion()
    flag0()
