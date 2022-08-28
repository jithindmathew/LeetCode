class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        return self.findKthLarges(arr, len(arr)+1-k, 0, len(arr)-1)

    def findKthLarges(self, arr: List[int], k: int, low, high) -> int:
        def partition(low, high):
            ind = (low+high)//2
            pivot = arr[ind]
            # print("pivot",pivot)
            pivot_ind = high
            arr[ind], arr[high] = arr[high], arr[ind]
            while(low < high):
                while(low < high):
                    if arr[low] > pivot:
                        break
                    low += 1

                while(low < high):
                    if arr[high] < pivot:
                        break
                    high -= 1
                if low < high:
                    arr[low], arr[high] = arr[high], arr[low]
            arr[high], arr[pivot_ind] = arr[pivot_ind], arr[high]
            # print(arr)
            return high
        ind = partition(low, high)
        if ind+1 == k:
            return arr[ind]
        elif ind+1 > k:
            return self.findKthLarges(arr, k, low, ind-1)
        else:
            return self.findKthLarges(arr, k, ind+1, high)
