from urllib.request import HTTPDigestAuthHandler


def binary_search_int(sorted_list, value_to_find):   
    # Edge cases 
    if not sorted_list:
        return False
    # Set low, high
    low, high = 0, len(sorted_list) -1
    # Iteratively search
    while low <= high:   
        mid = (high - low) // 2 + low
        if sorted_list[mid] == value_to_find:
            return True
        elif value_to_find < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False




