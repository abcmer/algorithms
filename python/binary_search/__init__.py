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

def binary_search_recurrsive(sorted_list, value_to_find):
    return helper(sorted_list, value_to_find, 0, len(sorted_list)-1)

def helper(sorted_list, value_to_find, left, right):
    # Return false if left pointer becomes greater than right
    if left > right:
        return False
    # Init mid
    mid = (right - left) // 2 + left
    # Check if mid value equals value_to_find
    # Else recurrively call helper function again
    if sorted_list[mid] == value_to_find:
        return True
    elif value_to_find < sorted_list[mid]:
        return helper(sorted_list, value_to_find, left, mid - 1)
    else:
        return helper(sorted_list, value_to_find, mid + 1, right)



