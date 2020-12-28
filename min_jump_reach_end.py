def minJumps(arr,n):
    maxR=arr[0]
    step=arr[0]
    jump=1
    if(n==1):
        return 0
    elif(arr[0]==0):
        return -1
    else:
        for i in range(1,n):
            if(i==n-1):
                return jump
            maxR=max(maxR,arr[i]+1)
            step-=1
            if(step==0):
                jump+=1
                if(i>=maxR):
                    return -1
                step=maxR-i
    
    
n=int(input())
arr=list(map(int,input().split()))
print(minJumps(arr,n))