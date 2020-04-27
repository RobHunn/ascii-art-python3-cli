# ascii-art-python3-cli

Python3 cli tool for making high res ascci art images. <br>
Full color or black and white photos. <br>
The larger the image size the better the resolution.

## Features

Adjust features interactively or by command-line flags.

- adjust image scale --scale
- adjust character font-size --font-size
- adjust a character width --charW
- adjust a character height --charH
- reverse character order for white background img --rev
- name the output file --output
- query me for remaining options -i

![Black n white](/images/model2.png)

## Requirements

Python (3)<br>
pip

## Module Installation

pip install -r requirements.txt

**Tested on:**<br>
Mac OSX 10.15.4  
Windows 10

## Download ascii-art-python3-cli<br>

You can download the latest version of ascii-art-python3-cli by cloning the GitHub repository.

git clone https://github.com/RobHunn/ascii-art-python3-cli

## Usage - Make art

######Use any of these usage methods:

1. `python ascii.py` then answer interactive questions.
2. `python ascii.py img.jpg` output art with default settings<br>
3. `python ascii.py img.jpg` plus optional flags. Enter any number of optional flags. Use -i for interactive mode to be queried for remaining options.

Optional flags

> python ascii.py img.png --scale=.1 --charW=12 --charH=18 --rev=False --output=newimg -i

![Black n white](/images/output.png)
