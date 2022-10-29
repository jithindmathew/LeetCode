from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        temp = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                new_word = word[:j] + "*" + word[j + 1:]
                temp[new_word].append(word)

        seen = set([beginWord])

        q = deque([beginWord])

        ans = 1

        while len(q):
            n = len(q)

            for _ in range(n):
                temp_word = q.popleft()

                if temp_word == endWord:
                    return ans

                for i in range(len(temp_word)):
                    new_word = temp_word[:i] + "*" + temp_word[i + 1:]

                    for word in temp[new_word]:
                        if word not in seen:
                            seen.add(word)
                            q.append(word)

            ans += 1

        return 0


s = Solution()
s.ladderLength(beginWord="hit", endWord="cog", wordList=[
               "hot", "dot", "dog", "lot", "log", "cog"])
s.ladderLength(beginWord="hit", endWord="cog", wordList=[
               "hot", "dot", "dog", "lot", "log"])
