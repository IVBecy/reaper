# A ransomware written in Python

```python
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
 ```

# Features:
- [x] Encrypt files in any directory
- [x] Decrypt any file that has been decrypted.
- [x] Iterate over any sub directory and encrypt everything inside it.

# To do:
- [] If there are duplicate files, one of them cannot be encrypted

# How to use:
- **1**: Run ```create_key.py``` and change ALL instances of self.key in ```reaper.py``` to the key that you've just got from ```create_key.py```.
- **2**: Change the ```DIR``` variable in ```reaper.py```.
- **3**: Run ```py reaper.py -t```  to encrypt all the files, or just use ```run.sh```.
- **4**: If you want everything to be decrypted use ```py reaper.py -r```.
