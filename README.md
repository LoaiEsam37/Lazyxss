## Lazyxss

LazyXSS is a tool that can help you scan for reflected XSS, LFI without any effort.

## Setup

sudo chmod u+x setup.sh
./setup.sh
./main.py

if you have a problem with running ./main.py
try to change the first line in it from #!/bin/bash/python3.8
to #!/bin/bash/python3 or #!/bin/bash/python3.10
It depends on what version you have on your pc.

and another option you can use,
add this line to Your .Bashrc (alias lazyxss='python3 Foo/bar/Lazyxss/main.py') 
then close the terminal and open it again

Now You can just type (lazyxss) in your terminal and hit Enter 
Type (lazyxss -h) to display the options of the tool and some Examples for how to use it
