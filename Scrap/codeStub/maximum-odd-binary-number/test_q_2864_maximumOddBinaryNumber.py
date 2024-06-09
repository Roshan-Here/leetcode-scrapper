import pytest
from q_2864_maximumOddBinaryNumber import Solution


@pytest.mark.parametrize("s, output", [("010", "001"), ("0101", "1001")])
class TestSolution:
    def test_maximumOddBinaryNumber(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.maximumOddBinaryNumber(
                s,
            )
            == output
        )
