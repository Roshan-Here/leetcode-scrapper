import pytest
from q_0712_minimumAsciiDeleteSumForTwoStrings import Solution


@pytest.mark.parametrize(
    "s1, s2, output", [("sea", "eat", 231), ("delete", "leet", 403)]
)
class TestSolution:
    def test_minimumDeleteSum(self, s1: str, s2: str, output: int):
        sc = Solution()
        assert (
            sc.minimumDeleteSum(
                s1,
                s2,
            )
            == output
        )
