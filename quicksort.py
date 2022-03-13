
def quicksort(array):
    #pick last element in array
    print('\n starting with', array)
    if len(array)>1:
        val = array[-1]
    else:
        return array
    temp = 0
    temp2 = 0
    iter = 0
    start = 0
        #move to end of array
        #swap last and second to last
        #make new last first last 
    while array.index(val)+1!= iter: #not in place, index of value and iteration !=
        while (array[iter])>array[array.index(val)]:
            temp_iter= -(len(array)-array.index(val)) #9
            print('temp iter', temp_iter)
            temp_piv = array[array.index(val)]
            
            array[array.index(val)] = array[iter]
            # print ('male l f ', array)
            array[iter]=array[temp_iter-1]
            # print ('make f 2tl ', array)
            array[temp_iter-1]=temp_piv
            # print ('make 2tl piv ', array)
            print ('now arr', array)
        iter+=1
        print ('after pass', array)
        print("now iter;", iter, 'array index is:',array.index(val) )
    
    return quicksort(array[:array.index(val)]) + quicksort(array[array.index(val):])

test = [21, 4, 1, 3, 9, 20, 25, 6, 22, 14]

print (quicksort(test))