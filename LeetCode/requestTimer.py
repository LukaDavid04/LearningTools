class RecentCounter(object):
    def __init__(self):
        self.requests = [0]
        self.last = 0
        
    def ping(self, t):
        self.requests.append(t)
        while(True):
            if (t - self.requests[self.last]) > 3001:
                self.last += 1
            else: 
                break
        if len(self.requests) - self.last - 1 == 0:
            return 1
        else:
            return len(self.requests) - self.last - 1
        
recentCounter = RecentCounter()

recentCounter.ping(1);     # requests = [1], range is [-2999,1], return 1
recentCounter.ping(3002);   # requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(6000);  # requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(9000);  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 