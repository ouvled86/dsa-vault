class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        w = len(matrix[0])
        h = len(matrix)
        r =  w * h - 1
        
        while l <= r:
            mid = (l + r) // 2
            x = mid % w
            y = mid // w
            if matrix[y][x] == target:
                return True
            if matrix[y][x] > target:
                r = mid - 1
            elif matrix[y][x] < target:
                l = mid + 1
           
        return False
    