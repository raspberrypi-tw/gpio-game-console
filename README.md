# One Days Workshop for Raspberry Pi GPIO Tutorial

## Intro
In this workshop, we will introudce the Raspberry Pi GPIO, including:
1. Electronic circuit
2. How to write code for the following specification
3. Design a game console with simple hardware component

The slide is available on [用Raspberry Pi學GPIO - 自己做遊戲機](https://www.slideshare.net/raspberrypi-tw/gpio-gameconsolestarterkit)


## Environment
[Raspberry Pi 3](https://www.raspberrypi.com.tw/10684/55/) + SanDisk 32G microSD  + [Raspberry Pi GPIO Game Console Kit](https://www.raspberrypi.com.tw/2557/gpio-game-console-starter-kit/) + 2017-11-29-raspbian-stretch.img

## Prerequisite
### Install required package and Python module
```shell  
$ sudo apt-get update
$ sudo apt-get install -y x11vnc python-dev python-pip libsdl1.2-dev 
$ sudo pip install spidev evdev
```

### Emulation
1. Download pre-built emultation
```shell  
$ cd ~
$ wget http://sosorry.s3.amazonaws.com/raspberrypi/code/advmame
```

2. Create RC file
```shell  
$ cd ~
$ chmod 755 advmame
$ ./advmame
```

3. Download Super Mario ROM
```shell  
$ cd /home/pi/.advance/rom
$ wget http://sosorry.s3.amazonaws.com/download/suprmrio.zip
```
