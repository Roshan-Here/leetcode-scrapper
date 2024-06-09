import pytest
from q_2272_substringWithLargestVariance import Solution


@pytest.mark.parametrize("s, output", [("aababbb", 3), ("abcde", 0)])
class TestSolution:
    def test_largestVariance(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.largestVariance(
                s,
            )
            == output
        )
