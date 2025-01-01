#problem 661 LC

#Image Smoothener
class Solution(object):
    def imageSmoother(self, img):
        if not img:
            return []
        
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                count = 0
                total = 0
                for i in range(max(0, r-1), min(rows, r+2)):
                    for j in range(max(0, c-1), min(cols, c+2)):
                        total += img[i][j]
                        count += 1
                result[r][c] = total // count
        
        return result

