# encr

Makes serializing safer and easier by encrypting your data with a custom password.
You can get a history of all added functionalities between updates in the _CHANGELOG.md_ file.
You can get a list of features that should come in the future in the _COMING\_SOON.MD_ file.

## Dependencies

This package currently depends on _cryptography_, which at the time of writing depends on _cffi_, which again depends on _pycparser_.

Summing up, along with this package other 3 will be installed:

- cryptography
- cffi
- pycparser

## Usage

### The _encr_ class: safe data encryption and serialization with custom password

#### Creating an _encr_ instance

    from encr import encr
    e = encr("Password")

_encr_ takes two arguments:

- _password_, the string that will be hashed and converted into a key for encryption
- _clvl_ (optional), the compression level. Read [_zlib_'s documentation](https://docs.python.org/3/library/zlib.html#zlib.compress:~:text=level%20is%20an,to%20level%206\).) for information about that.

#### Changing the password mid-script: _setkey_

    e.setkey("New password")

_setkey_ changes the key used for serialization. It takes one argument:

- _password_, the string that will be hashed and converted into a key for encryption

##### Warning

Remember: changing the password of an _encr_ instance will make all previously encrypted data unusable, until you create another instance with the original password or reset the existing one with _setkey_.

#### Changing the compression level mid-script

    e.clvl = 5

_clvl_ is an attribute, which means it is a variable and it can't be called as a function. Just set _e.clvl_ like a normal variable.

#### Encrypting and decrypting: _dumps_ and _loads_

    serialized_object = e.dumps("foobar")
    print(serialized_object)
  > b'gAAAAABj85Nfc5tnmOSwj_wlSvFUop-E5ifYmEQUa8n2Ld5cNw5mahzkA-OpBDA9ky21OJa7vcLfheRMKA4yJppp7_ot_bWyTJ9lU5-TXCaeSJO8hzy3T7Y='
    deserialized_object = e.loads(serialized_object)
    print(deserialized_object)
  > foobar

_dumps_ serializes the object. It takes one argument:

- _obj_, the object to be encrypted

_loads_ deserializes the object. It takes one argument:

- _obj_, the encrypted object to be deserialized

#### Saving a variable to a file: _dump_ and _load_

    e.dump("foobar", "file.encr")
    print(e.load("file.encr"))
  > "foobar"

_dump_ serializes the object and saves it in a file. It takes two arguments:

- _obj_, the object to be encrypted
- _file_, the file where your object will be saved

_load_ takes a serialized object from a file and deserializes it. It takes one argument:

- _file_, the file where the object is stored

#### Encrypting a file: _dumpfile_ and _loadfile_

    e.dumpfile("MyFile.txt", "MyFile.encr")
    e.loadfile("MyFile.encr", "MyFile.txt")

_dumpfile_ reads a file and serializes it's content. It takes two arguments:

- _file_, the file to be encrypted
- _dest_, where your serialized file is saved

_loadfile_ reads a file and deserializes it's content. It takes two arguments:

- _file_, the file to be decrypted
- _dest_, where your deserialized file is stored

#### Encrypting a folder: _dumptree_ and _loadtree_

    e.dumptree("MyFolder", "MyFile.encr")
    e.loadtree("MyFile.encr")

_dumptree_ reads all the files contained in a folder and in all it's subfolders and serializes both their content, name and position. It takes two arguments:

- _file_, the folder to be encrypted
- _dest_, the file where your serialized folder is saved

_loadtree_ reads a file and restores the serialized tree. It takes one argument:

- _file_, the file containing the tree

#### Changing the password: _setkey_

    e = encr("Password")
    e.setkey("Password2")

You can change the key used for encryption anytime with the _setkey_ method.

#### Miscellaneous: _dumpfile_, _dumptree_ and _load_

    e.dumptree("MyFolder", "MyData.encr")
    print(e.load("MyData.encr")["MyFolder\\MyFile"].decode())
  
You can encrypt a file with _dumpfile_ or a tree with _dumptree_ and access it's content with _load_ without having to decrypt it.
_dumpfile_ saves directly the file's contents in binary mode, _dumptree_ saves all the filepaths and the file's contents in a dictionary.
