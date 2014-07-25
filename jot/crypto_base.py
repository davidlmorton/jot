class CryptoBase(object):
    def __init__(self, alg, key):
        self.alg = alg
        self.key = key

    def decrypt(self, data):
        return NotImplemented

    def encrypt(self, data):
        return NotImplemented

    def sign(self, data):
        return NotImplemented

    def verify(self, data, signature):
        return NotImplemented
