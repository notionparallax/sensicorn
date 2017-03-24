# Setting up remote firmware update

Requirements:
	- software reset
	- arduino software install
	- commandline arduino IDE



## software reset
Although initially a scary prospect, the solution was simple and elegent.
Using a 1 line function 'void(* resetFunc) (void) = NULL;

adding r as a send option for reset in the firmware, software reset is now possible.

## How to install arduino software
.json file etc. (to copmplete)

## Make space on the Raspberry Pi
The Pi ran out of space!

by using `df` I found that /dev/root was 100% used. Oh o.
To look into the file system pseudo-graphically I used 
```
sudo mount --bind / /mnt
sudo ncdu -x /mnt
```
I found /usr was 3.0Gib full (100%)
/usr/lib was 50% of this, the install libraries and their dependencies.
Looks like I'm going to need to remove a bunch of unnecessary libraries.
```
sudo apt-get remove [library to remove]
audo apt-get autoremove was not enough for the big guys (python 3.4, libreoffice, SuperCOliider etc.)
```
was not enough.
Using:
```
sudo apt-get purge libreoffice wolfram-engine sonic-pi scratch
sudo apt-get autoremove
```
cleared up 18% space.
should be enough to work with.
