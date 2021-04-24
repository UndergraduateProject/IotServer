from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import smtplib

def sendmail(mail):
    content = MIMEMultipart()  
    content["subject"] = "Mail testing"  
    content["from"] = "undergraduateIotFarm@gmail.com" 
    content["to"] = mail

    template = Template(Path("utils/mail_template.html").read_text())
    body = template.substitute({ "password": "123123" }) 
    content.attach(MIMEText(body, "html"))

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("undergraduateIotFarm@gmail.com", "nvfxzatrwqixvogm")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)