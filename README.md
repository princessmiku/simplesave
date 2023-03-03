# SimpleSave
Simple Storage is an easy way to work with data in your Python script. <br>
You can save and load your data without much effort or knowledge about any storage method. 
Moreover, it provides the possibilities to use data and variables globally in a script.<br>
The library does not reinvent the wheel, but enriches it with not having to deal with it.

# Installation

Installation from pip is not supported currently.

Installation with pip + github ``pip install git+https://github.com/princessmiku/simplesave``


# Infos


### Local and Global
It's possible to use it "local" or global (Planed) in your script

**Different**<br>
A local storage is allocated in a variable and the global storage is called directly from 
the library without a variable, so it can be used from anywhere.

### Storage Types

- Internal
- Json
- XML (Planed)
- SQLite (Planed)


# Setup

## Local Storage
All functions work the same on all types

## Internal
An internal memory stores the data in the class directly, when you restart the script, it loses all the data. 
If you want a way to save, this method is nothing for you.

This method is best suited for caches.

````python
from simplesave import Storage, INTERNAL
storage: Storage = Storage(INTERNAL)
````

### Value types
Accept any python possible type and class

## JSON
The JSON storage is built in the same way as the internal one, 
with the addition that you can store it in a JSON and load it from there.

With this storage method a file specification with ``file_path=xxx`` is possible, 
if no specification is set it falls back to the file ``simplesave.json``.

````python
from simplesave import Storage, JSON
storage: Storage = Storage(JSON, file_path="data.json")
````

### Value types
Accept all regular JSON Possible types

- String
- Integer
- Boolean
- Float
- List
- Dictionary

Lists content and dictionary are not checked if they correspond to the json format, 
this is the user's task to avoid it.

## XML
XML is the next planned feature

## SQLite
SQLite is planned


# Usage
All functions work the same on all types

### Variable types
- ``path`` is always a string
- ``index`` is always an integer 
- ``fill`` is always a list with string/integer objects
- ``value`` can be anything, but can also be limited by certain storage methods, 
 as not all types are supported by this one, for example JSON

## Path build
The library works with a key point principle, 
which means that entries are separated with a dot in the path -> ``user.5521.information.email``.

If there are unknown variables in the path then they are marked with a `?` -> ``user.?.inofrmation.email``

The filling of this goes through several ways

### String formatting
One way is to just do it directly in your own code

````python
user_id = "5521"
my_path = f"user.{user_id}.information.email"
````

### Integrated functions
The library has the possibility to take it over, otherwise the `?` would have no sense.

As an example we will use the `get_variable` function, but all functions where a path is specified can use the.

#### Use the fill parameter
With the fill you can pass a list with the values to be entered, 
strings and integers are allowed in there.

```python
storage.get_value("user.?.information.email", fill=[5521])
```
#### Use args
it is also possible to do it via args and write the parameters one after the other, but note if the function 
needs something else like the `value` or the `index` first.

Strings and integers are allowed in there.

````python
storage.get_value("user.?.information.email", 5521)
````
Example of multiple args

````python
storage.get_value("user.?.information.email.?", 5521, "main_address")
````

#### Note
At the end, it's possible to combine each other. 
But you have to take note that first the args and then the list is taken.

````python
storage.get_value("user.?.information.email.?", 5521, fill=["main_address"])
````
Of course, it is also possible to use several fill parameters, just to mention it
````python
storage.get_value("user.?.information.email.?", fill=[5521, "main_address"])
````
## GET

functions for getting data from the storage

### get_value
Get a value from the storage

#### Parameters
- path

#### Returns
- any

#### Example
````python
result = storage.get_value("config.port")
````

### get_value_by_index
Get a value from the storage, if this a list, get the item at the position

#### Parameters
- path
- index

#### Returns
- any

#### Example

````python
result = storage.get_value_by_index("config.ports", 1)
````

### get_value_type
Get the type of the value

#### Parameters
- path

#### Returns
- type of the value

#### Example

````python
val_type = storage.get_value_type("config.ports", 1)
````

### exists_path
Check if path exists

#### Parameters
- path

#### Returns
- true if path exists, else false

#### Example
````python
exists = storage.exists_path("config.ports")
````

## SET

### set_value
Set a value on the given path, its override the value if there's one

#### Parameters
- path
- value

#### Example
````python
storage.set_value("config.port", 2255)
````

### add_value
Add a value the list in a path, its generate automatically a list (without data loss), if there's no list

#### Parameters
- path
- value

#### Example
````python
storage.add_value("config.port", 2255)
````

## Delete

### delete
Delete all data in the path with the path itself (not the complete only the last)

#### Parameters
- path

#### Example
````python
storage.delete("config.port")
````

### remove_value_by_value
Remove from a list a value by the value

#### Parameters
- path
- value

#### Example
````python
storage.delete("config.ports", 2255)
````

### remove_value_by_index
Remove from a list a value with the index

#### Parameters
- path
- index

#### Example
````python
storage.delete("config.ports", 1)
````

### null
Set a path entry to null, its delete all sub data

#### Parameters
- path

#### Example
````python
storage.null("config.ports")
````

## More

### save

Save all the data of the current storage in your file

#### Example

````python
storage.save()
````

-----

Not completely used but
Translated with [DeepL translator](https://www.deepl.com/translator) (free version) 