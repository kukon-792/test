
import smtplib

smtObj=smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login('kukon11674@gmail.com','password')
smtObj.sendmail("miah.devops@gmail.com","kukon11673@gmail.com", 'Subject: SMTP check. \n This is a test email')
smtObj.quit()


