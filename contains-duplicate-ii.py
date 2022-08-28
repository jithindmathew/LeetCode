class Solution:
    def containsNearbyDuplicate(self, arr, k):

        hashmap = {}
        n = len(arr)
        for i in range(n):
            if arr[i] in hashmap and i - hashmap[arr[i]] <= k:
                return True
            else:
                hashmap[arr[i]] = i
        return False
