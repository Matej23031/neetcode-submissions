"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if intervals == []:
            return 0
        
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()

        s = 0
        e = 0
        cnt = 0
        max_cnt = -math.inf
        while s < len(intervals):
            print(cnt)
            if(start[s] < end[e]):
                cnt += 1
                max_cnt = max(max_cnt, cnt )
                s += 1
            else:
                cnt -= 1
                max_cnt = max(max_cnt,cnt)
                e += 1

        return max_cnt
