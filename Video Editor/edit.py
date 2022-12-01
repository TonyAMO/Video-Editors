import tkinter as tk
from tkinter import *


class editButton(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        menubar.add_cascade(label='Edit', menu=fileMenu)