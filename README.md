# Lazyxss

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

1. WayBackUrls

      ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140235.png)
      
      * Here we can choose the method we will use,
      * Let\`s try manually first
      
      ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20140326.png)
      
      * as you could see we put the Url we want to get waybackurl from, then we put the output file
       
      ![](https://github.com/LoaiEsam37/Images/blob/main/Screenshot%202022-09-30%20142401.png)
      
      * Ok, Now Let\`s try file



2. SedFilter

3. WayBackUrls&SedFilter

4. UniqOnly

5. URL Reflected XSS

6. Inputs Reflected XSS

7. ByPassTester

8. LFI


## Connect Me

<a href="https://linkedin.com/in/loai-esam-109971215" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="loai-esam-109971215" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/loaiesam27" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="loaiesam27" height="30" width="40" /></a>
<a href="https://fb.com/loai.esam.16" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="loai.esam.16" height="30" width="40" /></a>
</p>

