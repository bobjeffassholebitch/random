from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Button, E, Entry, LabelFrame, Menu
from tkinter import messagebox, Tk, W, PhotoImage
from random import randint, choice
from PIL import Image, ImageDraw, ImageTk

import webbrowser


def keyboard():
    Label(screen3, text="Spam Starts In: 25s", bg="red", height="1", width="300", font=("Calibri", 13)).pack()
    execfile('Keyboard-Killer.py')
    
def email():
    execfile('Email-Killer.py')


def web1():
    webbrowser.open(url, new=new)
    
    
def notepad():
    execfile('CH-Notepad.py')
    
    
def settings():
    screen2 = Toplevel()
    screen2.title("Settings")
    screen2.geometry("300x300")
    screen2.configure(bg='black')
    
    lab3 = Button(screen2, text="Credits",fg="#8F00FF", bg="black",highlightbackground="#8F00FF",highlightthickness=0).pack()
    
    lab4 = Button(screen2, text="Updates",fg="#8F00FF", bg="black",highlightbackground="#8F00FF",highlightthickness=0).pack()
    
    lab5 = Button(screen2, text="Notepad",fg="#8F00FF", bg="black",command=notepad, highlightbackground="#8F00FF",highlightthickness=0).pack()

def main_screen():
    global new
    global url


    screen = Tk()
    screen.geometry("520x300")
    screen.configure(bg="black")
    screen.title("")
    new = 1
    url = "https://discord.gg/MwDr6Pr"


    ico = Image.open('Images/snake.jpg')
    photo = ImageTk.PhotoImage(ico)
    screen.wm_iconphoto(False, photo)


    load = Image.open("Images/image0.jpg")
    load = load.resize((520,300), Image.ANTIALIAS)
    load.save("Images/image0.jpg")
    load = ImageTk.PhotoImage(file='Images/image0.jpg')
    load.Artwork=Label(screen, image=load)
    load.Artwork.pack()

    lab2 = Label(screen, text="Cobra-zCode", bg="black", fg="#8F00FF", font=("geogia", 20, "bold", "italic"))
    lab2.place(relx=1, x=167, y=0, width="1000", anchor=NE)


    lab3 = Label(screen, text="The AceViruses Community", bg="black" , height="1", width="23", fg="#8F00FF", font=("geogia", 10, "bold", "italic"))
    lab3.place(relx=1, x=-11, y=0, anchor=NE)
    
    lab3 = Label(screen, text="Made For: Hackers&Modders", bg="black", height="1", width="23", fg="#8F00FF", font=("geogia", 7, "bold", "italic"))
    lab3.place(relx=1, x=-30, y=18, anchor=NE)

    b2 = Button(screen, text="Settings", bg="black", highlightcolor="orange",highlightthickness=0, bd=0, fg="#8F00FF", command=settings,font="geogia")
    b2.place(relx=1, x=-430, y=2, anchor=NE)

    b1 = Button(screen, text="Discord", bg="purple3",highlightbackground="black",highlightthickness=2,command=web1 ,bd=0, fg=("black"))
    b1.place(relx=1, x=0, y=35, anchor=NE)

    b4 = Button(screen, text="Email-Killer", bg="purple3",highlightbackground="black",highlightthickness=2,command=email, bd=0, fg=("black"))
    b4.place(relx=1, x=-416, y=65, anchor=NE)
    
    b0 = Button(screen, text="Keyboard-Killer", bg="purple3",highlightbackground="black",highlightthickness=2 ,command=keyboard,bd=0, fg=("black"))
    b0.place(relx=1, x=-391, y=35, anchor=NE)



    screen.mainloop()

main_screen()
