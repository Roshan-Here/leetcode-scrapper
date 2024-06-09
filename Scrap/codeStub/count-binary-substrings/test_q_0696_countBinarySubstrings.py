import pytest
from q_0696_countBinarySubstrings import Solution


@pytest.mark.parametrize("s, output", [("00110011", 6), ("10101", 4)])
class TestSolution:
    def test_countBinarySubstrings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countBinarySubstrings(
                s,
            )
            == output
        )
