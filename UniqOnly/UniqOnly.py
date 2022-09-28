import os
from colorama import Fore
import re
import time
import sys
import socket
import getpass
import multiprocessing
from multiprocessing import Process
def USER_INPUTS():
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
        return INPUT, OUTPUT

def filter(INPUT, OUTPUT):
        # Filter Urls
        print(f"{Fore.WHITE}[ * ] Loading...")
        os.system(f"cat {INPUT} | uniq >> {OUTPUT}")

def START():
        INPUT, OUTPUT = USER_INPUTS()
        filter(INPUT, OUTPUT)
        print(f"{Fore.WHITE}[ OK ] Done")

def FINAL_LIST(INPUT, OUTPUT):
        filter(INPUT, OUTPUT)
        print(f"{Fore.WHITE}[ OK ] Done")
