import os
from colorama import Fore
import re
import multiprocessing
from multiprocessing import Process
import time
import sys
import socket
import getpass

def START():
        # set Input file
        while True:
                print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the input")
                INPUT = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
                if INPUT == "":
                        print(f"{Fore.RED}[ ! ] Not Vaild, try again")
                else:
                        try:
                                TRY = open(f"{os.getcwd()}/{INPUT}", "r")
                                TRY.close()
                                print(f"{Fore.WHITE}[ OK ] {INPUT}")
                                break
                        except:
                                print(f"{Fore.RED}[ ! ] Not Vaild, try again")
        # set Output file
        while True:
                print(f"{Fore.LIGHTGREEN_EX}[ * ] Type the filepath for the output")
                OUTPUT = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
                if OUTPUT == "":
                        print(f"{Fore.RED}[ ! ] Not Vaild, try again")
                else:
                        try:
                                TRY = open(f"{os.getcwd()}/{OUTPUT}", "a")
                                TRY.close()
                                print(f"{Fore.WHITE}[ OK ] {OUTPUT}")
                                break
                        except:
                                print(f"{Fore.RED}[ ! ] Not Vaild, try again")
        filter(INPUT, OUTPUT)
        
def filter(INPUT, OUTPUT):
        # Filter Urls
        print(f"{Fore.WHITE}[ * ] Loading...")
        os.system(f"cat {INPUT} |grep -v 'jpg\|jpeg\|png\|svg' |sed 's/=.*/=/g' |uniq > {OUTPUT}")
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

def FINAL_LIST(INPUT, OUTPUT):
        filter(INPUT, OUTPUT)
        print(f"{Fore.WHITE}[ OK ] Done")
