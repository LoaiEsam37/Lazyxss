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
import default as DEFAULT
import commandparse as CommandParse

def START_PROGRAM(URL, OUTPUT, PAYLOAD, DELAY, s):
    print(f"{Fore.WHITE}[ OK ] (ALL XSS) selected")
    print(f"{Fore.WHITE}[ * ] The Reflected_XSS will go first then Stored_XSS will go second")
    Reflected_XSS.FINAL_LIST(URL, OUTPUT, PAYLOAD, DELAY)
    Stored_XSS.FINAL(URL, OUTPUT, PAYLOAD, DELAY, s)