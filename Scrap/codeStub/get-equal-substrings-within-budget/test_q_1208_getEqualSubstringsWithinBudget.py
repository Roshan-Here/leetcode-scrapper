import pytest
from q_1208_getEqualSubstringsWithinBudget import Solution


@pytest.mark.parametrize(
    "s, t, maxCost, output",
    [("abcd", "bcdf", 3, 3), ("abcd", "cdef", 3, 1), ("abcd", "acde", 0, 1)],
)
class TestSolution:
    def test_equalSubstring(self, s: str, t: str, maxCost: int, output: int):
        sc = Solution()
        assert (
            sc.equalSubstring(
                s,
                t,
                maxCost,
            )
            == output
        )
