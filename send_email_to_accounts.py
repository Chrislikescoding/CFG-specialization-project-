# both need to be installed as packages
import yagmail
import keyring

import calendar
import datetime

# this section of code relies on storing the password for a dummy gmail account in a keyring
# this worked finne on windows but does not work in MAC Os where I am now testing my project
# the date is retrieved, then the sender,receiver ,subject,contents and attachment (i.e.
# this months edited claim records)are set. Account password is retrieved from the key ring,
# then yagmail sends the email oth passwords are FGpymiles.
# The password can be set using the setup_yagmail_passwword snippet

currentDate = datetime.date.today()
lastDayOfMonth = datetime.date(currentDate.year, currentDate.month,
                               calendar.monthrange(currentDate.year, currentDate.month)[1])

# password CFGpymiles at yahoo.com password CFGpymiles
sender = 'cbelle.sharpe@gmail.com'
# password CFGpymiles at yahoo.com password CFGpymiles
receiver = 'accountspymiles.com@yahoo.com '
subject = 'this is a test'
contents = "is this working, here is your expense report'  /extracted_data..csv"
attachments = '/extracted_data.csv'

temp_password = keyring.get_password("system", "username")
keyring.set_password("system", "username", temp_password)

yag = yagmail.SMTP(user=sender, password=temp_password)
yag.send(to=receiver, subject =subject, contents=contents, attachments='/extracted_data.csv')
print("Email sent")
