# !/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
from time_and_warning import time_comparison, emil_sender
from datetime import datetime

if time_comparison() == 1:
    cam = cv2.VideoCapture(0)
    run_once = 0
    screen = 0
    while cam.isOpened():
        ret, frame = cam.read()
        ret2, frame2 = cam.read()
        #porównywanie obrazu z kamer
        diff = cv2.absdiff(frame, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

        gausian_filter = (5, 5)
        blur = cv2.GaussianBlur(gray, gausian_filter, 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # oznaczanie ramką wykryte obiekty
        for c in contours:
            if cv2.contourArea(c) < 6500:
                continue

            #robienie ramki
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (101, 51, 102), 2)
            #finded beep

            if run_once == 0:
                # emil_sender()
                name_jpg = 'Frame' + str(screen) + '.jpg'
                cv2.imwrite(name_jpg, frame)
                emil_sender(name_jpg)
                # winsound.Beep(500, 200)
                run_once += 1
                screen += 1

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        cv2.imshow('Secure camera', frame)
else:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Camera works only in 22:00-06:00, its", current_time)