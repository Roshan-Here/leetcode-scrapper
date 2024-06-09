import pytest
from q_0686_repeatedStringMatch import Solution


@pytest.mark.parametrize("a, b, output", [("abcd", "cdabcdab", 3), ("a", "aa", 2)])
class TestSolution:
    def test_repeatedStringMatch(self, a: str, b: str, output: int):
        sc = Solution()
        assert (
            sc.repeatedStringMatch(
                a,
                b,
            )
            == output
        )
