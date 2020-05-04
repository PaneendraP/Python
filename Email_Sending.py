import smtplib as smtp

server=smtp.SMTP_SSL("smtp.gmail.com",465)
server.login('sender_Email','sender_password') 
server.sendmail("From","To",'Message here')
server.quit()

# for gmail need to allow security...
#Go to Google's Account Security Settings: www.google.com/settings/security
#Access for less secure apps". Set it to "Allowed".
