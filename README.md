# PyUtils
[![codebeat badge](https://codebeat.co/badges/79769141-a8fd-40a0-8763-40c5d82c71d6)](https://codebeat.co/projects/github-com-damonthecricket-py-utils-master) [![Build Status](https://travis-ci.org/damonthecricket/pyutils.svg?branch=master)](https://travis-ci.org/damonthecricket/pyutils)

Python programming language utils library.


1. [Features](#features)
2. [Installation](#installation)



### Features
1. Array. Tiny module to work with Python array.
   ```python
   import pyutils.array as array
   
   full_array = [1, 2, 3, 4, 5]
   empty_array = []
   
   # Returns 5
   last = array.last(full_array)
   
   # Returns False
   is_empty = array.is_empty(full_array)
   
   # Returns True
   is_elements = array.is_elements(full_array)
   
   # Returns None
   last = array.last(empty_array)
   
   # Returns True
   is_empty = array.is_empty(empty_array)
   
   # Returns False
   is_elements = array.is_elements(empty_array)
   ```
2. CSVUtil. Tiny module to work with csv file.
   ```python
   import pyutils.csvutils as csv
   
   // Load csv
   
   path = "1.txt"
   
   // Load 1.txt csv array.
   c = csv.load(path)
   
   // Load 1.txt csv file as dictionary array.
   c = csv.load_dictionary(path)
   ```

3. File. Tiny module to work with file.

   ```python
   import pyutils.file as file
  
   path = "data/text/file.txt"
  
   // Returns file.txt
   name = file.name_from_path(path)
  
   // Returns txt
   extension = file.name_from_path(path)
   ```

4. Folder. Tiny module to work with dictionary.
   ```python
   folder /
         1.txt
         2.txt
         a /
  
   import pyutils.folder as folder
  
   // Returns ["1.txt", "2.txt", "a"]
   content = folder.content("folder/")
   ```
 
 

 ### Installation
  ```
  $ git clone https://github.com/damonthecricket/pyutils.git
  ```
  

