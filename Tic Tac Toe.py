#import tkinter to create GUI
from tkinter import *

#import tkinter submodule, messagebox, to help us show the game results
import tkinter.messagebox

#create a Tk instance to help us use Tk methods
root = Tk()

#change the application's title
root.title("Tic Tac Toe")

#prevent the user from resizing the window
root.resizable(False, False)

