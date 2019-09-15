# Pi-beeper-script

This script is used to control a buzzer conencted to Raspberry pi 3 Model B on GPIO pin 18.
Inline Ofcourse Python3 required, it\'s almost end of 2019. You can change the GPIO pin connected to the VCC of the buzzre by changing the value of 'GPIO_Pin' variable at line 29

Usage:

Defaults
Inline 'python beep.py' 

5 beeps
Inline 'python beep.py 5'

5 beeps with each each beep lasting 500 milliseconds
Inline 'python beep.py 5 500'

5 beeps with each each beep lasting 500 milliseconds and 800 milliseconds delay in between
Inline 'python beep.py 5 500 800'

------
Usecase:
1) Beep at boot to know that the pi is ready.

To beep the pi at boot, you can add a @reboot cronjob. 
Inline 'crontab -e'
Add the following at the end of the file.
Inline '@reboot $HOME/scripts/beep.py 1 500'

------

2) Use as an output method to report any bug or notification from any other code

------

3) Use this as a command
First make the script executable
Inline 'chmod +x beep.py'
Inline Then either add it to '.bashrc' or to '/usr/bin/'
Inline 'nano ~/.bashrc'
Add this at the end
Inline 'alias beep=\'$HOME/scripts/beep.py\''

OR
Inline Create a symbolic link file in '/usr/bin'
Inline 'sudo ln -s $HOME/scripts/beep.py /usr/bin/beep'

------
