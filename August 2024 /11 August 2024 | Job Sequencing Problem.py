#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    def JobScheduling(self,Jobs,n):
        
        # code edutechbarsha
        # Sorting jobs based on profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Find maximum deadline to define the size of the time slots array
        max_deadline = max(job.deadline for job in Jobs)
        
        # Array to track which slots are filled
        time_slots = [-1] * (max_deadline + 1)  # using max_deadline + 1 for 1-based index

        total_jobs = 0
        total_profit = 0
        
        # Iterating over each job
        for job in Jobs:
            # Finding a slot for the job
            for j in range(min(max_deadline, job.deadline), 0, -1):
                if time_slots[j] == -1:  # If slot is empty
                    time_slots[j] = job.id
                    total_jobs += 1
                    total_profit += job.profit
                    break
        
        return total_jobs, total_profit


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends
