#BÀI TH8 KTLT
#1
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)


def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)
for i in range(1,180):
    painter.left(18)
    drawsq(painter, 200)
#2
import turtle, random
colors = ["red","green","blue","orange","purple","pink","yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
    

#4
from tkinter import *
window = Tk()
window.title("welcome to likegeeks app")
window.geometry('350x200')
lbl = Label(window,text="hello")
lbl.grid(column=0,row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

#5
import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choise, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""Choose your favourite programming language:"""
         justify = tk.LEFT,
         padx = 20).pack()
for val, language in enumerate(languages):
    tk.radiobutton(root,
                   text=language,
                   padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)
root.mainloop()

#6
from tkinter import *

def NewFile():
    print("New File!")
def About():
    print("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Ten", menu=filemenu)
filemenu.add_command(label="ho va ten", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="exit", comman=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="mật khẩu", menu=helpmenu)
helpmenu.add_command(label="mât khau:.", command=About)

mainloop()

#7
# import the modules
import tkinter
import random

#list of posside colour.
colour = ['Red','Blue','Green','Pink','Black','Yellow','Orange','While','Purple','Brown']
score = 0

# the game time left, initially 30 seconds.
timeleft = 30

#funtion that will start the game.
def startGame(event):

    if timeleft == 30:

        # start the countdown timer.
        countdown()

    #run the function to
    #choose the next colour.
    nextColour()

# Function to choose and
# display the next colour.
def nextColour():

    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft

    # if a game is curently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():

            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))
        # update the score.
        scoreLabel.confif(text = "Score: "+str(score))
# Countdow timer function
def countdown():

    global timeleft

    # if a game is in play
    if timeleft > 0:

        # decrement the timer.
        timeleft -= 1

        #update the time left label
        timeLabel.config(text = "Time left: "
                         + str(timeleft))
        #run the function again after 1 second.
        timeLabel.after(1000, countdown)

# Driver Code

# create a GUI window
root = tkinter.Tk()

#set the title
root.title("COLORGAME")

#set the size
root.geometry("375x200")

# add an instructions label
instructions = tkinter.Label(root, text = "Type in the colour"
                             " of the words, and not the word text!",
        font = ('Helvetica', 12))
instructions.pack()

# add a score label
timeLabel = tkinter.Label(root, text = "Time left: " +
                          str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))

label.pack()

# add a text antry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
