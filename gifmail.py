
import os
from random import randint
import hashlib

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def plog(text):
	n = len(text) + 4
	print "%s \n  %s \n%s"%('*'*n,text,'*'*n)

def find_all(string, sub):
    return [i for i in range(len(string)) if string.startswith(sub, i)]

def gifmail(speed='7'):
	string = '''Hello there,
Hope this mail finds you in the best of health and spirit.

With Warm regards
Saurav Tomar
'''
	string = string + " "
	string = string.replace("'",'"')
	unique_id = hashlib.md5(string).hexdigest()[:6]

	os.system("mkdir %s/%s"%(DIR_PATH,unique_id))
	arr= []
	for counter,char in enumerate(string):
		word = string[:counter]
		print word,counter
		arr.append([counter,word])
		os.system("convert -background white -gravity northwest  -fill black -pointsize 17 -size 500x100 caption:'%s' %s/%s/%s.png"%(word,DIR_PATH,unique_id,counter))
		if (counter + 1) == len(string):
			for i in xrange(1,5):
				counter = counter + 1
				word = string
				arr.append([counter,word])
				os.system("convert -background white -gravity northwest  -fill black -pointsize 17 -size 500x100 caption:'%s' %s/%s/%s.png"%(word,DIR_PATH,unique_id,counter))
		
	os.system("ffmpeg -i %s/%s/%%1d.png %s/%s/semi_final.gif"%(DIR_PATH,unique_id,DIR_PATH,unique_id))
	
	os.system("convert -delay 10x%s0 %s/%s/semi_final.gif %s/%s/final.gif"%(speed,DIR_PATH,unique_id,DIR_PATH,unique_id))

	os.system("cp %s/%s/final.gif %s/%s.gif"%(DIR_PATH,unique_id,DIR_PATH,unique_id))
	os.system("rm -rf %s/%s"%(DIR_PATH,unique_id))
	os.system("open -a 'Google Chrome' %s/%s.gif"%(DIR_PATH,unique_id))
	plog(unique_id)



def main():
	string= "they bowed down to him rather, because he was all of these things, and then again he was all of these things because"
	unique_id = hashlib.md5(string).hexdigest()[:6]
	word_arr = string.split(" ")

	os.system("mkdir %s/%s"%(DIR_PATH,unique_id))

	for counter,word in enumerate(word_arr):
		print word,counter
		#gen_image(unique_id,word,counter)
		os.system("convert %s/yellow.png -gravity center -weight Bold -pointsize 20 -annotate 0 '%s'  %s/%s/%s.png"%(DIR_PATH,word,DIR_PATH,unique_id,counter))
	
	os.system("ffmpeg -i %s/%s/%%1d.png %s/%s/semi_final.gif"%(DIR_PATH,unique_id,DIR_PATH,unique_id))
	os.system("convert -delay 10x30 %s/%s/semi_final.gif %s/%s/final.gif"%(DIR_PATH,unique_id,DIR_PATH,unique_id))

	os.system("cp %s/%s/final.gif %s/%s.gif"%(DIR_PATH,unique_id,DIR_PATH,unique_id))
	os.system("rm -rf %s/%s"%(DIR_PATH,unique_id))
	os.system("open -a 'Google Chrome' %s/%s.gif"%(DIR_PATH,unique_id))



'''
FontExperiment
convert -size 32x32 xc:white empty.jpg
convert yellow.png -gravity center -pointsize 72 -annotate 0 'FoodchamberIsle'  lol.png
convert yellow.png -gravity center -weight Bold -annotate 0 'FoodChamberIsle'  lol.png

convert mail_canvas.png -gravity northwest -pointsize 17 -size 500x caption:'food chamber' test.png
'''

if __name__ == '__main__':
	#main()
	gifmail()
	
