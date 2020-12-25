import smtplib
from email.mime.text import  MIMEText
msg=MIMEText("contenido es correo")

msg['subject']='Asunto del correo'
msg['From']='desdedonde@gmail.com'
msg['To']='haciadonde@gmail.com'
mailServer=smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('gnama476@gmail.com',"xxxxxxx")
mailServer.sendmail('keitagnama476@gmail.com','gnamakeita476@gmail.com', msg_as_string())
mailServer.close()