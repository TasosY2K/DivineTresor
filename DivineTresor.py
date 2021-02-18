#DivineTresor
from tkinter import filedialog
import tkinter
from tkinter import simpledialog
import pyAesCrypt
import os, sys

extension = ".divine"

def foldercrypt():
    folder = filedialog.askdirectory()
    file = simpledialog.askstring(title="Key", prompt="Encryption key:")
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename != os.path.basename(sys.argv[0]) or os.path.splitext(filename)[1] != extension:
                try:
                    os.chdir(root)
                    pyAesCrypt.encryptFile(filename, filename + extension, file, bufferSize)
                    os.unlink(filename) #warning it deletes the unecrypted file!
                except:
                    pass

def folderdecrypt():
    folder = filedialog.askdirectory()
    file = simpledialog.askstring(title="Key", prompt="Decryption key:")
    for root, dirs, files in os.walk(folder):
        for filename in files:
            try:
                os.chdir(root)
                pyAesCrypt.decryptFile(filename, filename.split(extension)[0], file, bufferSize)
                os.unlink(filename)
            except:
                pass

def filecrypt():
    files = filedialog.askopenfilenames()
    file = simpledialog.askstring(title="Key", prompt="Encryption key:")
    for filename in files:
            try:
                pyAesCrypt.encryptFile(filename, filename + extension, file, bufferSize)
                os.unlink(filename)
            except Exception as e:
                print(e)

def filedecrypt():
    files = filedialog.askopenfilenames()
    file = simpledialog.askstring(title="Key", prompt="Decryption key:")
    for filename in files:
            try:
                pyAesCrypt.decryptFile(filename, filename.split(extension)[0], file, bufferSize)
                os.unlink(filename)
            except Exception as e:
                print(e)

window = tkinter.Tk()#.withdraw()
window.wm_title("Divine Tresor")
window.config(background = "#FFFFFF")
greeting = tkinter.Label(text="Welcome to the Divine Tresor, may your files be safe!").pack()
filenc = tkinter.Button(
    text="Encrypt files",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = filecrypt,
).pack()
filedec = tkinter.Button(
    text="Decrypt files",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = filedecrypt,
).pack()
folderenc = tkinter.Button(
    text="Encrypt a folder",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = foldercrypt,
).pack()
folderdec = tkinter.Button(
    text="Decrypt a folder",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = folderdecrypt,
).pack()
bufferSize = 64 * 1024

if __name__ == "__main__":
    window.mainloop()

