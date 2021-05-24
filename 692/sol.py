#https://leetcode-cn.com/problems/top-k-frequent-words/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashidx = dict();
        for i in words:
            if i in hashidx.keys():
                hashidx[i] = hashidx[i] + 1;
            else:
                hashidx[i] = 1;
        #hashidx = sorted(hashidx.iteritems(), key = lambda d: d[1], reverse = True);
        sol = []
        items = hashidx.items();
        for i in items:
            sol.append([i[1], i[0]]);
        sol.sort();
        #sol = sorted(sol,key=(lambda sol:[-int(sol[1]), sol[0]]));
        sol = sorted(sol, key = lambda sol :(-sol[0], sol[1]));
        sol2 = []
        for i in range(k):
            sol2.append(sol[i][1]);
        return sol2;
