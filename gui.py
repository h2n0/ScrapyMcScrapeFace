import scrappy,webbrowser
from tkinter import *
from tkinter import messagebox as tkMessageBox##easy compat




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
class scraper_main:
    #vars
    #top = 0
    #entry = 0
    #status = 0
    def __init__(self):
        #tkinit
        self.top = Tk()
        self.top.title("Scrapper V0.1")
        self.top.resizable(width=False, height=False)
        ##preinit
        self.resizeWindow(400, 300)
        ##vars
        self.entry_VAR = StringVar()##holds text from entry
        self.status = StringVar()
        ##varset
        self.setStatus("Testing")
        ##widgets

        entry = Entry(self.top,textvariable = self.entry_VAR).pack()#.place(relx=0.5,rely=0.5,anchor="center")
        #entry.place(x=100, y=100)
        #entry.place(relx=0.5,rely=0.5,anchor="center")

        btn = Button(self.top, text="Scrape", command=self.scrape).pack()
        #btn.place(relx=0.5,rely=0.6,anchor="center")

        
        
        l = Label(self.top, textvariable=self.status).pack()
        #l.place(relx=0.5,rely=0.2, anchor="center")

        ##mainloop
        self.top.mainloop()

    def resizeWindow(self,w,h):
        self.top.geometry('{}x{}'.format(w, h))
  
    def setStatus(self,s):
        self.status.set(s)

    def scrape(self):
      album = self.entry_VAR.get()
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
        
          self.setStatus("It worked")
        except:
          warn("An error has occoured\nPlease double check the ID given")
          self.setStatus("An error occured somewhere")
  

#def scrape():
#  album = entry.get()
#  if(album == ""):
#    warn("No album ID given")
#  else:#Album ID is not empty
#    try:
#      info("Going to scrape this album\nThis might take a while")
#      scrappy.lookAtAlbum(album)
#      if ask("Want to see the downloaded files?"):
#        url = "{}".format(scrappy.cd)
#        print(url)
#        webbrowser.open(url)
        
#      setStatus("It worked")
#    except:
#      warn("An error has occoured\nPlease double check the ID given")
#      setStatus("An error occured somewhere")
  
#def resizeWindow(w,h):
#  top.geometry('{}x{}'.format(w, h))
  
#def setStatus(s):
#  status.set(s)
  
#Does what it says on the tin really
#def setupGUI():
#  global top, entry, status
#  top = Tk()
#  top.title("Scrapper V0.1")
#  top.resizable(width=False, height=False)
  
#  resizeWindow(400, 300)
  
#  entry = Entry(top)
#  entry.pack()
#  #entry.place(x=100, y=100)
#  entry.place(relx=0.5,rely=0.5,anchor="center")
  
#  btn = Button(top, text="Scrape", command=scrape)
#  btn.pack()
#  btn.place(relx=0.5,rely=0.6,anchor="center")
  
#  status = StringVar()
#  setStatus("Testing")
  
#  l = Label(top, textvariable=status)
#  l.pack()
#  l.place(relx=0.5,rely=0.2, anchor="center")

#setupGUI()##moved to init of class
#top.mainloop()##same
s_main = scraper_main()