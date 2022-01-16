from binary_search import binary_search_int
def test_binary_search_ints():
    assert binary_search_int([1,2,3,4,5,6,7,8,9,10], 7) == True
    assert binary_search_int([1,2,3], 2) == True 
    assert binary_search_int([1,2,3], 4) == False
    assert binary_search_int([1,2,3,4,5,6,7,8,9,10], 11) == False
    assert binary_search_int([1,2,3,4,5,6,7,8,9,10], -2) == False
    assert binary_search_int([], 5) == False
