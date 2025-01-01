#problem 1401 LC
#Circle and Rectangle Overlapping
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        Vx = abs(xCenter - (x1+x2)/2) - (x2-x1)/2
        Vy = abs(yCenter - (y1+y2)/2) -(y2-y1)/2
        
        return max(0, Vx) * max(0, Vx) + max(0, Vy) * max(0, Vy) <= (radius **2)
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkOverlap(2,8,6,5,1,10,4))
