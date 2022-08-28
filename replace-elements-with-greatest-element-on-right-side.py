class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        maxtillnow = arr[-1]
        temp = arr[-1]
        
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > maxtillnow:
                temp = arr[i]
            arr[i] = maxtillnow
            maxtillnow = temp
            
        arr[-1] = -1
        return arr
            