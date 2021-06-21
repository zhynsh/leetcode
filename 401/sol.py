#https://leetcode-cn.com/problems/binary-watch/
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        def binary(a: int):
            return len(bin(a).split('1')) - 1
        for a in range(12):
            if binary(a) <= turnedOn:
                for b in range(60):
                    if binary(b) == turnedOn - binary(a):
                        timestr = str(a) + ':'
                        if b < 10:
                            timestr += '0'
                        timestr += str(b)
                        times.append(timestr)
        return times
