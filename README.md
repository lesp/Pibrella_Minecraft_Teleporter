#Teleport Steve using a Pibrella

![alt](http://twentyoz.com/wp-content/uploads/2014/10/minecraft-logo.jpg)

Minecraft is great fun, but did you know that you can link the Minecraft world to the real world?
No I don't mean that creepers will try and get you in the night, I mean that you can do lots of great things using components in the real world that affect the Minecraft world.

What we will do is create a simple introduction to doing this, using an add on board for your Raspberry Pi

##Pibrella

![alt](http://pibrella.com/assets/pibrella-board.png)

Pibrella is a board designed and made by two companies [Cyntech](http://www.cyntech.co.uk/) and [Pimoroni](http://pimoroni.com/) and it enables anyone to use electronics safely with their Raspberry Pi.
The board retails for around £10 and is well worth the money.

###Install your Pibrella

The Pibrella is designed to work with all models of Raspberry Pi.

**NEVER unplug or plug an add on board from a Raspberry Pi while it is turned on. It will cause damage. Always ensure the power is off**

####For Model A and B
The Pibrella will fit over all of the GPIO pins and will be flush with the Raspberry Pi.

####For Model A+ and B+
The Pibrella will fit over the first 26 pins, where pin 1 is the pin nearest to the micro SD card slot.


####Installing software

Pibrella has an easy to use Python module and to install it we need to open a new LXterminal window and enter the following. Remember to press enter after each line.

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip
sudo pip install pibrella
```
Once installed, close the terminal window and open IDLE for Python 2.7. At present the Minecraft library is currently being ported to work with Python 3. Once this is done I will update this project.

Open the trasnsporter.py file, it's contents look like this.

```python
import pibrella
#Import the Pibrella module so that we can play with it
import time
#We are now masters of time, like Doctor Who, but with a far smaller budget
import mcpi.minecraft as minecraft
#We import the Minecraft module so that we can use it in Python
from random import randint
#From the random module we import the randint function which can choose a random number

mc = minecraft.Minecraft.create()
#We create a connection between Python and the Minecraft game world.

#We define a function and call it button_changed
def button_changed(pin):
    pibrella.buzzer.success()
    #Plays a jaunty little tune using the Pibrella buzzer
    pos = mc.player.getPos()
    #Stores the X,Y,Z position of the player as a variable called pos
    teleport = randint(1,100)
    #Stores a random integer between 1 and 100 in a variable called teleport
    mc.player.setPos(teleport,teleport,teleport)
    #We change the X,Y,Z position of the player to the value stored in the variable teleport
    mc.postToChat("ENERGIZE")
    #We post some Star Trek reference..cos that's cool right?

pibrella.button.changed(button_changed)
#This waits for a button press and when detected it runs the button_changed function.
```

Open an instance of Minecraft and create / open a world.

In IDLE, press F5 to run the code, wait a few seconds and then press the rather large red button on your Pibrella.

Hey presto, Steve is being teleported!


