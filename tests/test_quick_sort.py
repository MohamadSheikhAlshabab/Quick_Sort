from quick_sort import __version__
from quick_sort.quick_sort import swap,partition,quick_sort,print_list

def test_version():
    assert __version__ == '0.1.0'

def test_quick_sort_1():
    arr = [8, 4, 23, 42, 16, 15]
    n = len(arr) 
    expected = [4, 8, 15, 16, 23, 42]
    quick_sort(arr,0,n-1)
    actual = print_list(arr)
    assert actual == expected

def test_quick_sort_2():
    arr = [20, 18, 12, 8, 5, -2]
    n = len(arr) 
    expected = [-2, 5, 8, 12, 18, 20]
    quick_sort(arr,0,n-1)
    actual = print_list(arr)
    assert actual == expected

def test_quick_sort_3():
    arr = [5, 12, 7, 5, 5, 7]
    n = len(arr) 
    expected = [5, 5, 5, 7, 7, 12]
    quick_sort(arr,0,n-1)
    actual = print_list(arr)
    assert actual == expected

def test_quick_sort_4():
    arr = [2, 3, 5, 7, 13, 11]
    n = len(arr) 
    expected = [2, 3, 5, 7, 11, 13]
    quick_sort(arr,0,n-1)
    actual = print_list(arr)
    assert actual == expected

def test_quick_sort_empty():
    arr = []
    n = len(arr) 
    expected = []
    quick_sort(arr,0,n-1)
    actual = print_list(arr)
    assert actual == expected

def test_quick_sort_str():
    arr = ["1","-1","3"]
    n = len(arr) 
    expected = ["-1","1","3"]
    quick_sort(arr,0,n-1)
    actual = print_list(arr)
    assert actual == expected