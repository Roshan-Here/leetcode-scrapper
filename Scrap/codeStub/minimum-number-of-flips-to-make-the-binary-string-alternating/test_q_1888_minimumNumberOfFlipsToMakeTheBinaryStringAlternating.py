import pytest
from q_1888_minimumNumberOfFlipsToMakeTheBinaryStringAlternating import Solution


@pytest.mark.parametrize("s, output", [("111000", 2), ("010", 0), ("1110", 1)])
class TestSolution:
    def test_minFlips(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minFlips(
                s,
            )
            == output
        )
