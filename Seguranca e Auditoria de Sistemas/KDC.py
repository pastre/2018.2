#https://userpages.umbc.edu/~dgorin1/451/security/dcomm/keydist.htm
from Crypto.Cipher import AES

import base64
import random

def encrypt(key, string):
  cipher = AES.new(key.rjust(32) ,AES.MODE_ECB)
  encoded = base64.b64encode(cipher.encrypt(string.rjust(32)))
  return encoded
def decrypt(key, string):
  cipher = AES.new(key.rjust(32) ,AES.MODE_ECB)  
  decoded = cipher.decrypt(base64.b64decode(string.rjust(32)))
  return decoded.strip().decode('utf-8')

class KDC:
    def __init__(self):
        self.keys = {'alice': 'keyAlice'.rjust(32), 'bob': 'keyBo'.rjust(32)}

    def generate_session_key(self, u1, u2):
        u1 = decrypt(kdc.keys['alice'], u1)
        u2 = decrypt(kdc.keys['alice'], u2)
        
        r1 = str(random.getrandbits(32)).rjust(32)
        
        return encrypt(self.keys[u1], r1), encrypt(self.keys[u2], u1), encrypt(self.keys[u2], r1)
        
class Alice:
    def __init__(self):
        self.name = 'alice'
    def request_session_key(self, kdc, user):
        u1 = encrypt(kdc.keys[self.name], self.name)
        u2 = encrypt(kdc.keys[self.name], user.name)
        r1, ba, br1 = kdc.generate_session_key(u1, u2)
        self.session_key = decrypt(kdc.keys[self.name], r1)
        user.receive_keys(kdc, ba, br1)
        
    def receive(self, message):
        m = decrypt(self.session_key, message)
        print(m)
class Bob:
    def __init__(self):
        self.name= 'bob'
        
    def receive_keys(self, kdc, key, r1):
        key = decrypt(kdc.keys[self.name], key)
        self.session_key = decrypt(kdc.keys[self.name], r1)
    def send_message(self, to, msg):
        to_send = encrypt(self.session_key, msg)
        to.receive(to_send)

kdc = KDC()
alice = Alice()
bob = Bob()
alice.request_session_key(kdc, bob)
bob.send_message(alice, 'DEU BOM')
