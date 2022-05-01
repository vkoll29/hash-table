BLANK = object()


class HashTable:

    def _index(self, key):
        return hash(key) % len(self)


    def __init__(self, size):
        self.values = size * [BLANK]


    def __len__(self):
        return len(self.values)


    def __setitem__(self, key, value):
        """
        - turn an arbitrary key into a numeric hash which acts as the index.
        - then use the modulo operator to limit the resulting index within the available address space
        """
        self.values[self._index(key)] = value


    def __getitem__(self, key):
        """
        - get the hash value of the key which is its index
        - access the value at that index
        - check that the value is not BLANK object i.e has not been set. this means it does not have a key
        - use is operator instead of == to compare identities not values
        return value
        """
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value


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


    def get(self, key, default=None):
        """
        - get the value at key
        - if KeyError i.e missing key, return default which is an optional parameter
        """
        try:
            return self[key]
        except KeyError:
            return default


    def __delitem__(self, key):
        """
        after refactoring the index method as shown in the commented code,
        it turns out that deleting an item is simply assigning BLANK to the _index
        so assign with the brackets syntax which will delegate it to __setitem__ method
        """
        # self.values[self._index(key)] = BLANK
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)
