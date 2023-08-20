class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

def find_max_profit(jobs):
    jobs.sort(key=lambda job: job.finish)
    n = len(jobs)
    dp = [0] * n
    
    for i in range(n):
        dp[i] = jobs[i].profit
    
    for i in range(1, n):
        for j in range(i):
            if jobs[j].finish <= jobs[i].start:
                dp[i] = max(dp[i], dp[j] + jobs[i].profit)
    
    return max(dp)

# Example usage
jobs = [Job(1, 3, 5), Job(2, 5, 6), Job(4, 6, 5), Job(6, 7, 4), Job(5, 8, 11), Job(7, 9, 2)]
result = find_max_profit(jobs)
print("Maximum profit:", result)
