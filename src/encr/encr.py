from hashlib import sha512
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from zlib import compress, decompress
from pickle import dumps, loads
from os import makedirs, walk
from os.path import dirname, join, isfile

def salt(password):
    n = 0
    for char in password:
        n += ord(char)
    return sha512(password.encode()).digest()

class encr:
    def __init__(self, password, clvl=-1):
        """
        :param password: Password used to encrypt and decrypt the objects
        :type password: (str)
        :param clvl: Object compression level passed to zlib.compress
        :type clvl: (int)
        """
        self.setkey(password)
        self.clvl = clvl

    def setkey(self, password):
        self.encryptor = Fernet(urlsafe_b64encode(PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt(password), iterations=100000).derive(password.encode())))

    #Serialize a variable and return it's value
    def dumps(self, obj):
        """
        :param obj: Object to serialize
        :type obj: Any
        """
        return self.encryptor.encrypt(compress(dumps(obj), level=self.clvl))

    #Deserialize a variable and return it's value
    def loads(self, obj):
        """
        :param obj: Object to deserialize
        :type obj: (bytes)
        """
        return loads(decompress(self.encryptor.decrypt(obj)))

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
        if not isfile(file):
            raise FileNotFoundError(f"File '{file}' was not found.")
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

    def dumpitem(self, name, dest):
        """
        :param name: Name of thw file or folder to encrypt
        :type name: (str)
        """
        if isfile(name):
            self.dumpfile(name, dest)
        else:
            self.dumptree(name, dest)

    def loaditem(self, file):
        """
        :param file: File containing item to decrypt
        :type file: (str)
        """

"""
encr password --clvl 9
"""

if __name__ == "__main__":
    from sys import argv
    
    args = argv[1:]

    help_msg = """
encr - Safe data serialization+encryption command line utìlity.

Usage:
    encr [password] [--clvl lvl] [? | -h | --help]

Arguments:
    password - The password used for encryption/decryption. If empty, this help message is displayed. If the password contains spaces, please enclose it in quotation marks (e.g. ' encr "My spaced password" ').
    lvl - The compression level. Number from -1 to 9. Defaults to -1.
    ? | -h | --help - Display this help message

Command line tool:
    TODO: Continue help message and command line utility

"""

    if args == []:
        print(help_msg)