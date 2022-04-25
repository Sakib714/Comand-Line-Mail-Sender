import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(mail_address, password)

server.sendmail(from_mail_address, to_mail_address, mail_text)

print('Mail Send')
