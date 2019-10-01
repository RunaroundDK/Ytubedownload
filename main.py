## Download videos and music from youtube !!
import argparse
import subprocess

## Three diffrent commands
## -d = download single youtube video into mp3 format
## -t = download mutiple songs from a txt file
##youtube-dl --extract-audio --audio-format mp3 <video URL>
##youtube-dl -a video_links.txt

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--download",
						help="Download a youtube video into mp3 format.")
	parser.add_argument("-t", "--txt",
						help="Download from a txt file with urls.")

	args = parser.parse_args()
	if args.download:
		print ("Downloading {}".format(args.download))
		cmd = "youtube-dl --extract-audio --audio-format mp3 " + args.download
		sysoutput = subprocess.call(cmd, shell=True)
	elif args.txt:
		print("Downloading from {}".format(args.txt))
		cm = "youtube-dl --extract-audio --audio-format mp3 -a " + args.txt
		sysoutput = subprocess.call(cm, shell=True)
	else:
		print ("Something went wrong..")

if __name__== "__main__":
  main()


#Links sources
#https://docs.python.org/3/howto/argparse.html
#https://www.journaldev.com/16140/python-system-command-os-subprocess-call#python-ossystem-function
#https://www.slashgeek.net/2016/06/24/5-youtube-dl-tips-might-not-know/
