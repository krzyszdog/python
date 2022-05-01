text = """
Data Types
Dictionary

Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
While the values can be of any data type and can repeat, keys must be of immutable type (string,
number or tuple with immutable elements) and must be unique.
Accessing Elements from Dictionary

While indexing is used with other data types to access values, a dictionary uses keys.
Keys can be used either inside square brackets [] or with the get() method.

If we use the square brackets [], KeyError is raised in case a key is not found in the dictionary.
On the other hand, the get() method returns None if the key is not found.

Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.

If the key is already present, then the existing value gets updated.
In case the key is not present, a new (key: value) pair is added to the dictionary.

Method                  Description
----------------------------------------------------------------------------------------------------------------------
clear()                 Removes all items from the dictionary.
copy()                  Returns a shallow copy of the dictionary.
fromkeys(seq[, v])      Returns a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])            Returns the value of the key. If the key does not exist, returns d (defaults to None).
items()                 Return a new object of the dictionary's items in (key, value) format.
keys()                  Returns a new object of the dictionary's keys.
pop(key[,d])            Removes the item with the key and returns its value or d if key is not found.
                        If d is not provided and the key is not found, it raises KeyError.
popitem()               Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d])     Returns the corresponding value if the key is in the dictionary.
                        If not, inserts the key with a value of d and returns d (defaults to None).
update([other])         Updates the dictionary with the key/value pairs from other, overwriting existing keys.
values()                Returns a new object of the dictionary's values

Built-in functions
-------------------------------------------------------------------------------------------------------------------
all()           Return True if all keys of the dictionary are True (or if the dictionary is empty).
any()           Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()           Return the length (the number of items) in the dictionary.
cmp()           Compares items of two dictionaries. (Not available in Python 3)
sorted()        Return a new sorted list of keys in the dictionary.

"""

counter = 0
for letter in text:
    if letter == "a":
        # counter = counter + 1
        counter += 1

print(f"Loop for found {counter} letters 'a' ")
print("Loop for found {} letters 'a' ".format(counter))