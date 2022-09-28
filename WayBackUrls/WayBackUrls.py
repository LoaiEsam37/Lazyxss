import os
import requests
from colorama import Fore
import re
import sys
import time
import socket
import getpass
import multiprocessing
from multiprocessing import Process
def START():
	while True:
		# file OR manually
		print(f"{Fore.LIGHTGREEN_EX}[ * ] 1  -->  file\n[ * ] 2  -->  manually")
		USER = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
		if USER == "1":
			# INPUT
			URL = METHOD.File()
			# OUTPUT
			OUTPUT = Output_File()
			# EXEC
			print(f"{Fore.WHITE}[ * ] Loading...")
			EXEC.CommandList(URL, OUTPUT)
			print(f"{Fore.WHITE}[ OK ] Done")
			break
		if USER == "2":
			# INPUT
			URL = METHOD.Manually()
			# OUTPUT
			OUTPUT = Output_File()
			# EXEC
			print(f"{Fore.WHITE}[ * ] Loading...")
			EXEC.Command(URL, OUTPUT)
			print(f"{Fore.WHITE}[ OK ] Done")
			break
		else:
			print(f"{Fore.RED}[ ! ] Invaild Option")

class METHOD:

	def File():
		# FILEPATH
		while True:
			print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for targets :- ")
			FILEPATH = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
			try:
				f = open(f"{os.getcwd()}/{FILEPATH}", "r")
				URL = re.split("\n", str(f.read()))
				print(f"{Fore.WHITE}[ OK ] Vaild")
				break
			except:
				print(f"{Fore.RED}[ ! ] Not Vaild, try again")
		return URL

	def Manually():
		# URL
		while True:
			print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the URL you want to scan :- ")
			URL = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
			try:
				try:
					requests.get(f"http://{URL}")
				except:
					try:
						requests.get(f"https://{URL}")
					except:
							requests.get(URL)
				print(f"{Fore.WHITE}[ OK ] Vaild")
				break
			except:
				print(f"{Fore.RED}[ ! ] Not Vaild, try again")
		return URL

def Output_File():
	# OUTPUT
	while True:
		print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the output")
		OUTPUT = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
		if OUTPUT == "":
					print(f"{Fore.RED}[ ! ] Not Vaild, try again")
		else:
			try:
				TRY = open(f"{os.getcwd()}/{OUTPUT}", "a")
				TRY.close()
				break
			except:
				print(f"{Fore.RED}[ ! ] Not Vaild, try again")
	return OUTPUT

class EXEC:

	def CommandList(URL, OUTPUT):
		for i in range(len(URL)):
			try:
				try:
					requests.get(f"http://{URL[i]}")
				except:
					try:
						requests.get(f"https://{URL[i]}")
					except:
							requests.get(URL[i])
				# WayBackUrls
				os.system(f"echo \{URL[i]} | waybackurls >> {OUTPUT}")
				print(f"\r{Fore.WHITE}[ OK ] ({URL[i]}) Done")
			except:
				pass

	def Command(URL, OUTPUT):
		# WayBackUrls
		os.system(f"echo \{URL} | waybackurls >> {OUTPUT}")

def FINAL_LIST(URL, OUTPUT):
	# EXEC
	print(f"{Fore.WHITE}[ * ] Loading...")
	EXEC.CommandList(URL, OUTPUT)
	print(f"{Fore.WHITE}[ OK ] Done")

def FINAL_ONE(URL, OUTPUT):
	# EXEC
	print(f"{Fore.WHITE}[ * ] Loading...")
	EXEC.Command(URL, OUTPUT)
	print(f"{Fore.WHITE}[ OK ] Done")
