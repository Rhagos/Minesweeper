
#Implement a basic GUI library


import sys
import math

try:
    import tkinter
except Exception as e:
    print('Can\'t load tkinter! ' + str(e))

#THE HUMAN EYE CAN ONLY SEE AT 24 FPS KAPPA
FRAME_TIME = 1/30

class Canvas(object):
    """
    Canvas object supports drawing/animation primatives

    draw_ methods return the id of a shape in the Tk object.
    This is passed into move_/edit_ methods

    Only 1 canvas can exist at a time
    """

    _instance = None

    def __init__(self, width=1024, height=768, title='', color='White',tk=None):
        #Singleton enforcement (Throws an exception if more than 1 canvas)
        if Canvas._instance is not None:
            raise Exception('Only 1 Canvas can be instantiated')
        Canvas._instance = self

        #Attributes
        self.color = color
        self.width = width
        self.height = height

        #Root window
        self._tk = tk or tkinter.Tk()
        self._tk.protocol('WM_DELETE_WINDOW', sys.exit)
        self._tk.title(title or 'Graphics Window')
        self._tk.bind('<Button-1>', self._click)
        self._click_pos = None

        #Canvas object
        self._canvas = tkinter.Canvas(self._tk, width = width, height=height)
        self._canvas.pack()
        self._draw_background()
        self._canvas.update()
        self._images = dict()

        #Clears the given shape, otherwise clears all
        def clear(self, shape='all'):
            self._canvas.delete(shape)
            if shape == 'all':
                self._draw_background()
