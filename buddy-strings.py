class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        a, b = Counter(s), Counter(goal)
        if a != b:
            return False
        diff = sum([1 for i in range(len(s)) if s[i] != goal[i]])
        if diff == 2:
            return True
        elif diff == 0:
            return any(cnt > 1 for char, cnt in a.items())
        else:
            return False
