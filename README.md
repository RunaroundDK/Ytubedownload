# Ytubedownload
Python scirpt that will download youtube videos in command line.

## Purpsoe
I get lazy and sometimes don't like typing out long commands, So I created this command line script to download videos faster!!

## Installation

Arch Linux
```sh
pacman -S youtube-dl
```
Ubuntu 
```sh
sudo apt-get install youtube-dl
```

## Usage example

To download youtube videos into mp3 audio
```sh
python main.py -d <url>
```
Download multiple videos from a file into mp3 audio
```sh
python main.py -t <file.txt>
```

## Release History
* 0.1.1
    * Added txt download option 
    * Fixed Bug 
* 0.1.0
    * added -d option
    * uploaded file to github
* 0.0.1
    * Work in progress

## Sources
https://docs.python.org/3/howto/argparse.html
https://www.journaldev.com/16140/python-system-command-os-subprocess-call#python-ossystem-function
https://www.slashgeek.net/2016/06/24/5-youtube-dl-tips-might-not-know/
