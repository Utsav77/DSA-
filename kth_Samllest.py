def partition(arr,l,r):
    x=arr[r]
    i=l
    for j in range(l,r):
        if(arr[j]<=x):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[r]=arr[r],arr[i]
    return i
    
    
def kthSmallest(arr, l, r, k):
    if(k>0 and k<=r-l+1):
        pivot_pos=partition(arr,l,r)
    
    if(pivot_pos-l==k-1):
        return arr[pivot_pos]
    elif(pivot_pos-l>k-1):
        return kthSmallest(arr, l, pivot_pos-1, k)
    else:
        return kthSmallest(arr, pivot_pos+1 , r, k-pivot_pos+l-1)
        
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    print(kthSmallest(arr,0,n-1,k))
