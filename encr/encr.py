from hashlib import sha512
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from zlib import compress, decompress
from json import dumps, loads

class encr:
    def __init__(self, password:str, clvl:int=-1):
        """
        :param password: Password used to encrypt and decrypt the objects.
        :type password: (str)
        :param clvl: Object compression level passed to zlib.compress
        :type clvl: (int)
        """
        self.key = urlsafe_b64encode(sha512(password.encode()).hexdigest()[:32].encode())
        self.clvl = clvl
    
    #Serialize a variable and return it's value
    def dumps(self, obj:dict|list|tuple|str|float|bool|None) -> bytes:
        """
        :param obj: Object to serialize
        :type obj: Any JSON serializable object; (dict) or (list) or (tuple) or (str) or (float) or (bool) or (None)...
        """
        return Fernet(self.key).encrypt(compress(dumps(obj).encode(), level=self.clvl))

    #Deserialize a variable and return it's value
    def loads(self, obj:bytes):
        """
        :param obj: Object to deserialize
        :type obj: (bytes)
        """
        return loads(decompress(Fernet(self.key).decrypt(obj)))
    
    #Serialize a variable and save it in a file
    def dump(self, obj:dict|list|tuple|str|float|bool|None, file:str):
        """
        :param obj: Object to serialize
        :type obj: Any JSON serializable object; (dict) or (list) or (tuple) or (str) or (float) or (bool) or (None)...
        :param file: File where the serialized object is saved
        :type file: (str)
        """
        open(file, 'wb').write(self.dumps(obj))
    
    #Deserialize a variable saved in a file and return it's value
    def load(self, file:str):
        """
        :param file: File where the serialized object is saved
        :type file: (str)
        """
        return self.loads(open(file, 'rb').read())
    
    #Encrypt a file
    def dumpfile(self, file:str, dest:str):
        """
        :param file: File to encrypt
        :type file: (str)
        :param dest: Destination of encrypted file
        :type dest: (str)
        """
        self.dump(open(file).read(), dest)
    
    #Decrypt a file
    def loadfile(self, file, dest):
        """
        :param file: File to decrypt
        :type file: (str)
        :param dest: Destination of decrypted file
        :type dest: (str)
        """
        open(dest, "w").write(self.load(file))
