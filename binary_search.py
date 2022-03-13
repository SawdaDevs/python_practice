

def binary_search(input_array, value):
    index_to_go = int(len(input_array)/2) #can I do this recursively? Yes, but how
    
    end_array = len(input_array)
    start_array = 0
    print ('Ind start',  index_to_go)
    print ('\n')
    while (len(input_array[start_array:end_array])>1 and input_array[index_to_go]!=value):
        if input_array[index_to_go] < value: # go to this index
            start_array = index_to_go #new sub array starts at this array
            index_to_go = int((start_array+end_array)/2)
            print (' new ind to go ', index_to_go, 'st:',start_array, 'end:', end_array )
            print (input_array[start_array:end_array])
        elif input_array[index_to_go] > value:
            end_array = index_to_go #new sub array ends at this array
            index_to_go = int((start_array+end_array)/2)
            print (' new ind to go ', index_to_go, 'st:',start_array, 'end:', end_array )
            print (input_array[start_array:end_array])
        
        if input_array[index_to_go]==value: #value is the same
            return index_to_go
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))