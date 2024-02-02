from linear_search import linear_search,linear_search_global
import pytest

def test_linear_search_exists():
    assert linear_search(3, [1,2,3]) == 2

def test_linear_search_does_not_exist():
    assert linear_search(4, [1,2,3]) == None

def test_linear_search_each_int_exists_but_not_whole():
    assert linear_search(13, [1,2,3]) == None


# tests for linear_search_global
def test_global_search_multiple_chars():
    assert linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]

def test_global_search_single_char():
    assert linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6]

def test_global_search_duplicate_char():
    assert linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4]
