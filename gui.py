from logo64 import imgData
from lang import lang, buttons
from start import installApp, installData, installAppData, uninstalAll, backupData
from local import innerPath, Ul, Folder, OSdist
from vars import appName
from rtl import rtl
import time
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sys
from threading import Timer
from tkinter.ttk import Progressbar


f = Folder()
f.exist()


def ext():
    sys.exit()


class Gui:

    foreg = "#BFBFBF"
    backg = "#333333"
    red = "#803430"
    yelw = "#807D1D"
    green = "#2D806D"
    rootH = 500
    rootW = 550
    imageLogo = "img/logoInstall.png"
    imageData = imgData

    root = Tk()

    def ct(self, x):
        self._curStateLabelText.set(str(lang[Ul][x]))

    def exitBut(self, x):
        self.cancelButt.destroy()
        self.installButt.destroy()
        self.uninstButt.destroy()
        Button(self.fbuttons, relief='flat',
               text=buttons[Ul][10], bd=0, command=x).pack(padx=20, side=LEFT)

    def afterInstall(self):
        f.exist()
        self.pBar.destroy()
        if f.dataExists and f.dataExists:
            self.curStateLabel.config(fg=self.green)
            self.ct(65)

        else:
            self.curStateLabel.config(fg=self.red)
            self.ct(68)

    def afterUnInstall(self):
        f.exist()
        if not f.dataExists and not f.dataExists:

            time.sleep(5)
            self.curStateLabel.config(fg=self.green)
            self.ct(67)

        else:
            self.curStateLabel.config(fg=self.red)
            self.ct(68)

    def installAppGui(self):
        def x():
            pBar()
            installApp()
            self.afterInstall()

        def z():
            self.ct(64)
            self.exitBut(ext)

        def pBar():
            self.pBar = Progressbar(
                self.root, orient=HORIZONTAL, length=200, mode="determinate", takefocus=True, maximum=100)
            self.pBar.pack()
            for i in range(100):
                self.pBar.step()
                self.root.update()

        def y():
            pBar()
            installApp()
            installData()
            self.afterInstall()

        if f.dataExists:
            z()
            x()

        if not f.dataExists:
            z()
            y()

    def installDataGui(self):
        installData()
        ext()

    def installAppDataGui(self):
        installAppData()
        ext()

    def uninstalAllGui(self):
        def x():
            uninstalAll()
            self.afterUnInstall()

        def y():
            self.ct(66)
            self.exitBut(ext)

        t = Timer(2, x)
        t.start()

        y()

    def backupDataGui(self):
        backupData()
        ext()

    def initialGui(self):
        # MAIN WIN

        self.root.title(appName.upper() + ' ' + buttons[Ul][8])
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(
            self.root.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - windowHeight / 2 -
                           (self.rootH / 2))
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.root.geometry(str(self.rootH) + "x" + str(self.rootW))
        self.root["bg"] = self.backg

        # LOGO
        ''' logo = ImageTk.PhotoImage(file=innerPath + str(self.imageLogo)) '''
        logo = PhotoImage(data=self.imageData)
        flogo = Frame(self.root)
        flogo.pack()
        logoLabel = Label(flogo, bg=self.backg, image=logo)
        logoLabel.pack()

        # WELCOME
        text1 = buttons[Ul][7]
        text2 = appName.upper()
        text3 = buttons[Ul][8]
        introLabel1 = Label(self.root, text=text1, font=(None, 16),
                            bg=self.backg, fg=self.foreg)
        introLabel2 = Label(self.root, text=text2, font=(None, 18),
                            bg=self.backg, fg=self.foreg)
        introLabel3 = Label(self.root, text=text3, font=(None, 16),
                            bg=self.backg, fg=self.foreg)
        introLabel1.pack()
        introLabel2.pack()
        introLabel3.pack()

        # CURRENT STATE
        self._curStateLabelText = StringVar()
        if f.appExists:
            if f.dataExists:
                self.curStateLabelText = lang[Ul][60]
            if not f.dataExists:
                self.curStateLabelText = lang[Ul][62]
        if not f.appExists:
            if f.dataExists:
                self.curStateLabelText = lang[Ul][63]
            if not f.dataExists:
                self.curStateLabelText = lang[Ul][61]
        self._curStateLabelText.set(str(self.curStateLabelText))
        self.curStateLabel = Label(self.root, textvariable=self._curStateLabelText, font=(
            None, 12), pady=10, bg=self.backg, fg=self.yelw)
        self.curStateLabel.pack()

        # BUTTONS
        # ok = rtl(buttons[Ul][1])
        cancel = rtl(buttons[Ul][2])
        uninst = rtl(buttons[Ul][5])
        if f.appExists:
            inst = rtl(buttons[Ul][9])
        if not f.appExists:
            inst = rtl(buttons[Ul][4])
        self.fbuttons = Frame(self.root, bg=self.backg)
        self.fbuttons.pack(side=BOTTOM, pady=40)

        self.installButt = Button(self.fbuttons, relief='flat', text=inst,
                                  bd=0, command=self.installAppGui)
        self.uninstButt = Button(self.fbuttons, relief='flat',
                                 text=uninst, bd=0, command=self.uninstalAllGui)
        self.cancelButt = Button(self.fbuttons, relief='flat',
                                 text=cancel, bd=0, command=ext)
        if f.appExists:
            if f.dataExists:
                self.cancelButt.pack(padx=20, side=LEFT)
                self.installButt.pack(padx=20, side=LEFT)
                self.uninstButt.pack(padx=20, side=LEFT)
            if not f.dataExists:
                self.cancelButt.pack(padx=20, side=LEFT)
                self.installButt.pack(padx=20, side=LEFT)
                self.uninstButt.pack(padx=20, side=LEFT)
        if not f.appExists:
            if f.dataExists:
                self.cancelButt.pack(padx=20, side=LEFT)
                self.installButt.pack(padx=20, side=LEFT)
            if not f.dataExists:
                self.cancelButt.pack(padx=20, side=LEFT)
                self.installButt.pack(padx=20, side=LEFT)

        self.root.mainloop()

    def currentState(self):
        pass

    def progressBar(self):
        pass

    def t(self):
        pass
