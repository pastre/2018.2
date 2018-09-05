#https://userpages.umbc.edu/~dgorin1/451/security/dcomm/keydist.htm


import random
def encrypt(key):
    return key*2

def decrypt(key):
    return key/2

class KDC:
    def __init__(self):
        self.keys = {'alice': 123, 'bob' = 456}
    
class KDCUser:
    def __init__(self, name):
        self.kdc = KDC()
        self.key = self.kdc.keys[]
  
class Alice(KDCUser):
    def __init__(self):
        super().__init__('alice')
    def setSessionKey(user):
        self.kdc.generateSession(self, user)
class Bob(KDCUser):
    def __init__(self):
        super().__init__('bob')
    
alice = Alice()
bob = Bob()
