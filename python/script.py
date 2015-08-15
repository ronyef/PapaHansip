__author__ = 'ronyefendy'

import webiopi
import datetime

GPIO = webiopi.GPIO

LIGHT = 17  #GPIO menggunakan BCM number

HOUR_ON = 8     # nyalakan di jam 08:00
HOUR_OFF = 18   # matikan di jam 18:00

# fungsi setup yang otomatis dipanggil oleh WebIOPi
def setup():
    # set GPIO
    GPIO.setFunction(LIGHT, GPIO.OUT)

    # ambil datetime
    now = datetime.datetime.now()

    # test apakah kita di ON time
    if (now.hour >= HOUR_ON) and (now.hour < HOUR_OFF):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)

#fungsi loop
def loop():
    # ambil datetime
    now = datetime.datetime.now()

    # toggle light ON ketika waktu ON
    if (now.hour == HOUR_ON and now.minute == 0) and (now.second == 0):
        if GPIO.digitalRead(LIGHT) == GPIO.LOW:
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    # toggle light OFF
    if (now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0):
        if GPIO.digitalRead(LIGHT) == GPIO.HIGH:
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # loop delay
    webiopi.sleep(1)

# destroy saat shutdown
    GPIO.digitalWrite(LIGHT, GPIO.LOW)

# Macros di bawah ini
@webiopi.macro
def getLightHours():
    return "%d;%d" % (HOUR_ON, HOUR_OFF)

@webiopi.macro
def setLightHours(on, off):
    global HOUR_ON, HOUR_OFF
    HOUR_ON = int(on)
    HOUR_OFF = int(off)
    return getLightHours()

