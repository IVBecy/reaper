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
- [X] Take bitcoin payment to any wallet (Payment does not work).

# DISCLAIMER:
- This is a proof of concept, it wasn't designed to harm anyone. If you use it for unethical purposes
I take no responsibility, if the script was used in a bad manner.

# How to use:
 - 1: Change the `DIR,TARGET_WALLET,AMOUNT_OF_BITCOIN,KEY` variables to make sure that your information is in the script.
 - 2: Run `create-key.py` to get an encryption key.
 - 3: Run `pip install -r requirements.txt` to get the libraries installed.
 - 4: Run `py reaper.py -t`.

 - ALL IN ONE: Start `run.sh`. Pip and packages will be installed and the script will start.

