# ascii-art-python3-cli
Python3 cli tool for making ascci art images. <br>
Full color or black and white photos. <br>
The larger the image size the better the resolution.

## Features
- adjust image scale        --scale
- adjust a character width  --charW
- adjust a character height --charH
- revers character order for white background img   --rev
- name the output file      --output


## Requirements
Python (3)<br>

## Module Installation
pip install -r requirements.txt<br>
Tested on<br>
Mac OSX 10.15.4

##Download udemy-dl
You can download the latest version of ascii-art-python3-cli by cloning the GitHub repository.

git clone https://github.com/RobHunn/ascii-art-python3-cli

##Usage
Make art image by first calling the start file then passing you image file name

>python ascii.py img.png

Optional flags

>python ascii.py img.png --scale=.1 --charW=12 --charH=18 --rev=False --output=newimg
