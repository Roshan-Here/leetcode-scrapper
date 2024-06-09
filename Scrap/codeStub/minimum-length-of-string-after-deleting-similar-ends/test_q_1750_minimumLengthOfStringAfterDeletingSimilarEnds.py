import pytest
from q_1750_minimumLengthOfStringAfterDeletingSimilarEnds import Solution


@pytest.mark.parametrize("s, output", [("ca", 2), ("cabaabac", 0), ("aabccabba", 3)])
class TestSolution:
    def test_minimumLength(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumLength(
                s,
            )
            == output
        )
