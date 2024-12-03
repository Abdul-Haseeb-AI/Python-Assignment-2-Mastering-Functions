def flatten_list(n_list): # function which flatten a nested list
    flat_list = []
    for elements in n_list:
        if isinstance(elements,list):  # cheak weather the element is list or not
            flat_list.extend(flatten_list(elements))    #send element(list) to function and extend the flat_list in this way the element in list form is not appended
        else:
            flat_list.append(elements)     # add element to flat_list
    return flat_list
nested_list = [0,[1,2],5,2,[2,3,5]]  
print(nested_list)
print(flatten_list(nested_list))
