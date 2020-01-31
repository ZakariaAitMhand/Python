from dirsync import sync
from tkinter import *
from tkinter import filedialog
from datetime import date
import time
import base64
import os
from iconCode import IconCode




class Synchrone(object):
	"""
		Synchrone is a class defining 
		the components
		the functionalities 
		of the GUI enabling the end user 
		to synchronize a destination folder with a souce folder
		this was developped by Zakaria Ait Mhand
	"""
	def __init__(self, window):
		self.window = window
		self.source_folder = StringVar()
		self.source_folder.set("chemin de dossier source")
		self.destination_folder = StringVar()
		self.destination_folder.set("chemin de dossier destination")

		self.button_src = Button(self.window, height=2, width=25, text="Source", command=self.browse_button_src)
		self.button_src.grid(row=1, column=1, padx=5, pady=5)
		self.lbl_src = Label(self.window, textvariable=self.source_folder)
		self.lbl_src.grid(row=1, column=2)

		self.button_dest = Button(self.window, height=2, width=25, text="Destination", command=self.browse_button_dest)
		self.button_dest.grid(row=2, column=1, padx=5, pady=5)
		self.lbl_dest = Label(self.window, textvariable=self.destination_folder)
		self.lbl_dest.grid(row=2, column=2)

		self.button_sync_once = Button(self.window, height=2, width=25, text="Synchronisation instantanée", command=self.sync_folders_once, state=DISABLED)
		self.button_sync_once.grid(row=3, column=1, padx=5, pady=5)

		self.button_sync1h = Button(self.window, height=2, width=25, text="Synchronisation Continue 1h", command=self.sync_folders_1h, state=DISABLED)
		self.button_sync1h.grid(row=3, column=2, padx=5, pady=5)

		self.button_sync4h = Button(self.window, height=2, width=25, text="Synchronisation Continue 4h", command=self.sync_folders_4h, state=DISABLED)
		self.button_sync4h.grid(row=4, column=1, padx=5, pady=5)

		self.button_sync24h = Button(self.window, height=2, width=25, text="Synchronisation Continue 24h", command=self.sync_folders_24h, state=DISABLED)
		self.button_sync24h.grid(row=4, column=2, padx=5, pady=5)
		
	def sync_folders_1h(self):
		hours = 1
		self.sync_folders(hours);
	def sync_folders_4h(self):
		hours = 4
		self.sync_folders(hours);
	def sync_folders_24h(self):
		hours = 24
		self.sync_folders(hours);

	def sync_folders(self, nbh):
		sleepTime = 60
		hour = sleepTime * 60
		counter = 0
		tday = str(date.today())
		dest = self.destination_folder.get()
		while(counter<hour*nbh):
			self.window.withdraw()
			counter+=sleepTime
			sync(self.source_folder.get(), self.destination_folder.get()+ "/" +tday, 'sync', verbose=True, create=True)
			time.sleep( sleepTime )
		self.window.deiconify()

	def sync_folders_once(self):
	    tday = str(date.today())
	    dest = self.destination_folder.get()
	    sync(self.source_folder.get(), self.destination_folder.get()+ "/" +tday, 'sync', verbose=True, create=True)
	    time.sleep( 5 )
	def stateToNormal(self):
		self.button_sync_once.config(state="normal")
		self.button_sync1h.config(state="normal")
		self.button_sync4h.config(state="normal")
		self.button_sync24h.config(state="normal")

	def stateToDisable(self):
		self.button_sync_once.config(state="disabled")
		self.button_sync1h.config(state="disabled")
		self.button_sync4h.config(state="disabled")
		self.button_sync24h.config(state="disabled")
		
	def browse_button_src(self):
		askdirectory = filedialog.askdirectory()
		filename = askdirectory if os.path.isdir(askdirectory) else "chemin de dossier source"
		self.source_folder.set(filename)
		if os.path.isdir(self.source_folder.get()) and os.path.isdir(self.destination_folder.get()):
			self.stateToNormal()
		else:
			self.stateToDisable()

	def browse_button_dest(self):
		askdirectory = filedialog.askdirectory()
		filename = askdirectory if os.path.isdir(askdirectory) else "chemin de dossier destination"
		self.destination_folder.set(filename)
		if os.path.isdir(self.source_folder.get()) and os.path.isdir(self.destination_folder.get()):
			self.stateToNormal()
		else:
			self.stateToDisable()




window = Tk()
window.title('Synchrone')
# window.geometry('450x205')
window.geometry('450x205')
window.resizable(1,0)
window.maxsize(700, 205)

iconCode = IconCode();
icondata= base64.b64decode(iconCode.getIconCode())
## The temp file is icon.ico
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()
window.wm_iconbitmap(tempFile)
## Delete the tempfile
os.remove(tempFile)
# wm_iconbitmap(tempFile)

# if os.path.exists(os.path.join(os.getcwd(),"icon.ico")):
# 	icon = os.path.join(os.getcwd(),"icon.ico")
# 	window.iconbitmap(icon)
# 	window.wm_iconbitmap(icon)

Syn = Synchrone(window);

mainloop()