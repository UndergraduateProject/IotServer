from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import smtplib
import random


def sendmail(mail):
    password = random.randint(0, 10000)
    password = '%04d' % password
    content = MIMEMultipart()
    content["subject"] = "Mail testing"
    content["from"] = "undergraduateIotFarm@gmail.com"
    content["to"] = mail

    template = Template(Path("utils/mail_template.html").read_text())
    body = template.substitute({"password": password})
    content.attach(MIMEText(body, "html"))

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("undergraduateIotFarm@gmail.com",
                       "nvfxzatrwqixvogm")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            return password

        except Exception as e:
            return False
