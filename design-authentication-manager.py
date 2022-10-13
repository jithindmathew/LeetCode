class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.dictt = dict()
        self.time_to_live = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dictt[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dictt and \
           self.dictt[tokenId] + self.time_to_live > currentTime:
            self.dictt[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0

        for i in self.dictt:
            if self.dictt[i] + self.time_to_live > currentTime:
                ans += 1

        return ans

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
