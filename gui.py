import scrappy
from Tkinter import *
import tkMessageBox
import webbrowser

#Gobal decleration
top = 0
entry = 0
status = 0


#Utility function, not sure if needed or not yet. We'll see
def info(b):
  tkMessageBox.showinfo("Info",b)
  
#Another utility function for good mesaure
def warn(b):
  tkMessageBox.showwarning("Warning",b)

#More utilitys
def ask(q):
  return tkMessageBox.askyesno("Question", q)

#THe main funtion called by the button press
def scrape():
  album = entry.get()
  if(album == ""):
    warn("No album ID given")
  else:#Album ID is not empty
    try:
      info("Going to scrape this album\nThis might take a while")
      scrappy.lookAtAlbum(album)
      if ask("Want to see the downloaded files?"):
        url = "{}".format(scrappy.cd)
        print(url)
        webbrowser.open(url)
        
      setStatus("It worked")
    except:
      warn("An error has occoured\nPlease double check the ID given")
      setStatus("An error occured somewhere")
  
def resizeWindow(w,h):
  top.geometry('{}x{}'.format(w, h))
  
def setStatus(s):
  status.set(s)
  
#Does what it says on the tin really
def setupGUI():
  global top, entry, status
  top = Tk()
  top.title("Scrapper V0.1")
  top.resizable(width=False, height=False)
  
  resizeWindow(400, 300)
  
  entry = Entry(top)
  entry.pack()
  #entry.place(x=100, y=100)
  entry.place(relx=0.5,rely=0.5,anchor="center")
  
  btn = Button(top, text="Scrape", command=scrape)
  btn.pack()
  btn.place(relx=0.5,rely=0.6,anchor="center")
  
  status = StringVar()
  setStatus("Testing")
  
  l = Label(top, textvariable=status)
  l.pack()
  l.place(relx=0.5,rely=0.2, anchor="center")

setupGUI()
top.mainloop()