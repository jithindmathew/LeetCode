class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        size = len(bed) - 1
        i = 1
        while i < size:
            if bed[i] == bed[i - 1] == bed[i + 1] == 0:
                bed[i] = 1
                n -= 1
                i += 2
                
            else:
                i += 1
                
            if n <= 0: return True
        return False
            