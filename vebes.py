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
b=0
if (options.name is None and options.song is None):
    b=1
    choice=raw_input("You want to search a Song or Artist: ")
    a=1
    if(choice!='Song' and choice!='Artist'):
        a=0

while(a==0 and b==1):
    if(choice!='Song' and choice!='Artist'):
        print 'choose correct option'
        choice=raw_input("You want to search a Song or Artist: ")
        a=1
        if(choice!='Song' and choice!='Artist'):
            a=0

if (options.name is None and options.song is None and choice=='Song'):
    options.song = raw_input('Enter Name of the song:')

if (options.name is None and options.song is None and choice=='Artist'):
    options.name = raw_input('Enter Name of the Artist:')

if(options.name is None):
    a = os.path.dirname(os.path.realpath(__file__))


    os.chdir(a)
    cou = 0
    for file in glob.glob("*.mp3"):
    
	   tag = eyeD3.Tag()
	   tag.link(file)
	   if(options.song in file):
		
		  cou=cou+1
		  print file
    	
    b = os.path.dirname(os.path.realpath(__file__))
    
    os.chdir(b)
    for name in glob.glob('*/*.mp3'):
        tag = eyeD3.Tag()
        tag.link(name)
        if(options.song in name):
    
            cou=cou+1
            print name
	
    if(cou==0):
	   print "no song available"

if (options.name is None and options.song is None):
    options.name = raw_input('Enter Name of the artist:')


if(options.song is None):
    a = os.path.dirname(os.path.realpath(__file__))

    os.chdir(a)
    count = 0
    for file in glob.glob("*.mp3"):
    
        tag = eyeD3.Tag()
        tag.link(file)
        if(options.name in tag.getArtist()):
        
            count=count+1
            print tag.getTitle()
        
    b = os.path.dirname(os.path.realpath(__file__))
    
    os.chdir(b)
    for name in glob.glob('*/*.mp3'):
        tag = eyeD3.Tag()
        tag.link(name)
        if(options.name in tag.getArtist()):
    
            count=count+1
            print tag.getTitle()
    
    if(count==0):
        print "no song of this artist"

time.sleep(3)
