import yagmail #install package
import keyring #install package

import calendar
import datetime


currentDate = datetime.date.today()
lastDayOfMonth = datetime.date(currentDate.year, currentDate.month, calendar.monthrange(currentDate.year, currentDate.month)[1])

print(currentDate)
print(lastDayOfMonth)
currentDate = datetime.date.today()
lastDayOfMonth = datetime.date(currentDate.year, currentDate.month, calendar.monthrange(currentDate.year, currentDate.month)[1])

print(currentDate)
print(lastDayOfMonth)
sender = 'cbelle.sharpe@gmail.com'
#receiver = 'fmwijtmhvvsrepsudg@kvhrw.com'
receiver = 'accountspymiles.com@yahoo.com ' #password CFGpymiles at yahoo.com password CFGpymiles
subject='this is a test'
contents = "is this working, here is your expense report'  /first.csv"
attachments = '/first.csv'
#my_password =
temp_password= keyring.get_password("system", "username")
keyring.set_password("system", "username", temp_password)

print(keyring.get_password("system", "username"))

yag = yagmail.SMTP(user=sender, password=temp_password)
yag.send(to=receiver, subject =subject, contents=contents,attachments ='first.csv')


print("Email sent")
