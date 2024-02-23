def top_n(items, n):
    """Return the top n items in an array, in desc order

    Args:
        item (array): list or array - like object 
        n (int): number of items to return
        
    Return:
        array: top n items, in desc order
        
    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
    """
    for i in range(n): # keep sorting until we have top n items
        for j in range(len(items) - 1 -i): 
            if items[j] > items[j + 1]:  # if the first is bigger the second item
                items[j], items[j + 1] = items[j + 1], items[j]  # swap the items
    
    #get last two items
    top_n = items[-n:]
    
    #retun in desc order
    return top_n[::-1]