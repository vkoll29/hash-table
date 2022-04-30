BLANK = object()


class HashTable:
    def __init__(self, size):
        self.values = size * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        """
        - turn an arbitrary key into a numeric hash which acts as the index.
        - then use the modulo operator to limit the resulting index within the available address space
        """
        index = hash(key) % len(self)
        self.values[index] = value


    def __getitem__(self, key):
        """
        - get the hash value of the key which is its index
        - access the value at that index
        - check that the value is not BLANK object i.e has not been set. this means it does not have a key
        - use is operator instead of == to compare identities not values
        return value
        """
        index = hash(key) % len(self)
        value = self.values[index]
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
