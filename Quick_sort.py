def quick_sort(sequence):
    """
        1. Check the length of sequence 
        2. if length > 1, pop last element from sequence and use that element
            as pivot. 
        3. finally concatinate the output eg. lower_sequence + pivot + higher squence
    """
    length = len(sequence)
    if(length <= 1):
        return sequence
    else:
        pivot = sequence.pop()
    
    elements_greater = [] #elements greater than pivot
    elements_lower = [] #elements less than pivot

    for element in sequence:
        if(element > pivot):
            elements_greater.append(element)
        else:
            elements_lower.append(element)
    
    
    return quick_sort(elements_lower) + [pivot] + quick_sort(elements_greater)
    

print(quick_sort([1.6,7,5,9,4,8,0]))
