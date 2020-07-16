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
    '''CREATE THE BUTTONS THAT WILL ASSOCIATE USER INPUT WITH THE PREVIOUSLY DEFINED STRING VARIABLES'''
    
    button1 = Button(root, height=9, width=19, relief="ridge", borderwidth=5, background="#EFBBFF", command=lambda:btn_press(1,0,0))
    button1.grid(row=0,column=0)

    button2 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#EFBBFF', textvariable=btn2,command=lambda:btn_press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#EFBBFF', textvariable=btn3,command=lambda:btn_press(3,0,2))
    button3.grid(row=0,column=2)

    button4 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#D896FF', textvariable=btn4,command=lambda:btn_press(4,1,0))
    button4.grid(row=1,column=0)

    button5 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#D896FF', textvariable=btn5,command=lambda:btn_press(5,1,1))
    button5.grid(row=1,column=1)

    button6 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#D896FF', textvariable=btn6,command=lambda:btn_press(6,1,2))
    button6.grid(row=1,column=2)

    button7 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#BE29EC', textvariable=btn7,command=lambda:btn_press(7,2,0))
    button7.grid(row=2,column=0)

    button8 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#BE29EC', textvariable=btn8,command=lambda:btn_press(8,2,1))
    button8.grid(row=2,column=1)

    button9 = Button(root, height=9, width=19,relief='ridge',borderwidth=5,background='#BE29EC', textvariable=btn9,command=lambda:btn_press(9,2,2))
    button9.grid(row=2,column=2)

game()

#function to check for the pressed button
def btn_press(num, r, c):
    '''GRAB THE BUTTON NUMBER THE USER CLICKS ON - VARIABLE NUM, AND THE LOCATIONON THE WINDOW - r FOR ROW AND c FOR COLUMN'''
    

#function to check for a winner
def check_winner():
    pass

#function to clear game
def clear_game():
    pass

#create an event handler
root.mainloop()