class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, p):
            if len(p) == n * 2:
                l.append(p)
                return
            if left < n:
                dfs(left + 1, right, p + "(")
            if right < left:
                dfs(left, right + 1, p + ")")
        l = []
        dfs(0, 0, "")
        return l