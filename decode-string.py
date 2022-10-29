class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp_str = ""

                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str

                stack.pop()

                temp_num = ""

                while stack and stack[-1].isdigit():
                    temp_num = stack.pop() + temp_num

                stack.append(temp_str * int(temp_num))

        return "".join(stack)
