#!/usr/bin/python3
"""
linver 1.0.0 - made by @techguy16
Probably the best recreation of Winver for Linux

Yes it is very incomplete, due to not having a banner for every distro,
but hey - it works.
"""
from tkinter import *
from tkinter import ttk
import os
import distro
import socket

os.system('uname -r > version.txt')
version_file=open('version.txt')
version = "Kernel build " + version_file.read()
version_file.close()

os.system('echo $USER > username.txt')
usern=open('username.txt')
username = usern.read()
usern.close()

hostname = socket.gethostname()

distrov = distro.name()
titlebartext = "About " + distrov
distrover = distro.version()
distrocode = distro.codename()
distroversion = "Version " + distrover + " (" + distrocode + ")"

root = Tk()
root.title(titlebartext)
root.geometry("450x420")
root.resizable(False,False)

"""
This section only changes the distro name to add the company (if applicable).
Not all distros have a company or organisation supporting them, so linver will
just display the distro name.
"""
if distrov == 'Pop!_OS':
    distrov = 'System76 Pop!_OS'
if distrov == 'Ubuntu':
    distrov = 'Canonical Ubuntu'
if distrov == 'Kali GNU/Linux':
    distrov = 'Offensive Security Kali Linux'
if distrov == 'openSUSE':
    distrov = 'SUSE openSUSE'

"""
The code that closes the window lives here.
"""
def close():
    root.destroy()

"""
This section chooses the correct photo for the currently running Linux distro
"""
if distrov == 'System76 Pop!_OS':
    path = PhotoImage(file='assets/PopOS.png')
elif distrov == 'Canonical Ubuntu':
    path = PhotoImage(file='assets/Ubuntu.png')
elif distrov == 'Linux Mint':
    path = PhotoImage(file='assets/LinuxMint.png')
else:
    path = PhotoImage(file="assets/Linux.png")

"""
I guess this is the code that actually produces the window.
"""
label_image = Label(root, image=path,width=430, height=90)
label_image.image = path
label_image.place(x=10, y=10)
distrolabel = Label(root, text=distrov)
distrolabel.place(x=20, y=115)
distrover = Label(root, text=distroversion)
distrover.place(x=20, y=135)
kernelver = Label(root, text=version)
kernelver.place(x=20, y=155)
licensetext = Label(root, text="The Linux kernel is protected under the GNU General Public\n\
Licence in the United States and other countries/regions.", justify=LEFT)
licensetext.place(x=20, y=200)
tolicense = Label(root, text="This product is registered to:", justify=LEFT)
tolicense.place(x=20, y=260)
usernametext = Label(root, text=username, justify=LEFT)
usernametext.place(x=50, y=280)

hostnametext = Label(root, text=hostname, justify=LEFT)
hostnametext.place(x=50, y=300)
okbutton = Button(root, text='OK', command=close, width=8)
okbutton.place(x=345, y=377)

# For compatibility. That's it.
root.mainloop()

# If you made it this far, take a breather.
