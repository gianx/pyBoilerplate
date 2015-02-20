# pyBoilerplate

This is a simple template I use as a boilerplate for Python 2.7.x projects.  

It uses only standard library modules and it provides:

- CTRL+C management;
- Simple text encoding;
- Simple logging;
- Simple configuration management;
- Tool for creating directory structure;
- Improved error management;

### CTRL+C management
If CTRL+C in pressed, the script calls the function __ctrlc_handler__

### Simple text encoding
You can use the function __myencode(text)__ to try encoding a given text in the corrent format.  
Very useful when reading from files or managing external text.  


### Simple logging
The script creates a log named __[scriptname].log__ in which is possible to log message, infos, error, etc.  
It uses standar Python [logging](https://docs.python.org/2/library/logging.html) module (see linked documentation).  
In this repository you'll find a log example (__20150122-pyBoilerplate.log__)

### Simple configuration management
The script tries to read a configuration file named _[scriptname].conf_   
It uses standar Python [ConfigParser](https://docs.python.org/2/library/configparser.html) module (see linked documentation).  
Section are parsed but all the given configuration values are inserted in the same dictionary without any hierrarchy (basically sections are ignored).   
In this repository you'll find an example of a simple configuration file (__pyBoilerplate.conf__).

### Exception management
Snippet to handle and log exceptions
