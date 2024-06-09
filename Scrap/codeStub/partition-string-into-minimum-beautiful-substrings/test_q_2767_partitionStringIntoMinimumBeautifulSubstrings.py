import pytest
from q_2767_partitionStringIntoMinimumBeautifulSubstrings import Solution


@pytest.mark.parametrize("s, output", [("1011", 2), ("111", 3), ("0", -1)])
class TestSolution:
    def test_minimumBeautifulSubstrings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumBeautifulSubstrings(
                s,
            )
            == output
        )
