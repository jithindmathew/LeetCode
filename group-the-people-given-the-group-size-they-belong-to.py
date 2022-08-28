
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        size = len(groupSizes)
        for i in range(size):
            if groupSizes[i] not in dict:
                dict[groupSizes[i]] = [i]

            else:
                dict[groupSizes[i]].append(i)

        ans = []

        for key, value in dict.items():
            front = 0
            back = key
            n = len(value)//key
            while n != 0:
                ans.append(list(value[front:back]))
                n -= 1
                front += key
                back += key
        return ans
