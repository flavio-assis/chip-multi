#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from smtplib import SMTP
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from src.config import get_config
from src.logger import Logger


class Email:
    def __init__(self):
        self.server = SMTP('smtp.gmail.com', 587)
        self.user = ''
        self.user_key = ''

    def login(self):
        conf = get_config()
        self.user = conf['MAIL_USER']
        self.user_key = conf['MAIL_PASS']
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.user, self.user_key)

    def send_mail(self, to, subject, body, attachments=None):
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = ', '.join(to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachments is not None:
            for attachment in attachments:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment[1].read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename = ' + attachment[0])
                msg.attach(part)

        content = msg.as_string()
        try:
            self.server.sendmail(self.user, to, content)
        except Exception as error:
            logger = Logger()
            logger.send(f'An Error occurred while sending the mail! ERROR: {error}')
            sys.exit(6)

    def logout(self):
        self.server.quit()

