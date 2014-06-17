import smtplib

fromaddr = 'asaf12@gmail.com'
toaddrs  = 'asaf12@gmail.com'
msg = 'Testing this out'


# Credentials (if needed6  
username = 'asaf12'
password = 'bepresent'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()