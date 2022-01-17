def binarySearch(arr,targed):
    st = -1
    end = -1
    ln = len(arr)
    l,r = 0,ln

    #Left search
    while l<r:
        mid = (r+l)//2
        if arr[mid] >= targed:
            r = mid
        else:
            l = mid+1
        if arr[mid] == targed: st = mid
    
    
    # right search
    l,r = 0,ln
    while l<r:
        mid = (r+l)//2
        if arr[mid]<= targed:
            l = mid + 1
        else:
            r = mid
        if arr[r-1] == targed: end = r-1 

    return [st,end]

arr = [0,1,1,3,5,8,8,8,9]
print (binarySearch(arr,8))
    