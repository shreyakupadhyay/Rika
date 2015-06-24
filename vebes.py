import glob
import os
import eyeD3
import sys
import time
import fnmatch
import optparse
parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='name-of-the-artist')
parser.add_option('-s', '--song', dest='song', help='song-name')

(options, args) = parser.parse_args()
a=0
if (options.name is None and options.song is None):
    choice=raw_input("You want to searh a Song or Artist: ")
    a=1
    if(choice!='Song' and choice!='Artist'):
        a=0
#if (options.name is None and options.song is None and choice=='Song'):
    #options.song = raw_input('Enter Name of the song:')
#if options.song is None:
 #   options.song = raw_input('Enter Name of the song:')
while(a==0):
    if(choice!='Song' and choice!='Artist'):
        print 'choose correct option'
        choice=raw_input("You want to searh a Song or Artist: ")
        a=1
        if(choice!='Song' and choice!='Artist'):
            a=0

if (options.name is None and options.song is None and choice=='Song'):
    options.song = raw_input('Enter Name of the song:')

if (options.name is None and options.song is None and choice=='Artist'):
    options.name = raw_input('Enter Name of the Artist:')

if(options.name is None):
    a = os.path.dirname(os.path.realpath(__file__))
#print a
#os.chdir("/home/shreyak/Documents/ReceivedFiles")
    os.chdir(a)
    cou = 0
    for file in glob.glob("*.mp3"):
    #import eyeD3
	   tag = eyeD3.Tag()
	   tag.link(file)
	   if(options.song in file):
		#print tag.getArtist()
		  cou=cou+1
		  print file
    	#print(file)'Backstreet Boys'
#if(count==0):
#	print "no song of this artist"

#def scanfolder():
    b = os.path.dirname(os.path.realpath(__file__))
    #os.chdir("/home/shreyak/Documents/ReceivedFiles")
    #cou=0
    os.chdir(b)
    for name in glob.glob('*/*.mp3'):
        tag = eyeD3.Tag()
        tag.link(name)
        if(options.song in name):
     #   	cou=cou+1
            cou=cou+1
            print name
	#if(cou==0):
	#	print "no song of this artist"
    if(cou==0):
	   print "no song available"
#scanfolder()
#time.sleep(3)

#parser = optparse.OptionParser()
#parser.add_option('-n', '--name', dest='name', help='name-of-the-artist')
#parser.add_option('-s', '--song', dest='song', help='song-name')

#(options, args) = parser.parse_args()
if (options.name is None and options.song is None):
    options.name = raw_input('Enter Name of the artist:')
#if options.song is None:
 #   options.song = raw_input('Enter Name of the song:')

if(options.song is None):
    a = os.path.dirname(os.path.realpath(__file__))
#print a
#os.chdir("/home/shreyak/Documents/ReceivedFiles")
    os.chdir(a)
    count = 0
    for file in glob.glob("*.mp3"):
    #import eyeD3
        tag = eyeD3.Tag()
        tag.link(file)
        if(options.name in tag.getArtist()):
        #print tag.getArtist()
            count=count+1
            print tag.getTitle()
        #print(file)'Backstreet Boys'
#if(count==0):
#   print "no song of this artist"

#def scanfolder():
    b = os.path.dirname(os.path.realpath(__file__))
    #os.chdir("/home/shreyak/Documents/ReceivedFiles")
    #cou=0
    os.chdir(b)
    for name in glob.glob('*/*.mp3'):
        tag = eyeD3.Tag()
        tag.link(name)
        if(options.name in tag.getArtist()):
     #      cou=cou+1
            count=count+1
            print tag.getTitle()
    #if(cou==0):
    #   print "no song of this artist"
    if(count==0):
        print "no song of this artist"
#scanfolder()
time.sleep(3)
