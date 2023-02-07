from distutils.core import setup

setup(
    name = "encr",
    packages = ["encr"],
    version = "0.0.1",
    license = "gpl-3.0",
    description = "A small package for safe data serialization and encryption",
    author = "Silvio Amuntenci",
    author_email = "amuntenci.silvio@gmail.com",
    url = "https://github.com/Malasaur/encr",
    download_url = "https://github.com/Malasaur/encr/archive/refs/tags/v0.0.1.tar.gz",
    keywords = ["serialization", "encryption"],
    install_requires = ["cryptography"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ]
)