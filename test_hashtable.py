import pytest

from hashtable import HashTable, BLANK

@pytest.fixture
def hash_table():
    sample_data = HashTable(size=100)
    sample_data['hola'] = 'hello'
    sample_data[24.9] = 43
    sample_data[False] = True
    return sample_data


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


def test_should_find_value_by_key(hash_table):
    assert hash_table['hola'] == 'hello'
    assert hash_table[24.9] == 43
    assert hash_table[False] == True


def test_should_raise_error_on_missing_key():
    hash_table = HashTable(size=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table['missing_key']
    assert exception_info.value.args[0] == 'missing_key'


# implementing the equivalent of dict's in method
def test_should_find_key(hash_table):
    assert 'hola' in hash_table


def test_should_not_find_key(hash_table):
    assert 'missing_key' not in hash_table

# implementing the equivalent of dict's get method
def test_should_get_value(hash_table):
    assert hash_table.get('hola') == 'hello'

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get('missing_key') is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get('missing_key', 'default') == 'default'

def test_should_get_value_with_default(hash_table):
    assert hash_table.get('hola', 'default') == 'hello'
