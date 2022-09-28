import multiprocessing
from multiprocessing import Process
import os
import requests
from colorama import Fore
import re
import sys
import time
import socket
import getpass

def START():
	while True:
		# file OR manually
		print(f"{Fore.LIGHTGREEN_EX}[ * ] 1  -->  file\n[ * ] 2  -->  manually")
		USER = input(f"{Fore.WHITE}{getpass.getuser()}@DNSploit$ ")
		if USER == "1":
			# INPUT
			URL = METHOD.File()
			# OUTPUT
			OUTPUT = Output_File()
			# EXEC
			print(f"{Fore.WHITE}[ * ] Loading...")
			EXEC.CommandList(URL, OUTPUT)
			print(f"{Fore.WHITE}[ OK ] Done")
			os.system("rm tmp.txt")
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
			os.system("rm tmp.txt")
			break
		else:
			print(f"{Fore.RED}[ ! ] Invaild Option")

class METHOD:

	def File():
		# FILEPATH
		while True:
			print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for targets :- ")
			FILEPATH = input(f"{Fore.WHITE}{getpass.getuser()}@DNSploit$ ")
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
			URL = input(f"{Fore.WHITE}{getpass.getuser()}@DNSploit$ ")
			try:
				try:
					requests.get(f"{URL}")
				except:
					try:
						requests.get(f"https://{URL}")
					except:
						requests.get(f"http://{URL}")
				print(f"{Fore.WHITE}[ OK ] Vaild")
				break
			except:
				print(f"{Fore.RED}[ ! ] Not Vaild, try again")
		return URL

def Output_File():
	# OUTPUT
	while True:
		print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the output")
		OUTPUT = input(f"{Fore.WHITE}{getpass.getuser()}@DNSploit$ ")
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
        tmp = "tmp.txt"
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
                os.system(f"echo \{str(URL[i])} | waybackurls >> {tmp}")
                print(f"\r[ OK ] ({URL[i]}) Done")
            except:
                pass
        
        os.system(f"cat {tmp} |grep -v 'jpg\|jpeg\|png\|svg' |sed 's/=.*/=/g' | uniq >> {OUTPUT}")
        f = open(f"{os.getcwd()}/{OUTPUT}", "r")
        read = re.split("\n", str(f.read()))
        f = open(f"{os.getcwd()}/{OUTPUT}","w")
        for i in range(len(read)):
                if re.search("=", read[i]):
                        f = open(f"{os.getcwd()}/{OUTPUT}", "a")
                        f.writelines(read[i])
                        f.writelines("\n")
                        f.close()
                else:
                        pass



    def Command(URL, OUTPUT):
        # WayBackUrls
        os.system(f"echo \{URL} | waybackurls >> {OUTPUT}")
        temp = "tmp.txt"
        os.system(f"cat {OUTPUT} |grep -v 'jpg\|jpeg\|png\|svg' |sed 's/=.*/=/g' | uniq >> {temp}")
        f = open(f"{os.getcwd()}/{temp}", "r")
        read = re.split("\n", str(f.read()))
        f = open(f"{os.getcwd()}/{temp}","w")
        for i in range(len(read)):
            if re.search("=", read[i]):
                f = open(f"{os.getcwd()}/{temp}", "a")
                f.writelines(read[i])
                f.writelines("\n")
                f.close()
            else:
                pass
        f = open(f"{os.getcwd()}/{temp}", "r")
        final = re.split("\n", str(f.read()))
        f = open(f"{os.getcwd()}/{OUTPUT}", "w")
        for i in range(len(final)):
            f = open(f"{os.getcwd()}/{OUTPUT}", "a")
            f.writelines(final[i])
            f.writelines("\n")       


def FINAL_LIST(URL, OUTPUT):
	print(f"{Fore.WHITE}[ * ] Loading...")
	EXEC.CommandList(URL, OUTPUT)
	print(f"{Fore.WHITE}[ OK ] Done")
	os.system("rm tmp.txt")
		
def FINAL_ONE(URL, OUTPUT):
	print(f"{Fore.WHITE}[ * ] Loading...")	
	EXEC.Command(URL, OUTPUT)
	print(f"{Fore.WHITE}[ OK ] Done")
	os.system("rm tmp.txt")
