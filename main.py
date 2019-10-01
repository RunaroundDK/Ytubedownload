## Download videos and music from youtube !!
import argparse
import subprocess
## Three diffrent commands
## -d = download single youtube video into mp3 format
## -ply = Download a whole playlist into an mp3 format
## -t = download mutiple songs from a txt file
##youtube-dl --extract-audio --audio-format mp3 <video URL>
##youtube-dl -a video_links.txt
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--download", required=True,
						help="Download a youtube video into mp3 format.")
	parser.add_argument("-ply", "--playlist",
						help="Download a playlist into a mp3 foramt.")
	parser.add_argument("-t", "--txt",
						help="Download from a txt file with urls.")

	args = parser.parse_args()
	if args.download:
		print ("Downloading {}".format(args.download))
		cmd = "youtube-dl --extract-audio --audio-format mp3 " + args.download
		sysoutput = subprocess.call(cmd, shell=True)
	elif args.txt:
		print("Downloading from {}".format(args.txt))



if __name__== "__main__":
  main()
