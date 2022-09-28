import time
from colorama import Fore
import re
import requests
import sys
import time
import socket
import getpass
import os
import multiprocessing
from multiprocessing import Process
def START():
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
        elif USER == "2":
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
    # set Output file
    while True:
        print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the output")
        FILEPATH = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
        if FILEPATH == "":
            print(f"{Fore.RED}[ ! ] Not Vaild, try again")
        else:
            try:
                TRY = open(f"{os.getcwd()}/{FILEPATH}", "a")
                TRY.close()
                print(f"{Fore.WHITE}[ OK ] {FILEPATH}")
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
    
    Request(URL, FILEPATH, DELAY)

def Request(URL, FILEPATH, DELAY):
    success = 0
    fail = 0
    PAYLOAD = ["\'\'\'\'\'\'", "\"\"\"\"\"\"", "((((((", "))))))", "&&&&&&", ">>>>>>", "<<<<<<", "\\\\\\\\\\\\"]
    print("---------------------------------------------")
    print("\n\n\n\n\n")
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
                            if status_code == "200":
                                if re.search(PAYLOAD[i], str(result.content)):
                                    f = open(f"{os.getcwd()}/{FILEPATH}", "a")
                                    f.writelines(URL[i])
                                    f.writelines("\n")
                                    success += 1
                                    num += 1
                                    break
					# handling Error : No WIFI or Wrong URL
                        except:
                            pass
                    # check if payloads didn`t work
                    if num == 0: fail += 1
                    else: pass
                else:
                    pass
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


def FINAL(URL, FILEPATH, DELAY):
    Request(URL, FILEPATH, DELAY)
