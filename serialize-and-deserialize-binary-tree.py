# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        def encode_dfs(node):
            if not node:
                ans.append('N')
                return

            ans.append(str(node.val))

            encode_dfs(node.left)
            encode_dfs(node.right)

        ans = []

        encode_dfs(root)

        return ','.join(ans)

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0

        def decode_dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))

            self.i += 1

            node.left = decode_dfs()
            node.right = decode_dfs()

            return node
        return decode_dfs()




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
