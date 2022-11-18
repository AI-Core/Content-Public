# MOTIVATION

- every piece of data stored on a computer is stored in bytes, 8 bits
- but many different use cases require data to be in a text format, like sending email or displaying HTML
- so whatever data type it is, images, video, python dictionary, it needs to be encoded into a string of text

<!-- - you could do a binary encoding, where you
- instead, you can use base 64 encoding -->

- base 64 encoding is a common way to do that
- the most common use case of base 64 encoding is to represent images as strings so that they can be stored in text assets like HTML

# WHAT IS BASE 64 ENCODING?

- base 64 encoding is where data is represented using text
- it's a binary to text encoding scheme, which means that it is used to turn binary data into text
- it's like binary data, but now you have base 64 numbers instead of base 2

- these are the 64 different characters
- all upper case alphabet
- all lower case alphabet
- integers
- plus and slash

- it's these ones because they can be found in almost all character sets
- and it's 64 because that's a nic power of 2

- that means that we can count up to 64 with a single character
- whereas in binary data, you can count up to 2 with a single character because you only have the characters 0 and 1 to work with

- that means that the

- in base 64, 4 characters can store 3 bytes of data
- that's because a byte is 8 bits, 3 of them gives you 24 bits, and 2 to the power of 24 is 16777216
- which is the same as 64 to the power of 4
- and that's the number of different states that you can represent with either of them

# USE CASES

_Show image data stored in base64 format_

# OUTRO

- this final output is very normal characters
- it doesn't contain backslashes or @ symbols which might have a particualr meaning in some files and break their parsers
