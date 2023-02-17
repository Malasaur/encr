Makes serializing safer and easier by encrypting your data with a custom password (hashed and turned into a key)

## Usage

#### Create an _encr_ instance

    from encr import encr
    e = encr("Password")

_encr_ takes three arguments:
- _password_, the string that will be hashed and converted into a key for encryption
- _lib_, the library/object used for serialization (read the "Custom _library_" section for more info)
- _clvl_, the compression level

#### _dumps_ and _loads_

    serialized_object = e.dumps("foobar")
    deserialized_object = e.loads(serialized_object)
    print(deserialized_object)
  > "foobar"

_dumps_ serializes the object. It takes one argument:
- _obj_, the object to be encrypted

_loads_ deserializes the object. It takes one argument:
- _obj_, the encrypted object to be deserialized

#### _dump_ and _load_

    e.dump("foobar", "file.encr")
    print(e.load("file.encr"))
  > "foobar"

_dump_ serializes the object and saves it in a file. It takes two arguments:
- _obj_, the object to be encrypted
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

_loadfile_ reads a file and deserializes it's content. It takes two arguments:
- _file_, the file to be decrypted
- _dest_, where your deserialized file is stored

#### _dumptree_ and _loadtree_

    e.dumpfile("MyFolder", "MyFile.encr")
    e.loadfile("MyFile.encr")

_dumpfile_ reads all the files contained in a folder and in all it's subfolders and serializes both their content, name and position. It takes two arguments:
- _file_, the folder to be encrypted
- _dest_, the file where your serialized folder is saved

_loadfile_ reads a file and restores the serialized tree. It takes one argument:
- _file_, the file containing the tree

#### Custom _library_

When you create an _encr_ instance, pass a custom serialization object/library as a keyword argument:

    from encr import encr
    import json
    e = encr("Password", lib=json)

_myobj_ must be an object/library (like _json_ or _marshal_) with two methods: _dumps_ and _loads_. _pickle_ is set by default

##### Attention:

Some libraries, like _json_, can't encrypt objects of type _bytes_, which is required by the _dumpfile_, _loadfile_, _dumptree_ and _loadtree_ methods
