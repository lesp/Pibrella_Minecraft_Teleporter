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
