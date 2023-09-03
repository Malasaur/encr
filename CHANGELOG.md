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

### Version 0.0.5

The _encr_ class didn't get any new methods.
Support for custom serialization library was removed as it was useless.
Read about version 0.0.5 in the _Detailed history_ section for more information.

### Version 0.1.0

Due to a major internal change, all data saved with previous versions of _encr_ is now useless.
Read about version 0.1.0 in the _Detailed history_ section for more information.

### Current version (0.1.0.1)

The latest _encr_ update.
The _encr_ repository was restructured and renewed, but no update was added to the program.

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

### Version 0.0.5

A new "VERSION_HISTORY.md" file was added.
This version removed the _lib_ argument from the _encr_ class as it was considered useless.
The class started using _pickle_ for serialization, and became unchangable/uncustomizable.

1 method was added to the _encr_ class:

- setkey (password)

As noticed after it's publication, the class' encryption key wasn't saved properly due to a bug, which made the package unusable.
The only way to bypass this bug was calling _e.setkey_ after the object's creation and resetting the key.
This bug was fixed in version _0.1.0_

### Version 0.1.0

This version fixed the bug found in _0.0.5_

The "VERSION_HISTORY.md" file is now called "CHANGELOG.md".
A new "COMING_SOON.md" file was added.
The _encr_ class now uses the built-in method to turn the password into a Fernet key.
The _encr_ class now stores the Fernet object directly instead of storing the key and recreating the instance every time.

Due to the above changes, all objects encrypted with previous versions of _encr_ can't be decrypted with future versions anymore.

The _encr_ class is now in its "Partially stable" version, which means that it shouldn't get major non-retro-compatible updates in the future like this

### Current version (0.1.0.1)

This version is a simple switch from a "setup.py+python -m build" to a "pyproject.toml+GitHub actions" publishing method, which is easier and will allow me to publish more updates in no time
