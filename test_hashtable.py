import pytest

from hashtable import HashTable


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
    assert HashTable(size=3)._pairs == [None, None, None]


def test_should_insert_key_value_pairs():
    hash_table = HashTable(size=100)

    hash_table['hola'] = 'hello'
    hash_table[24.9] = 43
    hash_table[False] = True

    assert ('hola', 'hello') in hash_table.pairs
    assert (24.9, 43) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 100


def test_should_not_create_none_value_when_created():
    hash_table = HashTable(size=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values


def test_should_insert_none_value():
    hash_table = HashTable(size=100)
    hash_table['key'] = None
    assert ('key', None) in hash_table.pairs


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


# implementing the equivalent of del in dict
def test_should_delete_key_value_pair(hash_table):
    assert 'hola' in hash_table
    assert ('hola', 'hello') in hash_table.pairs
    assert len(hash_table) == 100

    del hash_table['hola']

    assert 'hola' not in hash_table
    assert ('hola', 'hello') not in hash_table.pairs
    assert len(hash_table) == 100


def test_should_raise_key_error_when_deleting_missing_key(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table['missing_key']
    assert exception_info.value.args[0] == 'missing_key'


# test that the value of an existing pair can be updated
def test_should_update_existing_value(hash_table):
    assert hash_table['hola'] == 'hello'

    hash_table['hola'] = 'new value'

    assert hash_table['hola'] == 'new value'
    assert hash_table[24.9] == 43
    assert hash_table[False] == True
    assert len(hash_table) == 100


def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs


def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs
