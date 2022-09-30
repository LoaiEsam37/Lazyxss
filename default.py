import time
import multiprocessing
from multiprocessing import Process
import os
import requests
import sys
from colorama import Fore
import socket
import getpass
import argparse
import re
# Import files
import ByPassTester.ByPassTester as ByPassTester
import LFI.LFI as LFI
import Reflected_XSS.Reflected_XSS as Reflected_XSS
import Stored_XSS.Stored_XSS as Stored_XSS
import WayBackUrlsSedFilter.WayBackUrlsSedFilter as WayBackUrlsSedFilter
import UniqOnly.UniqOnly as UniqOnly
import SedFilter.SedFilter as SedFilter
import WayBackUrls.WayBackUrls as WayBackUrls

def DEFAULT():
	# print title
	print(
		Fore.LIGHTGREEN_EX+
		" _                   __  ______ ____\n"+
		"| |    __ _ _____   _\ \/ / ___/ ___|\n"+
		"| |   / _` |_  / | | |\  /\___ \___ \\\n"+
		"| |__| (_| |/ /| |_| |/  \ ___) |__) |\n"+
		"|_____\__,_/___|\__, /_/\_\____/____/\n"+
		"                |___/\n"
	)
	# DEFAULT
	while True:
		print(
			Fore.LIGHTGREEN_EX +
			"\n            ( Pre-Scanning )                             ( Scanner )\n"+
			"+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"+
			"|   [ * ] 1  -->  WayBackUrls             |   [ * ] 5  -->  URL Reflected XSS         |\n"+
			"|   [ * ] 2  -->  SedFilter               |   [ * ] 6  -->  Inputs Reflected XSS      |\n"+
			"|   [ * ] 3  -->  WayBackUrls&SedFilter   |   [ * ] 7  -->  ByPassTester              |\n"+
			"|   [ * ] 4  -->  UniqOnly                |   [ * ] 8  -->  LFI                       |\n"+
			"+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"+
			"\n"
			)
		USER = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")

		if USER == "1":
			print(f"{Fore.WHITE}[ OK ] (WayBackUrls) selected{Fore.BLUE}")
			WayBackUrls.START()
		elif USER == "2":
			print(f"{Fore.WHITE}[ OK ] (SedFilter) selected{Fore.BLUE}")
			SedFilter.START()
		elif USER == "3":
			print(f"{Fore.WHITE}[ OK ] (WayBackUrls&SedFilter) selected{Fore.BLUE}")
			WayBackUrlsSedFilter.START()
		elif USER == "4":
			print(f"{Fore.WHITE}[ OK ] (UniqOnly) selected{Fore.BLUE}")
			UniqOnly.START()
		elif USER == "5":
			print(f"{Fore.WHITE}[ OK ] (URL Reflected XSS) selected{Fore.BLUE}")
			Reflected_XSS.START()
		elif USER == "6":
			print(f"{Fore.WHITE}[ OK ] (Inputs Reflected XSS) selected{Fore.BLUE}")
			Stored_XSS.START()
		elif USER == "7":
			print(f"{Fore.WHITE}[ OK ] (ByPassTester) selected{Fore.BLUE}")
			ByPassTester.START()
		elif USER == "8":
			print(f"{Fore.WHITE}[ OK ] (LFI) selected{Fore.BLUE}")
			LFI.START()
		else:
			print(f"{Fore.RED}[ ! ] Invaild option")
