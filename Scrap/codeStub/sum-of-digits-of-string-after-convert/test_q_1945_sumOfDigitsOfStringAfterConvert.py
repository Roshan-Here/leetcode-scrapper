import pytest
from q_1945_sumOfDigitsOfStringAfterConvert import Solution


@pytest.mark.parametrize(
    "s, k, output", [("iiii", 1, 36), ("leetcode", 2, 6), ("zbax", 2, 8)]
)
class TestSolution:
    def test_getLucky(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.getLucky(
                s,
                k,
            )
            == output
        )
