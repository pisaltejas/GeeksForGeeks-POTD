class Solution:
    def __init__(self):
        self.map = defaultdict(int)
        self.result = []

    def helper(self, root):
        if not root:
            return ""
        left = self.helper(root.left)
        right = self.helper(root.right)
        curr = "{} {} {}".format(root.data, left, right)
        if self.map[curr] == 1:
            self.result.append(root)
        self.map[curr] += 1

        return curr

    def printAllDups(self, root):
        self.helper(root)
        self.result.sort(key=lambda node: node.data)
        return self.result
