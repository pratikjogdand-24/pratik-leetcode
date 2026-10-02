class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty,profit))
        worker.sort()

        ans = 0
        max_profit = 0 
        j = 0

        for w in worker :
            while j  < len(jobs) and jobs[j][0] <= w:
                max_profit = max(max_profit,jobs[j][1])
                j+=1
            ans += max_profit
        return ans