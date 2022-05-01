# BLANK = object()
from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    def __init__(self, size):
        self._pairs = size * [None]


    def __len__(self):
        return len(self._pairs)


    def __setitem__(self, key, value):
        """
        - turn an arbitrary key into a numeric hash which acts as the index.
        - then use the modulo operator to limit the resulting index within the available address space
        """
        self._pairs[self._index(key)] = Pair(key, value)


    def __getitem__(self, key):
        """
        - find pair at index
        - if nothing is found, raise KeyError
        - else return the tuple's second element
        """
        pair = self._pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value


    def __contains__(self, key):
        """
        - find the value at key
        - if a key error is raised return false
        - else return true
        """
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True


    def __delitem__(self, key):
        """
        after refactoring the index method as shown in the commented code,
        it turns out that deleting an item is simply assigning BLANK to the _index
        so assign with the brackets syntax which will delegate it to __setitem__ method
        """
        # self.values[self._index(key)] = BLANK
        if key in self:
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(key)


    def get(self, key, default=None):
        """
        - get the value at key
        - if KeyError i.e missing key, return default which is an optional parameter
        """
        try:
            return self[key]
        except KeyError:
            return default


    @property
    def pairs(self):
        return [pair for pair in self._pairs if pair is not None]

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def keys(self):
        return set(pair.key for pair in self.pairs)


    def _index(self, key):
        return hash(key) % len(self)
