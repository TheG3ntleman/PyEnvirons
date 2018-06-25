# PyEnvirons

"PyEnvirons" is a higher level API of pygame to easily design, devolop and debug environments for your unsupervised AI agent. It is under rapid development and features will be added almost every single day.

## Usage and examples

To show you how simple PyEnvirons is here is a example.

### Creating a functional window

```python
from Core import window #Importing the window class
screen = window.Window([800, 600], 'testwindow') 
#Instantiating the window class to make a window, by specifying the size and name of the window

from Core import app #Importing an app class for us to inject into the window
app = app.App(screen) #Instantiating the app class by giving the app our window

app.run() #running our app
```

### Using sprites, gameobjects and layers
```python
from Core import window #Importing the window class
screen = window.Window([800, 600], 'testwindow') 
#Instantiating the window class to make a window, by specifying the size and name of the window


from Core import app #Importing an app class for us to inject into the window
app = app.App(screen) #Instantiating the app class by giving the app our window


from Core import sprite #Importing the sprite class for us to load and use images on the hardrive.
image = sprite.Sprite('PyEnviron/SpriteTests/2635d6c2b056dfb.png') #Loading a sprite for our use by specfying a file path

from Core import layer #Each sprite must be alloted a layer to be instantiated eg:background, foreground, player, etc...
layer = layer.Layer() #Instantiating a layer for us to put sprites into

from Core import gameobject #The gameobject class, will have all the variables regarding the sprite, like the image, position, rotation, and script attached to it.
gm = gameobject.GameObject(image) #Instantiating a gameobject for us to use by giving it our sprite, position, rotation and scale are [0, 0], 0 degrees and [1, 1], respectivly, by defualt.

layer.add_gameobject(gm) #Adding our game object to the layer

app.add_layer(layer) #Adding the layer to our app

app.run()#Running the app
```
