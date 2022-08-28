class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:

        A[-1] += K

        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i], 10)
            if i:
                A[i-1] += K
        while K:
            A = [K % 10] + A
            K //= 10
        return A
