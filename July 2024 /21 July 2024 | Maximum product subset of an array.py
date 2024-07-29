#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        
        n=len(arr)
        max_neg=float("-inf")
        count_zero=0
        count_neg=0
        prod=1
        
        mod=10**9+7
        
        if n==1:
            return arr[0]
        
        for i in range(0,len(arr)):
            
            if arr[i]==0:
                count_zero+=1
                continue
            
            if arr[i]<0:
                max_neg=max(max_neg,arr[i])
                count_neg+=1
                
            prod=(prod*arr[i]) % mod
            
        if count_zero==n:
            return 0
            
        if count_neg % 2 !=0:
            
            if (count_neg==1 and count_zero>0) and (count_neg+count_zero==n):
                return 0
            
            
            prod = (prod * pow(max_neg, mod - 2, mod)) % mod 
            
        return prod


 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends
3tb
