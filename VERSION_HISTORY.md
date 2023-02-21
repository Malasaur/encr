## General functionality history

### Version 0.0.1

The first ever _encr_ version.
The _encr_ class had the following methods:

- dumps
- loads
- dump
- load
- dumpfile
- loadfile

### Version 0.0.2

The first _encr_ update.
The _encr_ class didn't get any new methods.
Support for custom serialization library was added.
Read about version 0.0.2 in the _Detailed history_ section for more information.

### Version 0.0.3

This version had a bug that made it unusable. It got fixed in _0.0.4_
The _encr_ class got 2 new methods:

- dumptree
- loadtree

### Version 0.0.4

This version fixed a bug from _0.0.3_. Nothing else was added.

### Current version (0.0.5)

The latest _encr_ update.
The _encr_ class didn't get any new methods.
Support for custom serialization library was removed as it was useless.
Read about version 0.0.5 in the _Detailed history_ section for more information.

## Detailed history

### Version 0.0.1

The _encr_ class had the following methods:

- dumps (obj)
- loads (obj)
- dump (obj, file)
- load (file)
- dumpfile (file, dest)
- loadfile (file, dest)

The _encr_ class used _json_ for serialization and _cryptography.Fernet_ for encryption.

### Version 0.0.2

A new argument for the _encr_ class was added: _lib_, allowing users to choose a custom library for serialization.
No methods were added to it.

### Version 0.0.3

Due to a bad import, the package was unusable.
The bug was soon solved with version _0.0.4_.

2 methods were added to the _encr_ class:

- dumptree (folder, dest)
- loadtree (file)

The default library for serialization was changed from _json_ to _pickle_

### Version 0.0.4

This version was just a fix to the bug found in _0.0.3_

### Current version (0.0.5)

This version removed the _lib_ argument from the _encr_ class as it was considered useless.
The class now uses _pickle_ for serialization, and now it is not changable/customizable anymore.