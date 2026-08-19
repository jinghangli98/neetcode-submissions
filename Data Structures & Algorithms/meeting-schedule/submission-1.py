"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key= lambda x: x.start)
        
        for i in range(len(intervals)-1):
            curr_s = intervals[i].start
            curr_e = intervals[i].end

            nxt_s = intervals[i+1].start
            if nxt_s < curr_e:
                return False
        
        return True
            
