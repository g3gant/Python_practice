def findgrid(n,m):
    if (n==1 or m==1):
        return 1
    #print (n-1,m)
    return findgrid(n-1,m)+findgrid(n,m-1)

print (findgrid(3,5))