from heapq import heappush
from heapq import heappop
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for task in tasks:
            if task in dic:
                dic[task] += 1
            else:
                dic[task] = 1
        h = []
        cnt = 0
        for v in dic.values():
            heappush(h, -v)
        while len(h) != 0:
            k = n + 1
            lst = []
            while k > 0 and len(h) != 0:
                freq = heappop(h)
                if freq + 1 < 0:
                    lst.append(freq+1)
                cnt += 1
                k -= 1
            for freq in lst:
                heappush(h, freq)
            if k != 0 and len(h) != 0:
                cnt += k
        return cnt








from collections import deque
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for task in tasks:
            if task not in dic:
                dic[task] = [task, 1]
            else:
                dic[task][1] += 1
        
        lst = list(dic.values())
        lst.sort(key=lambda x:x[1])
        i = len(lst) - 1
        while i >= 0 and lst[i][1] == lst[-1][1]:
            i-=1
        return max((lst[-1][1]-1)*(n+1) + len(lst)-1-i, len(tasks))