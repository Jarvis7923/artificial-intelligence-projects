class Solution:

    def __init__(self):
        super().__init__()

    def findCheapestPrice(self, n, flights, src, dst, K):
        # m = len(flights)
 
        f_src = self.find_flights_from_src(flights, src, 0, 1)
        if not f_src:
            return -1

        pq = sorted(f_src, key=lambda f: f[2])
        while pq:
            _src, _dst, _cost, k = pq.pop(0)
            if k > K:
                continue
            if _dst == dst:
                return _cost

            f_src = self.find_flights_from_src(flights, _dst, _cost, k+1)
            if not f_src:
                continue
            pq = sorted(f_src + pq, key=lambda f: f[2])
        return -1
                
        
    def find_flights_from_src(self, flights, src, cost, k):
        f = []
        for _src, _dst, _cost in flights:
            if _src == src: 
                f.append([_src, _dst, _cost + cost, k])
        return f 
def find_neighbors(src, deadends=None):
    n = []
    for i in range(4):
        n += change_ele(src, i)
    return n

def change_ele(src, index):
    us = list(src)
    us[index] = '0' if int(us[index]) is '9' else str(int(us[index]) + 1)
    us = ''.join(us)
    ls = list(src)
    ls[index] = '0' if int(ls[index]) is '9' else str(int(ls[index]) - 1)
    ls = ''.join(ls)
    return [us, ls]
        
    

if __name__ == "__main__":
    # n = 3
    # f = [[0,1,100],[1,2,100],[0,2,500]]
    # src = 0
    # dst = 2
    # K = 1
    # s = Solution()
    # res = s.findCheapestPrice(n,f,src,dst,K)
    # pass
    res = find_neighbors("1234")
    
    print(str(int(a)+1))