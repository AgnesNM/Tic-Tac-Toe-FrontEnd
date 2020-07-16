#import tkinter to create GUI
from tkinter import *

#help us show the winner or draw
import tkinter.messagebox

#create an instance of Tk in order to use Tk methods
root = Tk()

#changing the title
root.title('Tic Tac Toe')

#prevent the user from resizing the window
root.resizable(False,False)

#create global variables
click = True

#counts the number of moves. If there are 9 moves, then it's a draw
count = 0

#create string variables which will be associated with user input
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

#store x and o into variables
xPhoto = PhotoImage(file = "x.png")
oPhoto = PhotoImage(file = "o.png")

#create the main functions we will use in the game

#main game function
def game():
    pass

#function to check for the pressed button
def btn_press():
    pass

#function to check for a winner
def check_winner():
    pass

#function to clear game
def clear_game():
    pass

#create an event handler
root.mainloop()