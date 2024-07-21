class Solution:
    def findSwapValues(self, a, n, b, m):
        # Calculate the total sums of both arrays
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Compute the difference between the sums
        total_diff = sum_a - sum_b
        
        # If the difference is odd, it's impossible to balance the sums by swapping a single pair of elements
        if total_diff % 2 != 0:
            return -1
        
        # Desired difference we need to achieve by swapping elements
        target_diff = total_diff // 2
        
        # Convert the first array into a set for O(1) lookup
        set_a = set(a)
        
        # Check each element in the second array
        for elem in b:
            # If there's an element in set_a that, when swapped with elem, balances the sums
            if (elem + target_diff) in set_a:
                return 1
        
        # If no such elements are found, return -1
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends
  #tb
