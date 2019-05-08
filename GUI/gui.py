from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from lang import heb
from vars import appName
from local import innerPath


foreg = "#bdbec2"
backg = "#333333"
ok = heb("המשך")
cancel = heb("בטל")
uninst = heb("הסר")
rootH = 500
rootW = 500

# ------ROOT Window
root = Tk()
root.title(appName.upper() + " Installation")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2 -
                   (rootH / 2))

root.geometry("+{}+{}".format(positionRight, positionDown))
root.geometry(str(rootH) + "x" + str(rootW))
root["bg"] = backg
# ----------
image1 = "img/logoInstall.png"
image2 = "img/installingGif.png"

logo = ImageTk.PhotoImage(file=innerPath + str(image1))
flogo = Frame(root)
flogo.pack()
logoLabel = Label(flogo, bg=backg, image=logo)

logoLabel.pack()

installingFrame = Frame(root, bg=backg)
# installing = AnimatedGif(installingFrame, "installingGif.gif", 0.04)
# installing = ImageTk.PhotoImage(file=innerPath + str(image2))
# installingLabel = Label(installingFrame, bg=backg, image=installing)

t1 = heb(" ברוכים הבאים לאשף התקנה של ")
t2 = appName.upper()

introLabel1 = Label(root, text=t1, font=(None, 18), bg=backg, fg=foreg)
introLabel2 = Label(root, text=t2, font=(None, 18), bg=backg, fg=foreg)
introLabel1.pack()
introLabel2.pack()


fbuttons = Frame(root, bg=backg)
fbuttons.pack(side=BOTTOM, pady=40)
okButt = Button(fbuttons, relief='flat', text=ok, bd=0, command=start)
okButt.pack(padx=20, side=LEFT)
cancelButt = Button(fbuttons, relief='flat',
                    text=cancel, bd=0, command=quit)
cancelButt.pack(padx=20, side=LEFT)
uninstButt = Button(fbuttons, relief='flat',
                    text=uninst, bd=0, command=uninstall)
uninstButt.pack(padx=20, side=LEFT)
root.mainloop()
