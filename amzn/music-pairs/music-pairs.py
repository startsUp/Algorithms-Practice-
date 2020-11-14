class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reminders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += reminders[0]
            else: # check if a%60+b%60==60
                ret += reminders[60-t%60]
            reminders[t % 60] += 1 # reminder to update the reminders
        return ret