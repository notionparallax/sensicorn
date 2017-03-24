# Setting up remote firmware update

Requirements:
	- software reset
	- arduino software install
	- commandline arduino IDE



# software reset
Although initially a scary prospect, the solution was simple and elegent.
Using a 1 line functio 'void(* resetFunc) (void) = NULL;

adding r as a send option for reset in the firmware, software reset is now possible.

## To install sraduino software