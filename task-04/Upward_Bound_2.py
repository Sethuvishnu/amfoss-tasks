times = int(input())
for i in range(times):
    n = int(input())
    s = list(map(int, input().split()))
    t=0
    def is_sorted(arr):
        n = len(arr)
        for i in range(n - 1):
            if arr[i] >=arr[i + 1]:
                return False
        return True


    while not is_sorted(s):
        for i in range(len(s)-1):
        

            if s[i]>=s[i+1]:
                s[i]=s[i]//2
                t+=1
        if s[0]==0 and s[1]==0:
            t=-1
            break
    print(t)
