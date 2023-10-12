# PYTHON ZONE

This is a place where I document confusing concepts that I have met during my journey in the
software industry with Python.

## 1. POSITIONAL ONLY ARGUMENT "/" AND KEYWORD ONLY ARGUMENT "*"

"/" indicates that parameters before the "/" can only be passed positionally
and cannot be passed using keyword arguments.

"*" signals us that arguments after it must be keyword arguments.

e.g.

```python
def example_func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

example_func(1, 2, 3, 4, e=5, f=6)
```

## 2. IO

A concrete object belongs to *text I/O*, *binary I/O*, and *raw I/O* is called **file object**. Other common terms are **stream** or **file-like object**.

```python
# text IO expects and produces str objects
# the easiest way to create a text stream (text file object) is with open()
f = open("my_file.txt", "r", encoding="utf-8")
# NOTE: encoding="utf-8" here means the text data in the file is assumed to be encoded
# in UTF-8

# In memory text streams are also available as StringIO objects
f = io.StringIO("Some text data")
```

An image file, audio file or any non-textual data on the disk is considered a binary stream.
A binary stream is a sequence of bytes that represent binary data.

```python
# bytes IO expects bytes-like objects and produces bytes objects
# Create a binary stream with open()
f = open("my_image.jpg", "rb") # no encoding, decoding, or new line translation is performed

# In memory binary streams
f = io.BytesIO(b"Some binary data: \x00\x01")
```

## 3. Base64

Base64 is a binary-to-text encoding scheme that is used to represent binary data in an ASCII (text-based) format. It converts binary data into a set of printable ASCII characters, making it suitable for transferring and storing binary data in environments that expect only text-based data. There are several advantages when using the base64 encoding method:

1. Encoding Binary Data as Text: Base64 allows us to encode binary data (e.g., images, audio, video, or any binary file) into a string of ASCII characters. This is useful when you need to transmit binary data over protocols or systems that only support text-based data, such as email or HTTP headers.

2. URL and Filename Safety: Base64-encoded strings only contain ASCII characters that are safe to use in URLs and filenames. This is beneficial when you need to include binary data in a URL or use it as a part of a filename.

3. Data Integrity: Base64 encoding does not alter the data's content; it merely represents it in a different form. As a result, it preserves the integrity of the data during transmission or storage.

4. Cross-platform Compatibility: Base64 encoding is widely supported across different programming languages and platforms. This makes it a reliable and platform-independent method for encoding and decoding binary data.

Common use cases for Base64 encoding include:

- Embedding images or multimedia content in HTML or CSS files.
- Encoding binary attachments in emails.
- Storing binary data in JSON or XML data structures.
- Encoding binary data for transfer over HTTP headers or URL parameters.


## `yield` statement

- Similar to the `return` keyword: one returns values and the other returns a
  generator object to the one who calls the function.

- One major dissimilarity is return terminates the executions of the function,
  while yield pauses the execution of the function.

_Advantages:_

- Memory efficency is high since the execution happens only when the caller
  iterates over the object.

- Pausing and resuming from the same point can be done easily as the variable
  states are kept track.

_Disadvantages:_

- The flow of code might be difficult to understand,

- Might cause erros in the program if the calling of generator functions is not
  handled properly.
