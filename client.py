import tkinter
from functools import partial
import socket
import _thread
import time

win = 0
lose = 0
client = 0
colors = ['purple','blue','green','yellow','orange','red']
buttonClicked = False   
def check (color):
    global win
    global lose
    if(color == colorLabel['fg']):
        win += 1
        wonLabel['text']='Won: '+str(win)
    else:
        lose += 1
        loseLabel['text']='Lost: '+str(lose)
    global buttonClicked 
    buttonClicked = True
    reset()
def reset ():
    client.send('x'.encode('ascii'))
def socketCreation():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 7510
    c.connect((host,port))
    global client
    client = c
    global livesRemaining
    while True:
        msg= c.recv(2048).decode('ascii')
        for color in colors:
            if(color[0] == msg[0]):
                colorLabel['text']= color
            if(color[0] == msg[1]):
                colorLabel['fg']= color
        for i in range(10,0,-1):
            timerLabel['text']='Time: '+str(i)
            global buttonClicked
            if(buttonClicked):
                buttonClicked = False
                break
            time.sleep(1)
        reset()
        
#Window
window = tkinter.Tk()
window.title("Hangman")
window['bg']='white'
window['padx']=15
window['pady']=15
#Win Label
wonLabel = tkinter.Label(window)
wonLabel['font']=("",18)
wonLabel['bg']='white'
wonLabel['text']='Won: '+str(win)
wonLabel['fg']='green yellow'
wonLabel.grid(column=1,row=1,padx=5,pady=5)
#Lose Label
loseLabel = tkinter.Label(window)
loseLabel['font']=("",18)
loseLabel['bg']='white'
loseLabel['text']='Lost: '+str(lose)
loseLabel['fg']='firebrick1'
loseLabel.grid(column=1,row=2,padx=5,pady=5)
#Timer
timerLabel = tkinter.Label(window)
timerLabel['font']=("",18)
timerLabel['bg']='white'
timerLabel['text']='Time: 10'
timerLabel.grid(rowspan=2,column=5,row=1,padx=20,pady=5)    
#Color To Guess
colorLabel = tkinter.Label(window)
colorLabel['font']=("",25)
colorLabel['bg']='white'
colorLabel.grid(columnspan=3,column=2,row=3,padx=5,pady=5)
#Buttons   
#RED   
redButton = tkinter.Button(window)
redButton['relief']=tkinter.FLAT
redButton['bg']='red'
redButton['width']= 8
redButton['height']= 4
redButton['command']=partial(check,'red')
redButton.grid(column=2,row=4,padx=5,pady=5)
#ORANGE
orangeButton = tkinter.Button(window)
orangeButton['relief']=tkinter.FLAT
orangeButton['bg']='orange'
orangeButton['width']= 8
orangeButton['height']= 4
orangeButton['command']=partial(check,'orange')
orangeButton.grid(column=3,row=4,padx=5,pady=5)
#YELLOW
yellowButton = tkinter.Button(window)
yellowButton['relief']=tkinter.FLAT
yellowButton['bg']='yellow'
yellowButton['width']= 8
yellowButton['height']= 4
yellowButton['command']=partial(check,'yellow')
yellowButton.grid(column=4,row=4,padx=5,pady=5)
#GREEN
greenButton = tkinter.Button(window)
greenButton['relief']=tkinter.FLAT
greenButton['bg']='green'
greenButton['width']= 8
greenButton['height']= 4
greenButton['command']=partial(check,'green')
greenButton.grid(column=2,row=5,padx=5,pady=5)
#BLUE
blueButton = tkinter.Button(window)
blueButton['relief']=tkinter.FLAT
blueButton['bg']='blue'
blueButton['width']= 8
blueButton['height']= 4
blueButton['command']=partial(check,'blue')
blueButton.grid(column=3,row=5,padx=5,pady=5)
#PURPLE
purpleButton = tkinter.Button(window)
purpleButton['relief']=tkinter.FLAT
purpleButton['bg']='purple'
purpleButton['width']= 8
purpleButton['height']= 4
purpleButton['command']=partial(check,'purple')
purpleButton.grid(column=4,row=5,padx=5,pady=5)
#Socket Initialization
_thread.start_new_thread(socketCreation, () )
window.mainloop()