# Time - O(n log n), Space - O(n)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timesInt = []
        minTime = 24 * 60

        for i in range(len(timePoints)):
            time = timePoints[i]
            h, m = time.split(":")
            timesInt.append([int(h), int(m)])

        for i in range(1, len(timesInt)):
            total = (timesInt[i][0] - timesInt[i - 1][0]) * 60
            total += (timesInt[i][1] - timesInt[i - 1][1])
            minTime = min(minTime, total)
        
        # First and Last
        oppTime = (timesInt[0][0] + 24 - timesInt[-1][0]) * 60
        oppTime += (timesInt[0][1] - timesInt[-1][1])
        minTime = min(minTime, oppTime)

        return minTime


# Elegant Solution 
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        answer = 1440 + minutes[0] - minutes[-1]
        for i in range(1, len(minutes)):
            answer = min(answer, minutes[i] - minutes[i - 1])
        return answer