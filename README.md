# Pi Beeper Script

This script is used to control a buzzer conencted to Raspberry pi 3 Model B on GPIO pin 18.

Ofcourse Python3 required, it's almost end of 2019. You can change the GPIO pin connected to the VCC of the buzzre by changing the value of `GPIO_Pin` variable at line 29

**Usage:**

**Defaults**

`python beep.py`

**5 beeps**

`python beep.py 5`

**5 beeps with each each beep lasting 500 milliseconds**

`python beep.py 5 500`

**5 beeps with each each beep lasting 500 milliseconds and 800 milliseconds delay in between**

`python beep.py 5 500 800`

Make the script executable so that we do not have to type python at everytime

`chmod +x beep.py` then you can simply type `./beep.py` and run it as an executable.


------
**Usecase:**

**1)a) Beep at boot to know that the pi is ready. Using Crontab**

To beep the pi at boot, you can add a @reboot cronjob. 

`crontab -e`

Add the following at the end of the file.

`@reboot $HOME/scripts/beep.py 1 500`

------

**1)b) Beep at user login. Using `.bashrc`**

The pi will beep when bash is ready

`nano ~/.bashrc`

Add the following line at bottom

`~/scripts/beep.py 1 500`

You can check with running the following command

`source ~/.bashrc`

------

**1)c) Beep at boot to know that the bash is ready. Using `rc.local`**

The pi will beep when bash is ready

`sudo nano /etc/rc.local`

Add the following line before `exit 0` if it is there,

`/home/pi/scripts/beep.py 1 500`

------
**2) Beep at shutdown. Using `systemd service`**

`sudo nano /etc/systemd/system/beep-before-shut.service`

I like to beep twice at shutdown


```
[Unit]
Description=Beep before Shutting Down

[Service]
Type=oneshot
RemainAfterExit=true
ExecStart=/bin/true
ExecStop=/home/pi/scripts/beep.py 2 100 200

[Install]
WantedBy=multi-user.target
```

Enable and start the service

```
sudo systemctl enable beep-before-shut.service
sudo systemctl start beep-before-shut.service
```

------

**3) Use as an output method to report any bug or notification from any other code**

------

**4) Use this as a command**

First make the script executable

`chmod +x beep.py`

Then either add and alias to `.bashrc` or to `/usr/bin/`

`nano ~/.bashrc`

Add this at the end

`alias beep='$HOME/scripts/beep.py'`

**OR**

Create a symbolic link file in `/usr/bin`

`sudo ln -s $HOME/scripts/beep.py /usr/bin/beep`

