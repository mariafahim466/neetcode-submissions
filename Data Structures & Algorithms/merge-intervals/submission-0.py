class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        final = [intervals[0]]

        for start, end in intervals[1:]: 
            lastEnd = final[-1][1]

            if start <= lastEnd: 
                final[-1][1] = max(lastEnd, end)
            else: 
                final.append([start, end])
        return final

