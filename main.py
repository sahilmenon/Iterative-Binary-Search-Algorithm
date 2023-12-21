# Function for the iterative binary search algorithm

#function takes in the array, the low, the high and the target value which is x
def iterativesearch (array, low, high, x):
    while low <= high:
        mid = low + (high - low) //2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
                low = mid + 1
        
        elif array[mid] > x:
            high = mid + 1

        else:
            high = mid - 1

    return -1
    
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x = 44
 
    # Function call
    result = iterativesearch(array, 0, len(array)-1, x)
    if result != -1:
        print("Element is present: index", result)
    else:
        print("Element is not present")