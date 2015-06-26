import glob,os,eyeD3,sys,time,fnmatch,optparse
parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='name-of-the-artist')
parser.add_option('-s', '--song', dest='song', help='song-name')
parser.add_option('-a', '--album', dest='album', help='album-name')
(options, args) = parser.parse_args()
if (options.name is None and options.song is None and options.album is None):
    search=raw_input("Search: ")
    c=0
    b = os.path.dirname(os.path.realpath(__file__))
    os.chdir(b)
    for z in range(0,100):
        for name in glob.glob('*/*'*z+'.mp3'):
            tag = eyeD3.Tag()
            tag.link(name)
            if(search in name or search in tag.getArtist() or search in tag.getAlbum()):
                c=c+1
                print name
    if(c==0):
       print "no such type or search available"    
if(options.name is None and options.album is None and options.song is not None):
    cou = 0
    b = os.path.dirname(os.path.realpath(__file__))
    os.chdir(b)
    for i in range(0,100):
        for name in glob.glob('*/*'*i+'.mp3'):
            tag = eyeD3.Tag()
            tag.link(name)
            if(options.song in name):
    
                cou=cou+1
                print name
	
    if(cou==0):
	   print "no song available"

if(options.song is None and options.album is None and options.name is not None):
    count = 0
    b = os.path.dirname(os.path.realpath(__file__))
    
    os.chdir(b)
    for j in range(0,100):
        for name in glob.glob('*/*'*j+'.mp3'):
            tag = eyeD3.Tag()
            tag.link(name)
            if(options.name in tag.getArtist()):
    
                count=count+1
                print tag.getTitle()
    
    if(count==0):
        print "no song of this artist"

if(options.song is None and options.name is None and options.album is not None):
    co = 0
    b = os.path.dirname(os.path.realpath(__file__))
    
    os.chdir(b)
    for k in range(0,100):
        for name in glob.glob('*/*'*k+'.mp3'):
            tag = eyeD3.Tag()
            tag.link(name)
            if(options.album in tag.getAlbum()):
    
                co=co+1
                print name
    
    if(co==0):
        print "no song of this album"
