from hashlib import sha512
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from zlib import compress, decompress
import pickle
from os import makedirs, walk
from os.path import dirname, join

class encr:
    def __init__(self, password, lib=pickle, clvl=-1):
        """
        :param password: Password used to encrypt and decrypt the objects
        :type password: (str)
        :param lib: Library or object that will be used for serialization
        :type lib: Any
        :param clvl: Object compression level passed to zlib.compress
        :type clvl: (int)
        """
        self.key = urlsafe_b64encode(sha512(password.encode()).hexdigest()[:32].encode())
        self.lib = lib
        self.clvl = clvl
    
    #Serialize a variable and return it's value
    def dumps(self, obj):
        """
        :param obj: Object to serialize
        :type obj: Any
        """
        return Fernet(self.key).encrypt(compress(self.lib.dumps(obj), level=self.clvl))

    #Deserialize a variable and return it's value
    def loads(self, obj):
        """
        :param obj: Object to deserialize
        :type obj: (bytes)
        """
        return self.lib.loads(decompress(Fernet(self.key).decrypt(obj)))
    
    #Serialize a variable and save it in a file
    def dump(self, obj, file):
        """
        :param obj: Object to serialize
        :type obj: Any
        :param file: File where the serialized object is saved
        :type file: (str)
        """
        open(file, 'wb').write(self.dumps(obj))
    
    #Deserialize a variable saved in a file and return it's value
    def load(self, file):
        """
        :param file: File where the serialized object is saved
        :type file: (str)
        """
        return self.loads(open(file, 'rb').read())
    
    #Encrypt a file
    def dumpfile(self, file, dest):
        """
        :param file: File to encrypt
        :type file: (str)
        :param dest: Destination of encrypted file
        :type dest: (str)
        """
        self.dump(open(file, 'rb').read(), dest)
    
    #Decrypt a file
    def loadfile(self, file, dest):
        """
        :param file: File to decrypt
        :type file: (str)
        :param dest: Destination of decrypted file
        :type dest: (str)
        """
        open(dest, 'wb').write(self.load(file))
    
    #Encrypt a folder and turn it into a file
    def dumptree(self, folder, dest):
        """
        :param folder: Folder to encrypt
        :type folder: (str)
        :param dest: Destination of encrypted folder
        :type dest: (str)
        """
        data = dict()
        for dir in walk(folder):
            for file in dir[2]:
                filepath = join(dir[0], file)
                data[filepath] = open(filepath, 'rb').read()
        self.dump(data, dest)
    
    #Decrypt a folder which was serialized with 'encr.dumptree'
    def loadtree(self, file):
        """
        :param folder: File containing folder to decrypt
        :type folder: (str)
        """
        data = self.load(file)
        for file in data.keys():
            makedirs(dirname(file), exist_ok=True)
            open(file, 'wb').write(data[file])
