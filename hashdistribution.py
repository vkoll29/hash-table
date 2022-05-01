from collections import Counter
from string import printable

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histrogram):
    for key in sorted(histrogram):
        count = histrogram[key]
        padding = (max(histrogram.pairs()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")

def hash_f2(text):
    """
    - multipy index with characters ordinal value to give position weight hence avoiding anagrams having the same hash values
    - start counting the indeces from 1 not 0
    - use repr to add apostrophes instead of str
    - remove left apostrophe if it exists using lstrip
    """
    return sum(
    index * ord(char) for index, char in enumerate(repr(text).lstrip("'"), start=1))


# plot(distribute(printable, 6, hash_f2))
print(hash_f2('a'), hash_f2('b'), hash_f2('c'))
