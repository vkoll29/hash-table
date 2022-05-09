import pytest
from pytest_unordered import unordered

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


def test_should_report_length_of_empty_hashtable(hash_table):
    assert len(HashTable(size=100)) == 0


def test_should_report_length_of_nonempty_hashtable(hash_table):
    assert len(hash_table) == 3


def test_should_create_empty_pair_slots():
    assert HashTable(size=3)._slots == [None, None, None]


def test_should_insert_key_value_pairs():
    hash_table = HashTable(size=100)

    hash_table['hola'] = 'hello'
    hash_table[24.9] = 43
    hash_table[False] = True

    assert ('hola', 'hello') in hash_table.pairs
    assert (24.9, 43) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 3


def test_should_not_create_none_value_when_created():
    # values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in HashTable(size=100).values


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
    assert len(hash_table) == 3

    del hash_table['hola']

    assert 'hola' not in hash_table
    assert ('hola', 'hello') not in hash_table.pairs
    assert len(hash_table) == 2


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
    assert len(hash_table) == 3


def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs


def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs


def test_should_return_duplicate_values():
    hash_table = HashTable(size=100)
    hash_table['key1'] = 21
    hash_table['key2'] = 43
    hash_table['key3'] = 43

    assert [21, 43, 43] == sorted(hash_table.values)


def test_should_get_values(hash_table):
    assert unordered(hash_table.values) == ['hello', 43, True]


def test_should_get_values_of_empty_list():
    assert HashTable(size=100).values == []


def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values


def test_should_get_keys(hash_table):
    assert hash_table.keys == {'hola', 24.9, False}


def test_should_get_keys_of_empty_hash_table():
    assert HashTable(size=100).keys == set()


def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys


def test_should_return_pairs(hash_table):
    assert hash_table.pairs == {
        ('hola', 'hello'),
        (24.9, 43),
        (False, True)
    }


def test_should_return_pairs_for_empty_hash_table():
    assert HashTable(size=100).pairs == set()


def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.pairs)

    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)


def test_should_not_create_a_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(size=0)


def test_should_not_create_a_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(size=-100)


def test_should_report_size_of_empty_hashtable():
    assert HashTable(size=100).size == 100


def test_should_report_size(hash_table):
    assert hash_table.size == 100



