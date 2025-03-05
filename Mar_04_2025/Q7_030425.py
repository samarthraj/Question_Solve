#find the longest consecutive sequence of elements in unsorted array 

def longest_sequence(arr):

    arr.sort() 
    start = 0
    end = 0 

    for i in range(0, len(arr)-1): 
        if arr[i+1] - arr[i] == 1: 
            end += 1
            
    return end - start + 1

arr = [100,4,200,1,3,2]
#answer = 4 since [1,2,3,4] 
ans = longest_sequence(arr)
print(ans) 
