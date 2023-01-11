# MOTIVATION

- every piece of data stored on a computer is stored in bytes, 8 bits
- most of the time, you'll use a library to read in files, but...
- if you try to read an image file in using python's builtin open method, you'll get this error

_try to open image file with `open()`_

- you can see that by default it's trying to decode the byte data with a utf-8 decoder
- that will work for txt files and others where the byte data is a representation of utf-8 byte encoded data
- but it wont work for data that isnt in that format
- to get past this error you can add a `b` for binary to the mode which you're reading in the data

_add `b` to mode_

- and in that case python will read in the bytes of binary data
- the type of that data is bytes
- this shows each of the bytes represented in hexadecimal
