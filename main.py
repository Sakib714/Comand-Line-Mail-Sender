import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login("sakibsadman546@gmail.com", "SAKIB@own@01")

server.sendmail("sakibsadman546@gmail.com", "sakibsadman546@gmail.com", 'mail send from my python code')

print('Mail Send')