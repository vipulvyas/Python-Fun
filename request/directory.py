#!/usr/bin/python

import requests
from termcolor import colored

def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		print("error For connection")
		pass

target_url = raw_input("[*] Enter target Url With http and Whithout /: ")
file_dir = raw_input("[*] Enter the file for Bruteforce: ")

file = open(file_dir,"r")
for line in file:
	word = line.strip()
	
	full_url = target_url + "/" +word
	response = request(full_url)
	if response:
		print(colored("[+]Discovered Directory At This Link: "+ full_url,'green'))
	else:
		print(colored("[-]Can not Discovered Directory At This Link: "+ full_url,'red'))

