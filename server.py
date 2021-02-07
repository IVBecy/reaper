# Modules
import socket,sys
from cryptography.fernet import Fernet

# Variables
PORT = 80
MAX_INCOMING = 200

# Sending key to recipient
def listen_and_send():
  s = socket.socket()
  s.bind(("0.0.0.0", 80))
  try:
    s.listen(MAX_INCOMING)
  except KeyboardInterrupt:
    print("Exiting...")
    sys.exit() 
  conn,addr = s.accept()
  print(f"New connection: {addr[0]}:{addr[1]}\nSending key...")
  conn.send(Fernet.generate_key())
    
# Main
if __name__ == "__main__":
  print("Server up!")
  while True:
    listen_and_send()
