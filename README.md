Makes serializing safer and easier by encrypting your data with a custom password (hashed and turned into a key)

## Usage

#### Create an _encr_ instance

    from encr import encr
    e = encr("Password")

_encr_ takes three arguments:
- _password_, the string that will be hashed and converted into a key for encryption
- _lib_, the library/object used for serialization (read the "custom library" section for more info)
- _clvl_, the compression level

#### _dumps_ and _loads_

    serialized_object = e.dumps("foobar")
    deserialized_object = e.loads(serialized_object)
    print(deserialized_object)
  > "foobar"

_dump_ serializes the object. It takes one argument:
- _obj_, the object to be encrypted (Note: it must be JSON-serializable)

_load_ deserializes the object. It takes one argument:
- _obj_, the encrypted object to be deserialized

#### _dump_ and _load_

    e.dump("foobar", "file.encr")
    print(e.load("file.encr"))
  > "foobar"

_dump_ serializes the object and saves it in a file. It takes two arguments:
- _obj_, the object to be encrypted (Note: it must be JSON-serializable)
- _file_, the file where your object will be saved

_load_ takes a serialized object from a file and deserializes it. It takes one argument:
- _file_, the file where the object is stored

#### _dumpfile_ and _loadfile_

##### MyFile.txt

    foobar

##### program.py

    e.dumpfile("MyFile.txt", "MyFile.encr")
    e.loadfile("MyFile.encr", "MyFile.txt")

_dumpfile_ reads a file and serializes it's content. It takes two arguments:
- _file_, the file to be encrypted
- _dest_, where your serialized file is saved

_loadfile_ reads a file and serializes it's content. It takes two arguments:
- _file_, the file to be decrypted
- _dest_, where your deserialized file is stored

#### Custom _library_

JSON can't serialize classes or functions. If you want to do that, you can choose your custom library or class to serialize the objects.

When you create an _encr_ instance, pass the object/library as a keyword argument:

    from encr import encr
    e = encr("Password", lib=myobj)

_myobj_ must be an object/library (like _pickle_ or _marshal_) with two methods: _dumps_ and _loads_
