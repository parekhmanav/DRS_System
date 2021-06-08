import tkinter
from tkinter.constants import RIDGE
# from tkinter.constants import ANCHOR, NW
import cv2  
import PIL.Image, PIL.ImageTk
from functools import partial
import threading #Threading in python is used to run multiple threads (tasks, function calls) at the same time. 
import time
import imutils
# cv2 use for image processing, video capture 


# 2nd Step  ///////////////////////////
# Global var - width , height
WIDTH = 650
HEIGHT = 368


# 6st Step  ///////////////////////////
stream = cv2.VideoCapture("drs22.mp4")


# 1st Step  ///////////////////////////
# tkinter window 
root = tkinter.Tk()
root.title("  Decision Review System by Manav ")   #title

# Images First 
cv_img = cv2.cvtColor(cv2.imread("first.jpg"),cv2.COLOR_RGB2BGR)
canvas = tkinter.Canvas(root, width=650, height=368,highlightthickness=2,highlightbackground="black")
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_canvas = canvas.create_image(0,0,ancho =tkinter.NW,image=photo)
canvas.pack()

# 4th Step  ///////////////////////////

def play(speed):
    print("Play speed is {speed}")
    
    fram1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,fram1 + speed)

    grabbed , fram = stream.read()
    fram = imutils.resize(fram,width = WIDTH,height=HEIGHT)
    fram = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(fram))
    canvas.image = fram
    canvas.create_image(0,0,image = fram ,ancho =tkinter.NW)


# 5th Step  ///////////////////////////

def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon =1
    thread.start()
    print(" OUT ")

def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon =1
    thread.start()
    print(" NOT OUT ")

def pending(decision):
    fram = cv2.cvtColor(cv2.imread("decision.jpg"),cv2.COLOR_BGR2RGB)
    fram = imutils.resize(fram , width=WIDTH,height=HEIGHT)
    fram = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(fram))
    canvas.image = fram
    canvas.create_image(0,0,image = fram ,ancho =tkinter.NW)

    time.sleep(1.5)
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not-out.png"
    fram = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    fram = imutils.resize(fram , width=WIDTH,height=HEIGHT)
    fram = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(fram))
    canvas.image = fram
    canvas.create_image(0,0,image = fram ,ancho =tkinter.NW)
    

# 3rd Step  ///////////////////////////
# buttons 

btn = tkinter.Button(root,text="<< Previous (Fast)"  , width=50, command=partial(play,-25), bg="grey",font="Helvetica 10 bold",fg="blue",relief=RIDGE)
btn.config( width = 20 )
btn.pack(pady=2)

btn = tkinter.Button(root,text="<< Previous (Slow)" , width=50, command=partial(play,-2),bg="grey",font="Helvetica 10 bold",fg="blue",relief=RIDGE)
btn.config( width = 20 )
btn.pack(pady=2)

btn = tkinter.Button(root,text="Forward (Fast) >> " , width=50, command=partial(play,25),bg="grey",font="Helvetica 10 bold",fg="blue",relief=RIDGE)
btn.config( width = 20 )
btn.pack(pady=2)

btn = tkinter.Button(root,text=" Forward (Slow) >>" , width=50, command=partial(play,1),bg="grey",font="Helvetica 10 bold",fg="blue",relief=RIDGE)
btn.config( width = 20 )
btn.pack(pady=2)

btn = tkinter.Button(root,text="OUT" ,width=50 ,command=out ,bg="red",font="Helvetica 10 bold",relief=RIDGE)
btn.config( width = 20 )
btn.pack(pady=2)

btn = tkinter.Button(root,text="NOT OUT" ,width=50,command=not_out,bg="skyblue",font="Helvetica 10 bold",relief=RIDGE)
btn.config( width = 20 )
btn.pack(pady=2)

root.mainloop()