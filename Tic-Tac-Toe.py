#import tkinter to create GUI
from tkinter import *

#help us show the winner or draw
import tkinter.messagebox

#choose players
def choose_players(player_num):
    tkinter.messagebox.showinfo("Player", "Start the game, player %s" % player_num)

#create an instance of Tk in order to use Tk methods
root = Tk()

#changing the title
root.title('Tic Tac Toe')

#show game instructions
tkinter.messagebox.showinfo("Instructions", " Welcome to Tic Tac Toe. You need to enter 3 consecutive x's or o's in order to win")

playerEntry = Entry(root)
playerEntry.grid(row=0,column=1)

playerLabel = Label(root, text="Enter player: ")
playerLabel.grid(row=0, column=0)

playerButton = Button(root, text = "Submit",command = (lambda:choose_players(playerEntry.get())))
playerButton.grid(row=1, column=0)

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
    '''GRAB THE BUTTON NUMBER THE USER CLICKS ON - VARIABLE NUM, AND THE LOCATION ON THE WINDOW - r FOR ROW AND c FOR COLUMN'''

    '''DISPLAY THE USER INPUT ON THE SPECIFIC BUTTON LOCATION ON THE WINDOW'''
    #import the previously defined global variables - count and click

    global count,click

    if click == True:
        labelPhoto = Label(root, image =xPhoto)
        labelPhoto.grid(row=r,column=c)

        if num==1:
            btn1.set('x')
        elif num == 2:
            btn2.set('x') 
        elif num == 3:
            btn3.set('x')
        elif num == 4:
            btn4.set('x')
        elif num == 5:
            btn5.set('x') 
        elif num == 6:
            btn6.set('x')
        elif num == 7:
            btn7.set('x')
        elif num == 8:
            btn8.set('x')
        else:
            btn9.set('x')

        #redefine the click to be False and increment the number ofclicked buttons by 1
        click = False
        count += 1

        #check whether there is a win or tie
        check_winner()

    #when click is false (when the user changes the button)
    else:
        labelPhoto = Label(root, image = oPhoto)
        labelPhoto.grid(row = r, column = c)

        if num == 1:
            btn1.set('o')
        elif num == 2:
            btn2.set('o') 
        elif num == 3:
            btn3.set('o')
        elif num == 4:
            btn4.set('o')
        elif num == 5:
            btn5.set('o') 
        elif num == 6:
            btn6.set('o')
        elif num == 7:
            btn7.set('o')
        elif num == 8:
            btn8.set('o')
        else:
            btn9.set('o')

        #redefine the click to be True and increment the number of clicked buttons by 1
        click = True
        count += 1

        #check whether there is a winner or if there is a tie
        check_winner()  
    
#function to check for a winner
def check_winner():
    global click, count
    '''CHECK ROWS FOR 3 CONSECUTIVE X'S'''
    row1 = btn1.get() == 'x' and btn2.get() == 'x' and btn3.get() == 'x' != ' '
    row2 = btn4.get() == 'x' and btn5.get() == 'x' and btn6.get() == 'x' != ' '
    row3 = btn7.get() == 'x' and btn8.get() == 'x' and btn9.get() == 'x' != ' '

    '''CHECK DIAGONALS FOR 3 CONSECUTIVE X'S'''
    diag1 = btn1.get() == 'x' and btn5.get() == 'x' and btn9.get() == 'x' != ' '
    diag2 = btn3.get() == 'x' and btn5.get() == 'x' and btn7.get() == 'x' != ' '

    '''CHECK VERTICALS FOR 3 CONSECUTIVE X'S'''
    vert1 = btn1.get() == 'x' and btn4.get() == 'x' and btn7.get() == 'x' != ' '
    vert2 = btn2.get() == 'x' and btn5.get() == 'x' and btn8.get() == 'x' != ' '
    vert3 = btn3.get() == 'x' and btn6.get() == 'x' and btn9.get() == 'x' != ' '
        
    if (row1 or row2 or row3) or (diag1 or diag2) or (vert1 or vert2 or vert3):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player x wins")

        #set click to true so that the first image should always be x after game reset
        click = True

        #restart count for a new game
        count = 0

        #clears the displayed input from the last game
        clear_game()

        #resets the game
        game()

    '''CHECK ROWS FOR 3 CONSECUTIVE O'S'''
    row1 = btn1.get() == 'o' and btn2.get() == 'o' and btn3.get() == 'o' != ' '
    row2 = btn4.get() == 'o' and btn5.get() == 'o' and btn6.get() == 'o' != ' '
    row3 = btn7.get() == 'o' and btn8.get() == 'o' and btn9.get() == 'o' != ' '

    '''CHECK DIAGONALS FOR 3 CONSECUTIVE O'S'''
    diag1 = btn1.get() == 'o' and btn5.get() == 'o' and btn9.get() == 'o' != ' '
    diag2 = btn3.get() == 'o' and btn5.get() == 'o' and btn7.get() == 'o' != ' '

    '''CHECK VERTICALS FOR 3 CONSECUTIVE O'S'''
    vert1 = btn1.get() == 'o' and btn4.get() == 'o' and btn7.get() == 'o' != ' '
    vert2 = btn2.get() == 'o' and btn5.get() == 'o' and btn8.get() == 'o' != ' '
    vert3 = btn3.get() == 'o' and btn6.get() == 'o' and btn9.get() == 'o' != ' '


    if (row1 or row2 or row3) or (diag1 or diag2) or (vert1 or vert2 or vert3):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player o wins")

        #restart count for a new game
        count = 0

        #clears the displayed input from the last game
        clear_game()

        #resets the game
        game()
    
    '''CHECK FOR A DRAW'''
    if count == 9:
        tkinter.messagebox.showinfo(title="Tic Tac Toe",message="It's a draw")
        click = True
        
        clear_game()
        game()         

#function to clear game
def clear_game():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')

#create an event handler
root.mainloop()