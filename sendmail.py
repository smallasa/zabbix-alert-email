#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import sys

def send_email(email_content, to_email , email_title):
    msg = MIMEText( email_content, _subtype = 'html', _charset = 'utf8')
    msg['From'] = 'sos <' + user_name + '>'
    msg['Subject'] = '%s' % email_title

    try:
        s = smtplib.SMTP_SSL(smtp_server,465)

        s.login(user_name,user_passwd)

        s.sendmail(user_name,to_email,msg.as_string())

        s.close()
    except Exception as e:
        print 'Exception: ', e


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(0)

    smtp_server = 'smtp.exmail.qq.com'
    user_name   = 'xxxx@brandwisdom.cn'
    user_passwd = 'xxxx`'

    to_email_address = sys.argv[1].split(",")
    to_message_head  = sys.argv[2]
    to_message_body  = sys.argv[3]

    send_email(to_message_body,to_email_address,to_message_head)
