from colorama import Fore
import re
import requests
import os
import sys
import time
import socket
import getpass
import multiprocessing
from multiprocessing import Process
# FIRST STEP
def USER_INPUT():
	# Func_Request
	while True:
		print(f"{Fore.LIGHTGREEN_EX}[ * ] Do you want to put a file or Type manually the Payloads")
		print("[ * ] 1 --> manually\n[ * ] 2 --> file")
		USER = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
		# manually
		if USER == "1":
			Func_Request = 1
			while True:
				print(f"{Fore.LIGHTGREEN_EX}[ * ] Type your Payload")
				PAYLOAD = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
				if PAYLOAD == "":
					print(f"{Fore.RED}[ ! ] Not Vaild, try again")
				else:
					try:
						print(f"{Fore.WHITE}[ OK ]", PAYLOAD)
						break
					except:
						print({Fore.RED}, "[ ! ] You may need to Put \\ before These Chars {\", \'}, try again")
			break
		# file
		elif USER == "2":
			Func_Request = 2
			while True:
				print(f"{Fore.LIGHTGREEN_EX}[ * ] Type your Payloads filepath")
				Payload_filepath = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
				try:
					f = open(f"{os.getcwd()}/{Payload_filepath}", "r")
					PAYLOAD = str(f.read())
					print(f"{Fore.WHITE}[ OK ] {Payload_filepath}")
					break
				except:
					print(f"{Fore.RED}[ ! ] Not Vaild, try again")
			break
		else:
			print(f"{Fore.RED}[ ! ] invaild option")
	# TARGETS
	while True:
		print(f"{Fore.LIGHTGREEN_EX}[ * ] Do you want to Put a file or Type manually the targets")
		print("[ * ] 1  -->  manually\n[ * ] 2  -->  file")
		USER = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
		if USER == "1":
			# maually
			while True:
				print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the Url (If you want to Put multiple Urls separate them with \\n)")
				TARGETS = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
				try:
					try:
						requests.get(TARGETS)
					except:
						try:
							requests.get(f"http://{TARGETS}")
							TARGETS = f"http://{TARGETS}"
						except:
							requests.get(f"https://{TARGETS}")
							TARGETS = f"https://{TARGETS}"
					URL = re.split( "\n", TARGETS)
					print(f"{Fore.WHITE}[ OK ]", TARGETS)
					break
				except:
					print(f"{Fore.RED}[ ! ] Not Vaild, try again")
					print(f"{Fore.RED}[ ! ] Make Sure to Put http:// , https://")
			break
		if USER == "2":
			# file
			while True:
				print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the input")
				TARGETS = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
				try:
					# choose file that contain urls
					file = open(f"{os.getcwd()}/{TARGETS}", "r")
					URL = re.split( "\n", str(file.read()))
					file.close()
					print(f"{Fore.WHITE}[ OK ]", TARGETS)
					break
				except:
					print(f"{Fore.RED}[ ! ] Not Vaild, try again")
			break
		else:
			print(f"{Fore.RED}[ ! ] Invaild Option")
	# FILEPATH
	while True:
		print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the output")
		FILEPATH = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
		try:
			TRY = open(f"{os.getcwd()}/{FILEPATH}", "a")
			TRY.close()
			print(f"{Fore.WHITE}[ OK ]", FILEPATH)
			break
		except:
			print(f"{Fore.RED}[ ! ] Not Vaild, try again")
	# DELAY
	while True:
		print(f"{Fore.LIGHTGREEN_EX}[ * ] Delay Time between every request")
		DELAY = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
		try:
			DELAY = float(DELAY)
			print(f"{Fore.WHITE}[ OK ] {DELAY} sec")
			break
		except:
			print(f"{Fore.RED}[ ! ] Not Vaild, try again")
	# Return User Input Values
	return URL, FILEPATH, PAYLOAD, DELAY, Func_Request

