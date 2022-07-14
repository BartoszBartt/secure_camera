#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

def time_comparison():
    now = datetime.now()
    #to pod testy
    now = now.replace(hour=5, minute=0, second=0, microsecond=0)
    current_time = now.strftime("%H:%M:%S")

    today_22pm = now.replace(hour=22, minute=0, second=0, microsecond=0)
    today_22pm = today_22pm.strftime("%H:%M:%S")

    today_6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
    today_6am = today_6am.strftime("%H:%M:%S")

    midnight_before = now.replace(hour=23, minute=59, second=59, microsecond=59)
    midnight_before = midnight_before.strftime("%H:%M:%S")

    midnight_after = now.replace(hour=00, minute=0, second=1, microsecond=1)
    midnight_after = midnight_after.strftime("%H:%M:%S")
    time.sleep(1)


    if current_time > today_22pm and current_time < midnight_before or current_time > midnight_after and current_time < today_6am:
        return True
    else:
        return False

def emil_sender(jpg):
    email_sender = 'qwsdgrwer123@gmail.com'
    email_reciver = 'qwsdgrwer123@gmail.com'
    email_password = 'sanfmkwqvoprwygt'

    subject = 'Camera found something!'

    body = """
    Check your house and area of the camera
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['Subject'] = subject
    em.set_content(body)

    with open(jpg, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    em.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    contex = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contex) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())

