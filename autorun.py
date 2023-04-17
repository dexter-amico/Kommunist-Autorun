import tkinter
import pygame
import os
import sys
from PIL import ImageTk, Image


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


window = tkinter.Tk(className='Pendrive Comunista')
window.title('kommunisticheskaya fleshka') # Name displayed on the program screen
window.geometry("700x700") # Change this value for the size of the program screen

pygame.mixer.init()

# This is the file name or relative path to the music file
soundPath = resource_path('music.wav') 


def play(event):
    pygame.mixer.music.load(soundPath)
    pygame.mixer.music.play(loops=0)
    print(event)

# Button properties
buttonFrame = tkinter.Frame(window, width=700, height=10)
buttonFrame.pack(side='bottom', padx=15, pady=15)

# image frame properties
imageFrame = tkinter.Frame(window, width=600, height=600)
imageFrame.pack(side='top')

# change 'text' to change what is the text inside the button
button = tkinter.Button(buttonFrame, text='Vpered tovarishch!',
                        width=25, command=window.destroy)
button.pack()

# Create an object of tkinter ImageTk
# This is the file name or relative path to the image file
imgPath = resource_path("image.jpeg") 
img = ImageTk.PhotoImage(Image.open(imgPath))

# Create a Label Widget to display the text or Image
label = tkinter.Label(imageFrame, image=img)
label.pack()
# This make the music play on the very first time the program becomes visible
label.bind('<Visibility>', play) 

window.mainloop()
