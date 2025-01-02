#problem 1823 LC

#find winner of Circular Game
class Solution(object):
    def findTheWinner(self, n, k):
        array = [i for i in range(1, n+1)]
        t = 0
        while len(array) >1:
            t = (t + (k-1)) % len(array)
            array.pop(t)
        return array[0]