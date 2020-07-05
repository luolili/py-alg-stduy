import typing


def travese_better(x: int) -> int:
    def helper(x, res=0):
        x = x if x > 0 else -x
        if x == 0:
            return res
        res = res * 10 + x % 10
        w = helper(x // 10, res)
        if res > 2 ** 31:
            return 0
        return w

    return helper(x) if x >= 0 else -1 * helper(x)
