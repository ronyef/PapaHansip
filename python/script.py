__author__ = 'ronyefendy'

import webiopi
import datetime

GPIO = webiopi.GPIO

# Definisikan GPIO

# GPIO Motor Kiri
L1 = 22
L2 = 23

# GPIO Motor Kanan
R1 = 24
R2 = 25


# Fungsi-fungsi Motor Kiri

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)


def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)


def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)


# Fungsi-fungsi Motor Kanan

def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R1, GPIO.LOW)


def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)


def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R1, GPIO.HIGH)


# Definisi macro untuk JavaScript

def go_forward():
    left_forward()
    right_forward()


def go_backward():
    left_backward()
    right_backward()


def turn_left():
    left_backward()
    right_forward()


def turn_right():
    right_backward()
    left_forward()


def stop():
    left_stop()
    right_stop()


# Inisialisasi

# Setup GPIO

GPIO.setFunction(L1, GPIO.OUT)
GPIO.setFunction(L2, GPIO.OUT)
GPIO.setFunction(R1, GPIO.OUT)
GPIO.setFunction(R2, GPIO.OUT)


# Membuat Web Server
# server = webiopi.Server(port=8000, login="hansip", password="hansip")

# Mendaftarkan Macro untuk dipanggil di JS
server.addMacro(go_forward)
server.addMacro(go_backward)
server.addMacro(turn_right)
server.addMacro(turn_left)
server.addMacro(stop)


#Looping program Web Server
webiopi.runLoop()

# Mematikan program Web Server
server.stop()

# Atur ulang fungsi GPIO
GPIO.setFunction(L1, GPIO.IN)
GPIO.setFunction(L2, GPIO.IN)
GPIO.setFunction(L3, GPIO.IN)
GPIO.setFunction(L4, GPIO.IN)


