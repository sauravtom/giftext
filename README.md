# Giftext
Converts text to animated gifs


### Demo #1 (blinking animation)
![All examples](https://raw.githubusercontent.com/sauravtom/giftext/master/assets/r1.gif)  

### Demo #2 (typing animation)
![All examples](https://raw.githubusercontent.com/sauravtom/giftext/master/assets/hithchiker.gif)  


### Dependencies
* Python 2.7.x 
* [Imagemagick](https://www.imagemagick.org/) (for .gif output)
* [ffmpeg](https://www.ffmpeg.org/) (for .mp4 output)

```
usage: giftext.py [-h] -t TEXT -o SAVEPATH -a ANIMATIONTYPE [-s SPEED]

Giftext v1.0

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  text string
  -o SAVEPATH, --savepath SAVEPATH
                        output gif path
  -a ANIMATIONTYPE, --animationType ANIMATIONTYPE
                        Type of animation (typing/static) | Default is static
  -s SPEED, --speed SPEED
                        speed of animation | Default is 8
```

### Example

```
python giftext.py -t 'hello world' -o foo.gif -a typing
```

