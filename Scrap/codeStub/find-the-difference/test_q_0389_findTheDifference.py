import pytest
from q_0389_findTheDifference import Solution


@pytest.mark.parametrize("s, t, output", [("abcd", "abcde", "e"), ("", "y", "y")])
class TestSolution:
    def test_findTheDifference(self, s: str, t: str, output: str):
        sc = Solution()
        assert (
            sc.findTheDifference(
                s,
                t,
            )
            == output
        )
