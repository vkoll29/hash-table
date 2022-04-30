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
