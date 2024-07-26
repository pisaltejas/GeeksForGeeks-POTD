#User function Template for python3
class Solution:
    def kPangram(self,string, k):
    # code here
        arr = [0] * 26
        count = 0
        op = 0
        
        # Count frequencies of each character in the string
        for char in string:
            if char != ' ':
                arr[ord(char) - ord('a')] += 1
                count += 1
        
        # Count the number of missing characters
        for i in range(26):
            if arr[i] == 0:
                op += 1
        
        # Check if the number of operations needed is less than or equal to k
        # and if the string contains at least 26 alphabetic characters
        return (op <= k) and (count >= 26)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends
#tb
