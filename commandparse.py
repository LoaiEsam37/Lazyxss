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
import multiprocessing
from multiprocessing import Process
# Import files
import ByPassTester.ByPassTester as ByPassTester
import LFI.LFI as LFI
import Reflected_XSS.Reflected_XSS as Reflected_XSS
import Stored_XSS.Stored_XSS as Stored_XSS
import WayBackUrlsSedFilter.WayBackUrlsSedFilter as WayBackUrlsSedFilter
import UniqOnly.UniqOnly as UniqOnly
import SedFilter.SedFilter as SedFilter
import WayBackUrls.WayBackUrls as WayBackUrls
import default as DEFAULT
from main import *
import all_xss as All_XSS


if bool(args.tool):
    USER = (args.tool).lower()
    # Print title
    print(
    Fore.LIGHTGREEN_EX+
    "    __                     _  ____________\n"+
    "   / /   ____ _____  __  _| |/ / ___/ ___/\n"+
    "  / /   / __ `/_  / / / / /   /\__ \\__  \\\n"+
    " / /___/ /_/ / / /_/ /_/ /   |___/ /__/ /\n"+
    "/_____/\__,_/ /___/\__, /_/|_/____/____/\n"+
    "                  /____/\n"
        )



    # WayBackUrls
    if USER == "waybackurls" or USER == "w":

        print(f"{Fore.WHITE}[ OK ] (WayBackUrls) selected")

        # Handling errors
        if bool(args.payloadsfilename):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in WayBackUrls")
            quit()
        elif bool(args.payload):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in WayBackUrls")
            quit()    

        # LIST URL
        if bool(args.file) and bool(args.output):				
            WayBackUrls.FINAL_LIST(FILEPATH, OUTPUT)

        # ONE URL
        elif bool(args.url) and bool(args.output):
            WayBackUrls.FINAL_ONE(URL, OUTPUT)

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output):
            print(f"{Fore.RED}[ ! ] You have to put input and output together")
            quit()

        else:
            WayBackUrls.START()



    # SedFilter
    elif USER == "sedfilter" or USER == "s":

        print(f"{Fore.WHITE}[ OK ] (SedFilter) selected")

        # Handling errors
        if bool(args.payloadsfilename):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in SedFilter")
            quit()
        elif bool(args.payload):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in SedFilter")
            quit()

        # LIST URL
        if bool(args.file) and bool(args.output):
            SedFilter.FINAL_LIST(FILEPATH, OUTPUT)

        # ONE URL
        elif bool(args.url) and bool(args.output):
            print(f"{Fore.RED}[ ! ] One url is not an option")
            quit()

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output):
            print(f"{Fore.RED}[ ! ] You have to put input and output together")
            quit()

        # Easy Selection
        else:
            SedFilter.START()



    # WayBackUrls&SedFilter
    elif USER == "waybackurls&sedfilter" or USER == "ws":

        print(f"{Fore.WHITE}[ OK ] (WayBackUrls&SedFilter) selected")

        # Handling errors
        if bool(args.payloadsfilename):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in WayBackUrls&SedFilter")
            quit()
        elif bool(args.payload):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in ByPassTester")
            quit()

        # LIST URL
        if bool(args.file) and bool(args.output):			
            WayBackUrlsSedFilter.FINAL_LIST(URL, OUTPUT)

        # ONE URL
        elif bool(args.url) and bool(args.output):
            WayBackUrlsSedFilter.FINAL_ONE(URL, OUTPUT)

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output):
            print(f"{Fore.RED}[ ! ] You have to put input and output together")
            quit()

        # Easy Selection
        else:
            WayBackUrlsSedFilter.START()



    # UniqOnly
    elif USER == "uniqonly" or USER == "u":

        print(f"{Fore.WHITE}[ OK ] (UniqOnly) selected")

        # Handling errors
        if bool(args.payloadsfilename):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in UniqOnly")
            quit()
        elif bool(args.payload):
            print(f"{Fore.RED}[ ! ] put a payload is not an option in UniqOnly")
            quit()

        # LIST URL
        if bool(args.file) and bool(args.output):
            UniqOnly.FINAL_LIST(FILEPATH, OUTPUT)
		
        # ONE URL
        elif bool(args.url) and bool(args.output):
            print(f"{Fore.RED}[ ! ] One url is not an option")
            quit()

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output):
            print(f"{Fore.RED}[ ! ] You have to put input and output together")
            quit()

        # Easy Selection
        else:
            UniqOnly.START()



	# Reflected_XSS
    elif USER == "url_reflected_xss" or USER == "r-xss":

        print(f"{Fore.WHITE}[ OK ] (URL Reflected XSS) selected")

        # LIST URL
        if bool(args.file) and bool(args.output):

            # LIST URL
            if bool(args.payload) or bool(args.payloadsfilename):
                Reflected_XSS.FINAL_LIST(URL, OUTPUT, PAYLOAD, DELAY)                

            # Handling errors
            else:
                print(f"{Fore.RED}[ ! ] you have to set payloads with (-p or -pf)")
                quit()			

        # ONE URL
        elif bool(args.url) and bool(args.output):

            # ONE URL
            if bool(args.payloadsfilename) or bool(args.payload):
                Reflected_XSS.FINAL_ONE(URL,OUTPUT, PAYLOAD, DELAY)

            # Handling errors
            else:
                print(f"{Fore.RED}[ ! ] you have to set payloads with (-p or -pf)")
                quit()

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output) or bool(args.payload) or bool(args.payloadsfilename) or bool(args.delay):
            print(f"{Fore.RED}[ ! ] You have to put input, output and payloads together")
            quit()

        # Easy Selection
        else:
            Reflected_XSS.START()



    # Stored_XSS
    elif USER == "input_reflected_xss" or USER == "s-xss":

        print(f"{Fore.WHITE}[ OK ] (Inputs reflected XSS) selected")

        # LIST URL
        if bool(args.file) and bool(args.output):

            # LIST URL
            if bool(args.payloadsfilename) or bool(args.payload):
                s = requests.Session()
                s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                Stored_XSS.FINAL(URL, OUTPUT, PAYLOAD, DELAY, s)

            # Handling errors
            else:
                print(f"{Fore.RED}[ ! ] you have to set payloads with (-p or -pf)")
                quit()			

        # ONE URL
        elif bool(args.url) and bool(args.output):

            if bool(args.payloadsfilename) or bool(args.payload):
                s = requests.Session()
                s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                Stored_XSS.FINAL(URL, OUTPUT, PAYLOAD, DELAY, s)
            else:
                print(f"{Fore.RED}[ ! ] you have to set payloads with (-p or -pf)")
                quit()

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output) or bool(args.payload) or bool(args.payloadsfilename) or bool(args.delay):
            print(f"{Fore.RED}[ ! ] You have to put input, output and payloads together")
            quit()

        # Easy Selection
        else:
            Stored_XSS.START()



    # ByPassTester
    elif USER == "bypasstester" or USER == "b":

        print(f"{Fore.WHITE}[ OK ] (ByPassTester) selected")

        # LIST URL
        if bool(args.file) and bool(args.output):

            # Handling errors
            if bool(args.payloadsfilename):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in ByPassTester")
                quit()
            elif bool(args.payload):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in ByPassTester")
                quit()
			
            # LIST URL
            URL = re.split("\n", str(f.read()))
            ByPassTester.FINAL(URL, OUTPUT, DELAY)

        # ONE URL
        elif bool(args.url) and bool(args.output):

            if bool(args.payloadsfilename):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in ByPassTester")
                quit()
            elif bool(args.payload):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in ByPassTester")
                quit()

            # ONE URL
            ByPassTester.FINAL(URL, OUTPUT, DELAY)

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output) or bool(args.payload) or bool(args.payloadsfilename) or bool(args.delay):
            print(f"{Fore.RED}[ ! ] You have to put input, output together")
            quit()

        # Easy Selection
        else:
            ByPassTester.START()



    # LFI
    elif USER == "lfi" or USER == "l":

        print(f"{Fore.WHITE}[ OK ] (LFI) selected")

        # List URL
        if bool(args.file) and bool(args.output):

            # Handling errors
            if bool(args.payloadsfilename):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in LFI")
                quit()
            elif bool(args.payload):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in LFI")
                quit()
			
            # LIST URL
            LFI.FINAL(URL, OUTPUT, DELAY)

        # ONE URL
        elif bool(args.url) and bool(args.output):

            # Handling errors
            if bool(args.payloadsfilename):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in LFI")
                quit()
            elif bool(args.payload):
                print(f"{Fore.RED}[ ! ] put a payload is not an option in LFI")
                quit()

            # ONE URL
            LFI.FINAL(URL, OUTPUT, DELAY)

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output) or bool(args.payload) or bool(args.payloadsfilename) or bool(args.delay):
            print(f"{Fore.RED}[ ! ] You have to put input, output together")
            quit()
        else:
            LFI.START()


    elif USER == "all_xss" or USER == "a-xss":
        if bool(args.file) and bool(args.output):

            # LIST URL
            if bool(args.payloadsfilename) or bool(args.payload):
                s = requests.Session()
                s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                All_XSS.START_PROGRAM(URL, OUTPUT, PAYLOAD, DELAY, s)

            # Handling errors
            else:
                print(f"{Fore.RED}[ ! ] you have to set payloads with (-p or -pf)")
                quit()			

        # ONE URL
        elif bool(args.url) and bool(args.output):

            if bool(args.payloadsfilename) or bool(args.payload):
                s = requests.Session()
                s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                All_XSS.START_PROGRAM(URL, OUTPUT, PAYLOAD, DELAY, s)
            else:
                print(f"{Fore.RED}[ ! ] you have to set payloads with (-p or -pf)")
                quit()

        # Handling errors
        elif bool(args.url) or bool(args.file) or bool(args.output) or bool(args.payload) or bool(args.payloadsfilename) or bool(args.delay):
            print(f"{Fore.RED}[ ! ] You have to put input, output and payloads together")
            quit()

        # Easy Selection
        else:
            print(f"{Fore.RED}[ ! ] This is not an option in all_xss")
            quit()

    # wrong tool selection
    else:
        print(f"{Fore.RED}[ ! ] Invaild option")


else:
	if bool(args.payloadsfilename) or bool(args.payload) or bool(args.file) or bool(args.url) or bool(args.output) or bool(args.delay):
		# Print title
		print(
			Fore.LIGHTGREEN_EX+
			"    __                     _  ____________\n"+
			"   / /   ____ _____  __  _| |/ / ___/ ___/\n"+
			"  / /   / __ `/_  / / / / /   /\__ \\__  \\\n"+
			" / /___/ /_/ / / /_/ /_/ /   |___/ /__/ /\n"+
			"/_____/\__,_/ /___/\__, /_/|_/____/____/\n"+
			"                  /____/\n"
		)
		print(f"{Fore.RED}[ ! ] Invaild option")
	else:
		DEFAULT.DEFAULT()