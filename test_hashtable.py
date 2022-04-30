from hashtable import HashTable, BLANK

def test_should_create_hashtable():
    assert HashTable(size=100) is not None

def test_should_return_size():
    assert len(HashTable(size=100)) == 100

def test_should_create_empty_value_slots():
    assert HashTable(size=3).values == [BLANK, BLANK, BLANK]

def test_should_insert_key_value_pairs():
    hash_table = HashTable(size=100)

    hash_table['hola'] = 'hello'
    hash_table[24.9] = 43
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 43 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 100

def test_should_not_create_none_value_when_created():
    assert None not in HashTable(size=100).values

def test_should_insert_none_value():
    hash_table = HashTable(size=100)
    hash_table['key'] = None
    assert None in hash_table.values
