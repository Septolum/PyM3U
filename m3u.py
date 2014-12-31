import os, sys, locale
import win32_unicode_argv

m3u = [u'#EXTM3U']
ext = 'wav','aiff','aif','iff','svx','snd','au','voc','cue','ogg','mpc','mp+','mpp','mp3','mp2','mp4','m4a','aac','flac','fla','ape','mac','wv','spx','sid','cda', 'mkv'

def makem3u(dir):
	for i in os.listdir(dir):
		if i.lower().endswith(ext):
			m3u.append((dir + u'/' + i).encode('utf-8'))
	return m3u

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "Usage: m3u.py [Absolute directory you want a playlist of]\n"
		sys.exit(1)
	else:
		dir = sys.argv[1].replace('\\', '/')
		if os.path.exists(dir):
			file = file((dir + u'/' + dir.split(u'/')[-1] + u'.m3u'), 'w')
			content = []
			for x in makem3u(dir):
				content.append(x.decode('utf-8'))
			#print content
			contentstr = u'\n'.join(content)
			#print contentstr
			file.write(contentstr.encode('UTF-8-SIG'))
			file.close()
		else:
			sys.stderr.write("Given directory does not exist\n")
			sys.exit(2)