class Request():
	
	def PayloadList(URL, FILEPATH, PAYLOAD, DELAY):
		fail = 0 # Not vulnerable Website
		success = 0 # vulnerable Website
		print("---------------------------------------------")
		print("\n\n\n\n")
		print(f"{Fore.WHITE}")
		for i in range(len(URL)):
			try:	
				# Delay time between every request
				time.sleep(DELAY)
				# test payload
				test_Payload = "dnssploit"
				# send request with GET method
				result = requests.get(URL[i], test_Payload)
				# get Response
				status_code = result.status_code
				# clear 7 lines from console
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				# print to console
				print(
					f"URL No.: {success + fail} from {len(URL)} ; {int(((success+fail) / len(URL) * 100))}%\n"+
					f"Response: {status_code}\n"+
					f"vulnerable: {success}\n"+
					f"Not vulnerable: {fail}\n"+
					f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((((success + fail) * DELAY) + (success + fail)) / 60))} min\n"
					)
				# if Response = 200
				if status_code == 200:
					if re.search(test_Payload, str(result.content)):
						num = 0
						for j in range(len(PAYLOAD)):
							# Try the Payload
							try:
								# send request using GET method
								result = requests.get(URL[i], PAYLOAD[j])
								# Delay time between every request
								time.sleep(DELAY)
								# get response
								status_code = result.status_code
								# if Response = 200
								if status_code == 200:
									if re.search(PAYLOAD[j], str(result.content)):
									# Write vulnerable URL in the chose file
										f = open(f"{os.getcwd()}/{FILEPATH}", "a")
										f.writelines(URL[i])
										f.writelines("\n")
										success += 1
										num += 1
										break
									else:
										pass
								else:
									pass
							# handling Error : No WIFI or Wrong URL
							except:
								pass
						# check if payloads didn`t work
						if num == 0: fail += 1
						else: pass
					else:
						fail += 1
				else:
					fail += 1
			except:
				fail += 1
				# clear 7 lines from console
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				# print to console
				print(
					f"URL No.: {success + fail} from {len(URL)} ; {int(((success+fail) / len(URL) * 100))}%\n"+
					f"Response: ...\n"+
					f"vulnerable: {success}\n"+
					f"Not vulnerable: {fail}\n"+
					f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((((success + fail) * DELAY) + (success + fail)) / 60))} min\n"
					)
				
		# clear 7 lines from console
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		# print to console
		print(
			f"URL No.: {success + fail} from {len(URL)} ; {int(((success+fail) / len(URL) * 100))}%\n"+
			f"Response: ...\n"+
			f"vulnerable: {success}\n"+
			f"Not vulnerable: {fail}\n"+
			f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((((success + fail) * DELAY) + (success + fail)) / 60))} min\n"
			)
		# Done
		print(f"{Fore.LIGHTGREEN_EX}---------------------------------------------")

	def OnePayload(URL, FILEPATH, PAYLOAD, DELAY):
		fail = 0 # Not vulnerable Website
		success = 0 # vulnerable Website
		print("---------------------------------------------")
		print("\n\n\n\n\n")
		print(f"{Fore.WHITE}")
		for i in range(len(URL)):
			time.sleep(DELAY)
			try:
				# send request
				result = requests.get(URL[i], PAYLOAD)
				status_code = result.status_code
				# clear 7 lines from console
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				# print to console
				print(
					f"URL No.: {success + fail} from {len(URL)} ; {int(((success+fail) / len(URL) * 100))}%\n"+
					f"Response: {status_code}\n"+
					f"vulnerable: {success}\n"+
					f"Not vulnerable: {fail}\n"+
					f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((((success + fail) * DELAY) + (success + fail)) / 60))} min\n"
				)
				# if request response = 200
				if status_code == 200:
					if re.search(PAYLOAD, str(result.content)):
						f = open(f"{os.getcwd()}/{FILEPATH}", "a")
						f.writelines(URL[i])
						f.writelines("\n")
						success += 1
					else:
						fail += 1
				# if request response = 400, 401, ...etc
				else:
					fail += 1
			# handling Error : No WIFI or Wrong URL
			except:
				fail += 1
				# clear 7 lines from console
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[F")
				# print to console
				print(
					f"URL No.: {success + fail} from {len(URL)} ; {int(((success+fail) / len(URL) * 100))}%\n"+
					f"Response: {status_code}\n"+
					f"vulnerable: {success}\n"+
					f"Not vulnerable: {fail}\n"+
					f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((((success + fail) * DELAY) + (success + fail)) / 60))} min\n"
				)

		# clear 7 lines from console
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		# print to console
		print(
			f"URL No.: {success + fail} from {len(URL)} ; {int(((success+fail) / len(URL) * 100))}%\n"+
			f"Response: ...\n"+
			f"vulnerable: {success}\n"+
			f"Not vulnerable: {fail}\n"+
			f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((success + fail) / 60))} min\n"
		)
		# Done
		print(f"{Fore.LIGHTGREEN_EX}---------------------------------------------")

def START():
	URL, FILEPATH, PAYLOAD, DELAY, Func_Request = USER_INPUT()
	if Func_Request == 1:
		Request.OnePayload(URL, FILEPATH, PAYLOAD, DELAY)
	elif Func_Request == 2:
		Request.PayloadList(URL, FILEPATH, PAYLOAD, DELAY)
	else:
		pass

def FINAL_LIST(URL, FILEPATH, PAYLOAD, DELAY):
	Request.PayloadList(URL, FILEPATH, PAYLOAD, DELAY)

def FINAL_ONE(URL, FILEPATH, PAYLOAD, DELAY):
	Request.OnePayload(URL, FILEPATH, PAYLOAD, DELAY)
