import smtplib as smtp

server=smtp.SMTP_SSL("smtp.gmail.com",465)
server.login('phani.pothineni@gmail.com','@1270@phanipothineni') #
server.sendmail("phani.pothineni@gmail.com","paneendrap@gmail.com",'Hello How are you ?')
server.quit()

# for gmail need to allow security...
#Go to Google's Account Security Settings: www.google.com/settings/security
#Access for less secure apps". Set it to "Allowed".