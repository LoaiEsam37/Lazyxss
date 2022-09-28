import re
import os
import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin
import getpass
import socket
from colorama import Fore
import time
import multiprocessing
from multiprocessing import Process
# make a fake User-Agent
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

# main function
def xss_url_scanner(URL, FILEPATH, DELAY, PAYLOAD, s):
    success = 0
    fail = 0
    num_url = 0
    print("---------------------------------------------")
    print("\n\n\n\n\n\n", end='')
    for url in URL:
        num_url += 1
        try:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            print(
                Fore.WHITE+
                f"URL No.: {num_url} from {len(URL)} ; {int((num_url) / (len(URL)) * 100)}%;\n"+
                f"Response: {res.status_code};\n"+
                f"vulnerable: {success};\n"+
                f"Not vulnerable: {fail};\n"+
                f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - (((num_url * DELAY) + num_url) / 60))} min;\n"        
            )
        except:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            print(
                Fore.WHITE+
                f"URL No.: {num_url} from {len(URL)} ; {int((num_url) / (len(URL)) * 100)}%;\n"+
                f"Response: ...;\n"+
                f"vulnerable: {success};\n"+
                f"Not vulnerable: {fail};\n"+
                f"Approximate Time: {int((((len(URL) * DELAY) + len(URL)) / 60) - (((num_url * DELAY) + num_url) / 60))} min;\n"        
            )
        try:
            forms = get_forms(url, s)
            for form in forms:
                details = form_details(form)
                Payload_success = 0  
                for c in PAYLOAD:
                    data = {}
                    try:
                        for input_tag in details["inputs"]:
                            try:
                                if input_tag["type"] == "hidden" or input_tag["value"]:
                                    data[input_tag["name"]] = input_tag["value"] + c
                                elif input_tag["type"] != "submit":
                                    data[input_tag["name"]] = f"test{c}"
                                url = urljoin(url, details["action"])
                                if details["method"] == "post":
                                    res = s.post(url, data=data)
                                elif details["method"] == "get":
                                    res = s.get(url, params=data)
                                if re.search(c, res.content):
                                    with open(f"{os.getcwd()}/{FILEPATH}", "a") as f:
                                        f.writelines(str(url))
                                        f.writelines("\n")
                                    success += 1
                                    Payload_success += 1
                                    break
                                else:
                                    pass
                            except:
                                pass
                            time.sleep(DELAY)
                    except: pass
                if Payload_success == 0: fail += 1
        except: fail += 1
    # Done
    print(f"{Fore.LIGHTGREEN_EX}\r---------------------------------------------")

# grep all form tags from the url
def get_forms(url, s):
    try:
        soup = BeautifulSoup(s.get(url).content, "html.parser")
        result = soup.find_all("form")
        return result
    except:
        pass
# grep form details
def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        try:
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": input_name, "value": input_value})
        except:
            pass        
    detailsOfForm["action"] = action
    detailsOfForm["method"] = method
    detailsOfForm["inputs"] = inputs
    return detailsOfForm

class SETUP:
    def USER_INPUT():
        # PAYLOAD
        while True:
            print(f"{Fore.LIGHTGREEN_EX}[ * ] Do you want to put a file or Type manually the Payloads")
            print("[ * ] 1 --> manually\n[ * ] 2 --> file")
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@LazyXSS$ ")
            # manually
            if USER == "1":
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
        return URL, FILEPATH, DELAY, PAYLOAD

def START():
    URL, FILEPATH, DELAY, PAYLOAD = SETUP.USER_INPUT()
    xss_url_scanner(URL, FILEPATH, DELAY, PAYLOAD, s)

def FINAL(URL, FILEPATH, PAYLOAD, DELAY, s):
    xss_url_scanner(URL, FILEPATH, DELAY, PAYLOAD, s)
