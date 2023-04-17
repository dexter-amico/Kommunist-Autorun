# **Kommunist Autorun v0.1**

This is a funny autorun executable that I made using Py Installer and Tkinter. It's intended to be used inside a thumb drive or similaries, with the objective of making people aware of the potential risks of using USB flash drives from unknow sources in their computer, or inserting it elsewhere, mainly in public computers. The executable by itself does nothing, just show a program screen with an image and plays a background music, the only available button on the screen just closes the program without doing really anything.

In summary, this program or any associated files to it do not, or rather do not intend to, do anything harmful or collect any kind of data from the user's computer, the sole objective here is to cause some extende of surprise to the user through an unexpected screen and music poping without any kind of notice.

**DISCLAIMER:** To avoid any kind of copyright claims or legal issues I'll not upload the image and sound used by me on my personal iteration of it, but if your really want to see something very close to what I did try searching for the URSS Hymn and the picture of communist Bugs Bunny...

## **How To Compile This Program**

1. Download all files: `autorun.py` and `autorun.spec`
2. Put on the same folder of the files downloaded an image file and a music file
3. Personaly I suggest an image file with 600x600 pixel and in the jpeg format, or modifications on the code will be needed
4. For the music file I suggest a file in the wav format, or there will be necessary to do modifications on the code too
5. Rename the music file to `music.wav` and the image file to `image.jpeg`
6. On the python's console run the following code: `pyinstaller autorun.spec`
7. The executable file will be on the folder `dist`

## **Advanced Tips**

If you really know about the things you don't really need tips, right? But if I can give my 2 cents advice here are some tips:

1. You can change the size of the program screen and the image file on the code
2. The function `def resource_path` on the code is necessary for correct file managing and to the autorun works correctly in just one file. More information about this issue can be found on the following links:
   1. [Auto-py-to-exe: Only One File – WITH IMAGES – For Our Python Apps](https://pythonprogramming.altervista.org/auto-py-to-exe-only-one-file-with-images-for-our-python-apps/)
   2. [Stack Overflow - Bundling data files with PyInstaller (--onefile)](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741)
3. If you want to use an personalyzed icon my suggestion is to use `auto-py-to-exe` package for that, me personally couldn't do this directly with `Python Installer`. For that take a look on the first link above.

### **Necessary packages**

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pygame](https://www.pygame.org/news)
- [Pyinstaller](https://pyinstaller.org/en/stable/index.html)
- [OS](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [Pillow](https://pypi.org/project/Pillow/)
