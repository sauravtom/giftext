
"""
============================================================
              Giftext
Converts texts to gif animations
============================================================
"""
#imports 

import argparse
import time
import os
import time
import random
import pdb

from utils import blinking_animation,typing_animation

print("")
print("***********************************************")
print("                 Giftext v1.0                  ")
print("Converts text to animated gifs")
print("***********************************************")

#options
parser = argparse.ArgumentParser(description='Giftext v1.0')
parser.add_argument('-t','--text',help='text string',required=True)
parser.add_argument('-o' ,'--savepath',help='output gif path',required=True)
parser.add_argument('-a','--animationType',help='Type of animation (typing/blinking) | Default is blinking',type=str,default='static',required=True)
parser.add_argument('-s','--speed',help='speed of animation | Default is 8',type=int,default=8)

args = parser.parse_args()


start = time.time()  

if not args.savepath.endswith('.gif'):
	print("-o output file extension must be a gif")  
	exit()

if args.animationType not in 'blinking,typing'.split(','):
	print("-a flag should be either static or typing")  
	exit()

if args.animationType == 'blinking':
	blinking_animation(string=args.text,speed=args.speed,output=args.savepath)
else:
	typing_animation(string=args.text,speed=args.speed,output=args.savepath)



print ('Elaspsed ',time.time() - start, 'sec') 

