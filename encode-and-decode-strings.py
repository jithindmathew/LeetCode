class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
        ans = ""

        for i in strs:
            ans += str(len(i)) + '/' + i

        # print(ans)
        return ans

    def decode(self, strs):
        # write your code here
        n = len(strs)

        i = 0

        ans = []

        while i < n:

            first = i + 1

            while first < n:
                if strs[first] == '/':
                    break

                first += 1

            length = int(strs[i:first])

            ans.append(strs[first + 1: first + length + 1])

            i = first + length + 1

            # print(ans)

        return ans


s = Solution()

tests = [
    ["we", "say", ":", "yes"],
    ["lint", "co//de", "love", "you", "stupid"],
    ["a"],
    [],
    ["////// // e3d3dd3d3"],
    ['2/', '234/', '/', '1/', '2//', '3///', '', 'rr/', ' ']
]

for i in tests:
    print(i)
    print(s.decode(s.encode(i)))
    print(s.decode(s.encode(i)) == i)
