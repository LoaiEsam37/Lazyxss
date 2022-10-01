# Lazyxss

[![PyPI](https://img.shields.io/pypi/pyversions/apache-superset.svg?maxAge=2592000)](https://pypi.python.org/pypi/apache-superset)
[![PyPI version](https://badge.fury.io/py/pandas.svg)](https://badge.fury.io/py/pandas)
[![PyPI version](https://badge.fury.io/py/matplot.svg)](https://badge.fury.io/py/matplot)
[![Build Status](https://github.com/apache/superset/workflows/Python/badge.svg)](https://github.com/tomnomnom/waybackurls)
### LazyXSS is a tool that can help you scan for reflected XSS, LFI without any effort.

* [Installation](#Installation)
* [Usage](#Usage)


# Installation

    $ git clone https://github.com/LoaiEsam37/Lazyxss
    $ cd Lazyxss
    $ sudo chmod u+x setup.sh
    $ ./setup.sh
    $ ./main.py

if you have a problem with running **./main.py**
try to change the first line in **main.py** from **~~#!/bin/bash/python3~~**
to **#!/bin/bash/python3.10**
It depends on what version you have on your pc.

    $ cd
    $ nano .bashrc

* add this line ***alias lazyxss='python3 Foo/bar/Lazyxss/main.py'*** 

* close the terminal and open it again

* Type ``lazyxss -h`` to display the options of the tool and some Examples for how to use it.

![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140729.png)

# Usage

* There are two ways you can use the tool with 
* you can use Easy Selection that is look like this:
        
```
$ lazyxss
```

![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20142553.png)

* or you can use it with specific Options that is look like this:
```
$ lazyxss -t r-xss -f google -o vuln -d 1 -pf Payloads
```   
![](https://github.com/LoaiEsam37/Images/blob/main/9.png)

## WayBackUrls

   * Make sure to Download [Waybackurls](https://github.com/tomnomnom/waybackurls) and put it in ``/usr/bin`` because this section of my tool depends on it.
        
   ```python
   def Command(URL, OUTPUT)   
       # WayBackUrls
       os.system(f"echo \{URL} | waybackurls >> {OUTPUT}")
   ```

   ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140235.png)
      
   * Here we can choose the method we will use,
   * Let\`s try manually Option first
      
   ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140326.png)
      
   * as you could see we put the Url we want to get waybackurl from, then we put the output file
       
   ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20142401.png)
      
   * Ok, Now Let\`s try file Option

   ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140535.png)
      
   * We made a file that contains 3 targets let\`s scan them

   ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140637.png)
     
     
## SedFilter

   ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20142401.png)
   * Ok, Now we need to prepair the urls to be ready to add Payloads in it 
   * **https://www.google.com/#q=Ten+Amoretterobots.txt** as we can see here 
   * we need to remove the **Ten+Amoretterobots.txt** part of the url like this:

   ```python
   os.system(f"cat {INPUT} |grep -v 'jpg\|jpeg\|png\|svg' |sed 's/=.*/=/g' |uniq > {OUTPUT}")
   ```

   * Ok let\`s see how to do this with the tool

   ![](https://github.com/LoaiEsam37/Images/blob/main/1.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/3.png)
   
## WayBackUrls&SedFilter
   * To understand this section checkout [WayBackUrls](#WayBackUrls), [SedFilter](#SedFilter)
 
## UniqOnly

   ![](https://github.com/LoaiEsam37/Images/blob/main/5.png)
   
   * here we have duplicate url
   * Ok let\`s see how to do this with the tool
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/10.png)
    
## URL Reflected XSS
  
  * This tool if for using your payloads on just the Url parameters
  
   ![](https://github.com/LoaiEsam37/Images/blob/main/11.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/12.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/13.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/14.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/16.png)

## Inputs Reflected XSS
   
   * This tool is for using your payloads on every input on the website
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/11.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/12.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/13.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/14.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/16.png)
   
## ByPassTester
   
   * This tool if for using payloads on just the Url parameters
  
   ```python
   PAYLOAD = ["\'\'\'\'\'\'", "\"\"\"\"\"\"", "((((((", "))))))", "&&&&&&", ">>>>>>", "<<<<<<", "\\\\\\\\\\\\"]
   ```
   
   * The idea here is to try every bypass char on the website
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/13.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/14.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/16.png)
   
   
## LFI

   ![](https://github.com/LoaiEsam37/Images/blob/main/13.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/14.png)
   
   ![](https://github.com/LoaiEsam37/Images/blob/main/16.png)

## Connect Me

<a href="https://linkedin.com/in/loai-esam-109971215" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="loai-esam-109971215" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/loaiesam27" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="loaiesam27" height="30" width="40" /></a>
<a href="https://fb.com/loai.esam.16" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="loai.esam.16" height="30" width="40" /></a>
</p>

