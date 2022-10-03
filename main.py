#!/usr/bin/python3
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

parser = argparse.ArgumentParser(

	prog="LazyXSS",

	description='LazyXSS is a tool that can help you scan for reflected XSS, Stored XSS, LFI',

	epilog=
	"EXAMPLE: (lazyxss -t w -u www.example.com -o example_out)\n"+ 
	"here i chose the tool, set the site i wanted to get waybackurls for and set the output.\n"+
	"ANOTHER EXAMPLE: (lazyxss -t r-xss -f example_in -o example_out -d 10 -p lazyxss)\n"+
	"here i chose the tool, set the file of urls to take the input from then i set the output file and finally put the number of seconds for delay"
	)

parser.add_argument("--tool", "-t", help="select the tool you want to use from the following(ByPassTester = b, LFI = l, URL_Reflected_XSS = r-xss, SedFilter = s, Inputs_reflected_XSS = s-xss, UniqOnly = u, WayBackUrls = w, WayBackUrls&SedFilter = ws, ALL_xss = a-xss)")
parser.add_argument("--output", "-o", help="set the filename for Output")
parser.add_argument("--file", "-f", help="set the urls filename")
parser.add_argument("--url", "-u", help="set the url")
parser.add_argument("--delay", "-d", type=int, help="set the Time of Delay between every Request")
parser.add_argument("--payloadsfilename", "-pf", help="set the Payloads Filename")
parser.add_argument("--payload", "-p", help="Type the Payload")
args = parser.parse_args()

# Payload
if bool(args.payload):
	PAYLOAD = args.payload

# PayloadsFilename
if bool(args.payloadsfilename):
	try:
		payloadsfilename = args.file
		f = open(f"{os.getcwd()}/{payloadsfilename}", "r")
		PAYLOAD = re.split("\n", str(f.read()))
		f.close()
	except:
		print(f"{Fore.RED}[ ! ] Wrong payloadsfilename")
		quit()

# DELAY
if bool(args.delay):
	DELAY = args.delay
else:
	DELAY = 0

# FILEPATH
if bool(args.file):
	try:
		FILEPATH = args.file
		f = open(f"{os.getcwd()}/{FILEPATH}", "r")
		URL = re.split("\n", str(f.read()))
	except:
		print(f"{Fore.RED}[ ! ] Wrong FILEPATH")
		quit()

# URL
if bool(args.url):
	try:
		URL = args.url
		try:
			try:
				requests.get(f"{URL}")
			except:
				try:
					requests.get(f"https://{URL}")
				except:
					requests.get(f"http://{URL}")
		except:
			print(f"{Fore.RED}[ ! ] Wrong URL")
			quit()
	except:
		print(f"{Fore.RED}[ ! ] Wrong URL")
		quit()

# OUTPUT
if bool(args.output):
	try:
		OUTPUT = args.output
		f = open(f"{os.getcwd()}/{OUTPUT}", "a")
	except:
		print(f"{Fore.RED}[ ! ] Wrong OUTPUT")
		quit()

CommandParse
