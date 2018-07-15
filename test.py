import pytest
from app import (execute_queries, get_address_queries_from_file,
                 transform_address_details)


def test_transform_address_details():
    details = ['Sam', '9660']
    actual = transform_address_details(details)

    assert actual[0] == 'sam'
    assert type(actual[1]) is int
    assert type(actual) is tuple


def test_transform_address_details_with_invalid_list():
    details = 'jj'
    with pytest.raises(TypeError):
        transform_address_details(details)


def test_get_address_queries_from_filewith_invalid_file():
    with pytest.raises(IOError) as error:
        get_address_queries_from_file('./samples.txt')



def test_get_address_queries_from_file():
    actual = get_address_queries_from_file('./sample.txt')
    assert type(actual) is tuple
    assert len(actual) == 2
    assert len(actual[0]) == 103
    assert len(actual[1]) == 5


def test_execute_queries():
    addreesses = [('sam', 111), ('paul', 222)]
    queries =['sam', 'collins', 'paul']
    actual = execute_queries(addreesses, queries)
    assert actual is not None
    assert next(actual) == 'sam=111'
    assert next(actual) == 'Not Found'
    assert next(actual) == 'paul=222'


def test_execute_queries_with_multiple_similar_names():
    addreesses = [('sam', 111), ('paul', 222), ('sam', 444)]
    queries =['sam', 'collins', 'paul']
    actual = execute_queries(addreesses, queries)
    assert actual is not None
    assert next(actual) == 'sam=111'
    assert next(actual) == 'sam=444'
    assert next(actual) == 'Not Found'
    assert next(actual) == 'paul=222'
